import codecs
import json
import sys
import argparse
import signal
from mastodoner.crawler import Crawler
from mastodoner.version import version

def validate_output_file(value):
    if not value.endswith(".jsonl"):
        raise argparse.ArgumentTypeError("Output file must have a .jsonl extension")
    return value

def write_output_file(output_file, items):
    with codecs.open(output_file, 'wb', encoding='utf-8') as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

def main():
    
    # Create the parser
    parser = argparse.ArgumentParser(description="Crawl public data from Mastodon instance and save to a JSON Lines file.")
    subparsers = parser.add_subparsers(dest="command")

    # Create the version subparser
    version_parser = subparsers.add_parser("version", help="Check mastodoner version")

    # Create the instance subparser
    instance_parser = subparsers.add_parser("instance", help="Crawl instance endpoints")
    instance_parser.add_argument("--instance-url", required=True, help="Base URL of the Mastodon instance e.g. mastodon.online")
    instance_parser.add_argument("--node-info", action="store_true", help="Crawl node information of the instance")
    instance_parser.add_argument("--info", action="store_true", help="Crawl general information about the instance")
    instance_parser.add_argument("--peers", action="store_true", help="Crawl list of instance(s) that given instance is aware of")
    instance_parser.add_argument("--activity", action="store_true", help="Crawl instance activity over the last 3 months (binned weekly)")
    instance_parser.add_argument("--rules", action="store_true", help="Crawl rules that the users of given instance should follow")
    instance_parser.add_argument("--blocks", action="store_true", help="Crawl list of instance(s) blocked by given instance")
    instance_parser.add_argument("--trends", action="store_true", help="Crawl (hash)tags, statuses or links that trended within the past week on given instance. Use --type to specify the trend type (default: tags)")
    instance_parser.add_argument("--trend-type", choices=["tags", "statuses", "links"], help="Optional argument used with --trends to specify the type of trend (default: tags)")
    instance_parser.add_argument("--directory", action="store_true", help="Crawl instance directory i.e. user profiles")
    instance_parser.add_argument("--order", choices=["new", "active"], help="Optional argument used with --directory to specify the order of response (default: active)")
    instance_parser.add_argument("--include-remote", action="store_true", help="Optional argument used with --directory to include remote users")
    instance_parser.add_argument("--timeline", action="store_true", help="Crawl public timeline of given instance")
    instance_parser.add_argument("--only-local", action="store_true", help="Optional argument used with --timeline to crawl only local statuses")
    instance_parser.add_argument("--only-remote", action="store_true", help="Optional argument used with --timeline to crawl only remote statuses")
    instance_parser.add_argument("--only-media", action="store_true", help="Optional argument used with --timeline to filter out statuses without attachments")
    instance_parser.add_argument("--limit", type=int, help="Optional argument used with --trends, --directory or --timeline to limit the response")
    instance_parser.add_argument("output_file", type=validate_output_file, help="Output file (JSON Lines format)")

    # Create the user subparser
    user_parser = subparsers.add_parser("user", help="Crawl user endpoints")
    user_parser.add_argument("--username", required=True, help="Username of the Mastodon user in the format user@domain e.g. ignactro@mastodon.social")
    user_parser.add_argument("--info", action="store_true", help="Crawl user profile information")
    user_parser.add_argument("--statuses", action="store_true", help="Crawl statuses posted by the given user")
    user_parser.add_argument("--followers", action="store_true", help="Crawl users which follow the given user")
    user_parser.add_argument("--following", action="store_true", help="Crawl users which the given user follows")
    user_parser.add_argument("--limit", type=int, help="Optional argument used with --statuses, --followers or --following to limit the response")
    user_parser.add_argument("--only-media", action="store_true", help="Optional argument used with --statuses to filter out statuses without attachments")
    user_parser.add_argument("--exclude-replies", action="store_true", help="Optional argument used with --statuses to filter out statuses in reply to a different user")
    user_parser.add_argument("--exclude-reblogs", action="store_true", help="Optional argument used with --statuses to filter out reblogs (reposts)")
    user_parser.add_argument("--only-pinned", action="store_true", help="Optional argument used with --statuses to filter pinned statuses only")
    user_parser.add_argument("output_file", type=validate_output_file, help="Output file (JSON Lines format)")

    # Create the status subparser
    status_parser = subparsers.add_parser("status", help="Crawl status endpoints")
    status_parser.add_argument("--instance-url", required=True, help="Base URL of the Mastodon instance e.g. mastodon.online")
    status_parser.add_argument("--status-id", required=True, help="ID of the status on Mastodon instance")
    status_parser.add_argument("--info", action="store_true", required=True, help="Crawl information about the status")
    status_parser.add_argument("output_file", type=validate_output_file, help="Output file (JSON Lines format)")

    # Create the discover subparser
    discover_parser = subparsers.add_parser("discover", help="Discover instances")
    discover_parser.add_argument("--bearer-token", help="Bearer token for the 'instances.social' API. Alternatively, bearer token can also be provided by setting the 'INSTANCES_SOCIAL_TOKEN' environment variable. You can get the token from 'https://instances.social/api/doc/'")
    discover_parser.add_argument("--count", type=int, help="Number of instances to discover. Value between 1 and 10000 (default: 0 i.e. all instances)")
    discover_parser.add_argument("--include-dead", action="store_true", help="Include dead (down for at least two weeks) instances")
    discover_parser.add_argument("--include-down", action="store_true", help="Include down instances")
    discover_parser.add_argument("--include-closed", action="store_true", help="Include instances with closed registrations")
    discover_parser.add_argument("--min-users", type=int, help="Minimum users discovered instances must have. Value greater than or equal to 1")
    discover_parser.add_argument("--max-users", type=int, help="Maximum users discovered instances must have. Value greater than or equal to 1")
    discover_parser.add_argument("output_file", type=validate_output_file, help="Output file (JSON Lines format)")
    
    args = parser.parse_args()

    crawler = Crawler()

    items = []

    # log and stop when process receives SIGINT
    def stop(signal, frame):
        crawler.logger.warn("Process received SIGINT, stopping")
        sys.exit(0)

    signal.signal(signal.SIGINT, stop)

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "version":
        print(f"mastodoner {version}")
        sys.exit(0)

    if args.command == "instance":

        if sum([args.node_info, args.info, args.peers, args.activity, args.rules, args.blocks, args.trends, args.directory, args.timeline]) != 1:
            crawler.logger.error("Exactly one of --node-info, --info, --peers, --activity, --rules, --blocks, --trends, --directory, --timeline must be specified")
            sys.exit(1)

        if args.limit is not None and not (args.trends or args.directory or args.timeline):
            crawler.logger.error("--limit can only be used with --trends, --directory, or --timeline")
            sys.exit(1)

        if (args.trend_type is not None) and not args.trends:
            crawler.logger.error("--trend-type can only be used with --trends")
            sys.exit(1)

        if (args.order is not None or args.include_remote) and not args.directory:
            crawler.logger.error("--order and --include-remote can only be used with --directory")
            sys.exit(1)

        if (args.only_local or args.only_remote or args.only_media) and not args.timeline:
            crawler.logger.error("--only-local, --only-remote and --only-media can only be used with --timeline")
            sys.exit(1)

        if args.only_local and args.only_remote:
            crawler.logger.error("Only one of --only-local, --only-remote can be specified")
            sys.exit(1)

        if args.node_info:
            items = crawler.instance_nodeinfo(args.instance_url)

        elif args.info:
            items = crawler.instance_lookup(args.instance_url)

        elif args.peers:
            items = crawler.instance_peers(args.instance_url)

        elif args.activity:
            items = crawler.instance_activity(args.instance_url)

        elif args.rules:
            items = crawler.instance_rules(args.instance_url)

        elif args.blocks:
            items = crawler.instance_blocks(args.instance_url)

        elif args.trends:
            trend_type = "tags"
            
            if args.trend_type is not None:
                trend_type = args.trend_type
            
            if args.limit is not None:
                items = crawler.instance_trends(args.instance_url, args.limit, trend_type)
            else:
                items = crawler.instance_trends_all(args.instance_url, trend_type)

        elif args.directory:
            include_remote=False
            order = "active"

            if args.include_remote:
                include_remote=True

            if args.order is not None:
                order = args.order
            
            if args.limit is not None:
                items = crawler.instance_directory(args.instance_url, args.limit, order, include_remote)
            else:
                items = crawler.instance_directory_all(args.instance_url, order, include_remote)

        elif args.timeline:
            only_local=False
            only_remote=False
            only_media=False

            if args.only_local:
                only_local = True
            if args.only_remote:
                only_remote = True
            if args.only_media:
                only_media = True
            
            if args.limit is not None:
                items = crawler.instance_timeline(args.instance_url, args.limit, only_local, only_remote, only_media)
            else:
                items = crawler.instance_timeline_all(args.instance_url, only_local, only_remote, only_media)

    elif args.command == "user":
        
        if sum([args.info, args.statuses, args.followers, args.following]) != 1:
            crawler.logger.error("Exactly one of --info, --statuses, --followers, --following must be specified")
            sys.exit(1)

        if args.limit is not None and not (args.statuses or args.followers or args.following):
            crawler.logger.error("--limit can only be used with --statuses, --followers, or --following")
            sys.exit(1)

        if (args.only_media or args.exclude_replies or args.exclude_reblogs or args.only_pinned) and not args.statuses:
            crawler.logger.error("--only-media, --exclude-replies, --exclude-reblogs, and --only-pinned can only be used with --statuses")
            sys.exit(1)
            
        if args.info:
            items = crawler.user_lookup(args.username)

        elif args.statuses:
            only_media=False
            exclude_replies=False
            exclude_reblogs=False
            only_pinned=False
            
            if args.only_media:
                only_media = True
            if args.exclude_replies:
                exclude_replies = True
            if args.exclude_reblogs:
                exclude_reblogs = True
            if args.only_pinned:
                only_pinned = True
                
            if args.limit is not None:
                items = crawler.user_statuses(args.username, args.limit, only_media, exclude_replies, exclude_reblogs, only_pinned)
            else:
                items = crawler.user_statuses_all(args.username, only_media, exclude_replies, exclude_reblogs, only_pinned)

        elif args.followers:
            if args.limit is not None:
                items = crawler.user_followers(args.username, args.limit)
            else:
                items = crawler.user_followers_all(args.username)

        elif args.following:
            if args.limit is not None:
                items = crawler.user_following(args.username, args.limit)
            else:
                items = crawler.user_following_all(args.username)

    elif args.command == "status":

        if args.info:
            items = crawler.status_lookup(args.instance_url, args.status_id)
            
    elif args.command == "discover":

        instance_social_bearer_token=None
        count=0
        include_dead=False
        include_down=False
        include_closed=False
        min_users=0
        max_users=0

        if args.bearer_token:
            instance_social_bearer_token = args.bearer_token

        if args.count:
            count = args.count

        if args.include_dead:
            include_dead = True

        if args.include_down:
            include_down = True

        if args.include_closed:
            include_closed = True

        if args.min_users:
            min_users = args.min_users

        if args.max_users:
            max_users = args.max_users

        items = crawler.discover_instances(instance_social_bearer_token, count, include_dead, include_down, include_closed, min_users, max_users)

    # Write output to the output file
    if len(items) > 0:
        write_output_file(args.output_file, items)
        crawler.logger.info(f"Output saved to {args.output_file}")
        

if __name__ == "__main__":
    main()

import codecs
import json
import sys
import argparse
import signal
from mastodoner.crawler import Crawler
from mastodoner import version

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
    parser = argparse.ArgumentParser(description="Crawl Mastodon instance endpoints and save to a JSON Lines file.")
    subparsers = parser.add_subparsers(dest="command")

    # Create the version subparser
    version_parser = subparsers.add_parser("version", help="Check mastodoner version")

    # Create the directory subparser
    directory_parser = subparsers.add_parser("directory", help="Crawl instance directory i.e. local users")
    directory_parser.add_argument("--instance-url", required=True, help="Base URL of the Mastodon instance e.g. mastodon.online")
    directory_parser.add_argument("output_file", type=validate_output_file, help="Output file to save the instance directory (JSON Lines format)")

    # Create the user subparser
    user_parser = subparsers.add_parser("user", help="Crawl profile of a user")
    user_parser.add_argument("--username", required=True, help="Username of the Mastodon user in the format user@domain e.g. ignactro@mastodon.social")
    user_parser.add_argument("output_file", type=validate_output_file, help="Output file to save the user profile (JSON Lines format)")

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

    if args.command == "directory":
        items = crawler.local_instance_directory_all(args.instance_url)

    elif args.command == "user":
        items = crawler.user_lookup(args.username)

    # Write output to the output file
    if len(items) > 0:
        write_output_file(args.output_file, items)
        crawler.logger.info(f"Output saved to {args.output_file}")
        

if __name__ == "__main__":
    main()

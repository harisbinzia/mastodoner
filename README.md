# Mastodoner

Mastodoner is a command line tool (and Python library) for archiving [Mastodon](https://joinmastodon.org), a decentralized micro-blogging social network. Mastodoner does not currently require any authentication with Mastodon; it gathers all data through publicly accessible endpoints. 

## Installation

Install the mastodoner with ```pip```:

```
pip install -U mastodoner
```

Alternatively, you can also clone the latest version from the [repository](https://github.com/harisbinzia/mastodoner) and install it directly from the source code:

```
pip install -e .
```

**Note: Mastodoner requires Python 3.8 or higher.**

## CLI Usage

```
usage: mastodoner [-h] {version,instance,user} ...

Crawl Mastodon instance endpoints and save to a JSON Lines file.

positional arguments:
  {version,instance,user}
    version             Check mastodoner version
    instance            Crawl instance endpoints
    user                Crawl user endpoints

optional arguments:
  -h, --help            show this help message and exit
```

There are two main commands: ```instance``` and ```user```. Here is how you use each of them:

* ```instance```

```
usage: mastodoner instance [-h] --instance-url INSTANCE_URL [--node-info] [--info] [--peers] [--activity] [--rules] [--blocks] [--trends]
                           [--trend-type {tags,statuses,links}] [--directory] [--order {new,active}] [--include-remote] [--timeline] [--only-local]
                           [--only-remote] [--only-media] [--limit LIMIT]
                           output_file

positional arguments:
  output_file           Output file to save the instance directory (JSON Lines format)

optional arguments:
  -h, --help            show this help message and exit
  --instance-url INSTANCE_URL
                        Base URL of the Mastodon instance e.g. mastodon.online
  --node-info           Crawl node information of the instance
  --info                Crawl general information about the instance
  --peers               Crawl list of instance(s) that given instance is aware of
  --activity            Crawl instance activity over the last 3 months (binned weekly)
  --rules               Crawl rules that the users of given instance should follow
  --blocks              Crawl list of instance(s) blocked by given instance
  --trends              Crawl (hash)tags, statuses or links that trended within the past week on given instance. Use --type to specify the trend type
                        (default: tags)
  --trend-type {tags,statuses,links}
                        Optional argument used with --trends to specify the type of trend (default: tags)
  --directory           Crawl instance directory i.e. user profiles
  --order {new,active}  Optional argument used with --directory to specify the order of response (default: active)
  --include-remote      Optional argument used with --directory to include remote users
  --timeline            Crawl public timeline of given instance
  --only-local          Optional argument used with --timeline to crawl only local statuses
  --only-remote         Optional argument used with --timeline to crawl only remote statuses
  --only-media          Optional argument used with --timeline to filter out statuses without attachments
  --limit LIMIT         Optional argument used with --trends, --directory or --timeline to limit the response
```

* ```user```

```
usage: mastodoner user [-h] --username USERNAME [--info] [--statuses] [--followers] [--following] [--limit LIMIT] [--only-media] [--exclude-replies]
                       [--exclude-reblogs] [--only-pinned]
                       output_file

positional arguments:
  output_file          Output file to save the user profile (JSON Lines format)

optional arguments:
  -h, --help           show this help message and exit
  --username USERNAME  Username of the Mastodon user in the format user@domain e.g. ignactro@mastodon.social
  --info               Crawl user profile information
  --statuses           Crawl statuses posted by the given user
  --followers          Crawl users which follow the given user
  --following          Crawl users which the given user follows
  --limit LIMIT        Optional argument used with --statuses, --followers or --following to limit the response
  --only-media         Optional argument used with --statuses to filter out statuses without attachments
  --exclude-replies    Optional argument used with --statuses to filter out statuses in reply to a different user
  --exclude-reblogs    Optional argument used with --statuses to filter out reblogs (reposts)
  --only-pinned        Optional argument used with --statuses to filter pinned statuses only
```

## Intended Use

Mastodoner is developed to support academic research. The data collected through Mastodoner should only be used for research purposes. Mastodoner gathers all data through publicly accessible endpoints and strictly adheres to the rate limits set for each endpoint.

## Contributing

Contributions are welcome! For small bug fixes and minor improvements, feel free to just open a PR. For larger changes, please open an issue first so that other contributors can discuss your plan, avoid duplicated work, and ensure it aligns with the goals of the project. Thanks!

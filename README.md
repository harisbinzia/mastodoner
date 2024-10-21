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
usage: mastodoner [-h] {version,instance,user,status,discover} ...

Crawl public data from Mastodon instance and save to a JSON Lines file.

positional arguments:
  {version,instance,user,status,discover}
    version             Check mastodoner version
    instance            Crawl instance endpoints
    user                Crawl user endpoints
    status              Crawl status endpoints
    discover            Discover instances

optional arguments:
  -h, --help            show this help message and exit
```

There are four main commands: ```instance```, ```user```, ```status```, ```discover```. Here is how you use each of them:

* ```instance```

```
usage: mastodoner instance [-h] --instance-url INSTANCE_URL [--node-info] [--info] [--peers] [--activity] [--rules] [--blocks] [--trends]
                           [--trend-type {tags,statuses,links}] [--directory] [--order {new,active}] [--include-remote] [--timeline] [--only-local]
                           [--only-remote] [--only-media] [--limit LIMIT]
                           output_file

positional arguments:
  output_file           Output file (JSON Lines format)

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
  output_file          Output file (JSON Lines format)

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

* ```status```

```
usage: mastodoner status [-h] --instance-url INSTANCE_URL --status-id STATUS_ID --info output_file

positional arguments:
  output_file           Output file (JSON Lines format)

optional arguments:
  -h, --help            show this help message and exit
  --instance-url INSTANCE_URL
                        Base URL of the Mastodon instance e.g. mastodon.online
  --status-id STATUS_ID
                        ID of the status on Mastodon instance
  --info                Crawl information about the status
```

* ```discover```

```
usage: mastodoner discover [-h] [--bearer-token BEARER_TOKEN] [--count COUNT] [--include-dead] [--include-down] [--include-closed]
                           [--min-users MIN_USERS] [--max-users MAX_USERS]
                           output_file

positional arguments:
  output_file           Output file (JSON Lines format)

optional arguments:
  -h, --help            show this help message and exit
  --bearer-token BEARER_TOKEN
                        Bearer token for the 'instances.social' API. Alternatively, bearer token can also be provided by setting the
                        'INSTANCES_SOCIAL_TOKEN' environment variable. You can get the token from 'https://instances.social/api/doc/'
  --count COUNT         Number of instances to discover. Value between 1 and 10000 (default: 0 i.e. all instances)
  --include-dead        Include dead (down for at least two weeks) instances
  --include-down        Include down instances
  --include-closed      Include instances with closed registrations
  --min-users MIN_USERS
                        Minimum users discovered instances must have. Value greater than or equal to 1
  --max-users MAX_USERS
                        Maximum users discovered instances must have. Value greater than or equal to 1
```

## Python Usage

You can also use Mastodoner as a Python library. For example, here's how you can crawl a user's info:

```python
from mastodoner import Crawler
crawler = Crawler()
user_info = crawler.user_lookup('ignactro@mastodon.social')
```

For more examples of using Mastodoner as a Python library, check out the Colab. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Feb8ysG6dy1si1o1C4sAyIspVUsqNKF6?usp=sharing)

## Intended Use

Mastodoner is developed to support academic research. The data collected through Mastodoner should only be used for research purposes. Mastodoner gathers all data through publicly accessible endpoints and strictly adheres to the rate limits set for each endpoint.

## Contributing

Contributions are welcome! For small bug fixes and minor improvements, feel free to just open a PR. For larger changes, please open an issue first so that other contributors can discuss your plan, avoid duplicated work, and ensure it aligns with the goals of the project. Thanks!

## Reference

If you use this tool in any of your work, please cite below paper.
```
@inproceedings{10.1145/3627673.3679217,
author = {Zia, Haris Bin and Castro, Ignacio and Tyson, Gareth},
title = {Mastodoner: A Command-line Tool and Python Library for Public Data Collection from Mastodon},
year = {2024},
isbn = {9798400704369},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3627673.3679217},
doi = {10.1145/3627673.3679217},
booktitle = {Proceedings of the 33rd ACM International Conference on Information and Knowledge Management},
pages = {5314–5317},
numpages = {4},
location = {Boise, ID, USA},
series = {CIKM '24}
}
```

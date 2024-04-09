import logging
import time
import requests
from datetime import datetime

class Crawler:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.rate_limits = {}

    def instance_nodeinfo(self, instance_url):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")
        
        try:
            response = requests.get(f"https://{instance_url}/nodeinfo/2.0", timeout=120)
    
            if response.status_code == 200:
                self.logger.info(f"Crawled node information of instance {instance_url}.")
                return [response.json()]
            else:
                self.logger.error(f"Failed to fetch node information of instance {instance_url}. Status code: {response.status_code}")
                return []
    
        except Exception as e:
            self.logger.error(f"Error occurred while crawling node information of instance {instance_url}: {str(e)}")
            return []    
    
    def instance_lookup(self, instance_url):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")
        
        try:            
            # Check rate limit for this instance
            remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
            if remaining_requests is not None and remaining_requests < 5:
                wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                if wait_time > 0:
                    self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                    time.sleep(wait_time)
    
            response = requests.get(f"https://{instance_url}/api/v2/instance", timeout=120)
                
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            reset_time_str = response.headers.get('X-RateLimit-Reset')
            reset_time = datetime.fromisoformat(reset_time_str[:-1])
            self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
            if response.status_code == 200:
                self.logger.info(f"Crawled information of instance {instance_url}.")
                return [response.json()]
            else:
                self.logger.error(f"Failed to fetch information of instance {instance_url}. Status code: {response.status_code}")
                return []
    
        except Exception as e:
            self.logger.error(f"Error occurred while crawling information of instance {instance_url}: {str(e)}")
            return []    

    def instance_peers(self, instance_url):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")
        
        try:            
            # Check rate limit for this instance
            remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
            if remaining_requests is not None and remaining_requests < 5:
                wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                if wait_time > 0:
                    self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                    time.sleep(wait_time)
    
            response = requests.get(f"https://{instance_url}/api/v1/instance/peers", timeout=120)
                
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            reset_time_str = response.headers.get('X-RateLimit-Reset')
            reset_time = datetime.fromisoformat(reset_time_str[:-1])
            self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
            if response.status_code == 200:
                self.logger.info(f"Crawled peers of instance {instance_url}.")
                return [{'peers': response.json()}]
            else:
                self.logger.error(f"Failed to fetch peers of instance {instance_url}. Status code: {response.status_code}")
                return []
    
        except Exception as e:
            self.logger.error(f"Error occurred while crawling peers of instance {instance_url}: {str(e)}")
            return []

    def instance_activity(self, instance_url):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")
        
        try:            
            # Check rate limit for this instance
            remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
            if remaining_requests is not None and remaining_requests < 5:
                wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                if wait_time > 0:
                    self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                    time.sleep(wait_time)
    
            response = requests.get(f"https://{instance_url}/api/v1/instance/activity", timeout=120)
                
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            reset_time_str = response.headers.get('X-RateLimit-Reset')
            reset_time = datetime.fromisoformat(reset_time_str[:-1])
            self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
            if response.status_code == 200:
                self.logger.info(f"Crawled activity of instance {instance_url}.")
                return response.json()
            else:
                self.logger.error(f"Failed to fetch activity of instance {instance_url}. Status code: {response.status_code}")
                return []
    
        except Exception as e:
            self.logger.error(f"Error occurred while crawling activity of instance {instance_url}: {str(e)}")
            return []

    def instance_rules(self, instance_url):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")
        
        try:            
            # Check rate limit for this instance
            remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
            if remaining_requests is not None and remaining_requests < 5:
                wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                if wait_time > 0:
                    self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                    time.sleep(wait_time)
    
            response = requests.get(f"https://{instance_url}/api/v1/instance/rules", timeout=120)
                
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            reset_time_str = response.headers.get('X-RateLimit-Reset')
            reset_time = datetime.fromisoformat(reset_time_str[:-1])
            self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
            if response.status_code == 200:
                self.logger.info(f"Crawled rules of instance {instance_url}.")
                return response.json()
            else:
                self.logger.error(f"Failed to fetch rules of instance {instance_url}. Status code: {response.status_code}")
                return []
    
        except Exception as e:
            self.logger.error(f"Error occurred while crawling rules of instance {instance_url}: {str(e)}")
            return []    

    def instance_blocks(self, instance_url):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")
        
        try:            
            # Check rate limit for this instance
            remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
            if remaining_requests is not None and remaining_requests < 5:
                wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                if wait_time > 0:
                    self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                    time.sleep(wait_time)
    
            response = requests.get(f"https://{instance_url}/api/v1/instance/domain_blocks", timeout=120)
                
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            reset_time_str = response.headers.get('X-RateLimit-Reset')
            reset_time = datetime.fromisoformat(reset_time_str[:-1])
            self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
            if response.status_code == 200:
                self.logger.info(f"Crawled instance(s) blocked by instance {instance_url}.")
                return response.json()
            else:
                self.logger.error(f"Failed to fetch instance(s) blocked by instance {instance_url}. Status code: {response.status_code}")
                return []
    
        except Exception as e:
            self.logger.error(f"Error occurred while crawling instance(s) blocked by instance {instance_url}: {str(e)}")
            return []    

    def instance_trends_all(self, instance_url, trend_type='tags'):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")

        # Check if trend_type is valid
        if trend_type not in ['tags', 'statuses', 'links']:
            raise ValueError("Invalid value for 'trend_type'. It must be 'tags', 'statuses' or 'links'.")
        
        instance_tags = []
        offset = 0
        while True:
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                response = requests.get(f"https://{instance_url}/api/v1/trends/{trend_type}?limit=20&offset={offset}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)

                if response.status_code == 200:
                    tags = response.json()
                    instance_tags.extend(tags)
                    if len(tags) < 20:
                        self.logger.info(f"Crawled {len(instance_tags)} trending {trend_type} from the instance {instance_url}")
                        return instance_tags
                    else:
                        self.logger.info(f"Crawled {len(instance_tags)} trending {trend_type} from the instance {instance_url}")
                        offset += 20
                else:
                    self.logger.error(f"Failed to fetch trending {trend_type} from the instance {instance_url}. Status code: {response.status_code}")
                    return instance_tags

            except Exception as e:
                self.logger.error(f"Error occurred while crawling trending {trend_type} from the instance {instance_url}: {str(e)}")
                return instance_tags    

    def instance_trends(self, instance_url, max_limit, trend_type='tags'):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")

        # Check if max_limit is an integer and positive
        if not isinstance(max_limit, int) or max_limit < 1:
            raise ValueError("Invalid value for 'max_limit'. It must be a positive integer.")

        # Check if trend_type is valid
        if trend_type not in ['tags', 'statuses', 'links']:
            raise ValueError("Invalid value for 'trend_type'. It must be 'tags', 'statuses' or 'links'.")
        
        instance_tags = []
        offset = 0
        items_crawled = 0
        while items_crawled < max_limit:
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                limit = min((max_limit - items_crawled), 20)
                response = requests.get(f"https://{instance_url}/api/v1/trends/{trend_type}?limit={limit}&offset={offset}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)

                if response.status_code == 200:
                    tags = response.json()
                    instance_tags.extend(tags)
                    items_crawled += len(tags)
                    if len(tags) < limit:
                        self.logger.info(f"Crawled {len(instance_tags)} trending {trend_type} from the instance {instance_url}")
                        return instance_tags
                    else:
                        self.logger.info(f"Crawled {len(instance_tags)} trending {trend_type} from the instance {instance_url}")
                        offset += limit
                else:
                    self.logger.error(f"Failed to fetch trending {trend_type} from the instance {instance_url}. Status code: {response.status_code}")
                    return instance_tags

            except Exception as e:
                self.logger.error(f"Error occurred while crawling trending {trend_type} from the instance {instance_url}: {str(e)}")
                return instance_tags
        
        return instance_tags    
                
    def instance_directory_all(self, instance_url, order='active', include_remote=False):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")

        # Check if order is valid
        if order not in ['active', 'new']:
            raise ValueError("Invalid value for 'order'. It must be 'active' or 'new'.")

        # Check if include_remote is a boolean
        if not isinstance(include_remote, bool):
            raise ValueError("Invalid value for 'include_remote'. It must be a boolean.")
        
        local='true'
        if include_remote:
            local='false'
        
        instance_directory = []
        offset = 0
        while True:
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                response = requests.get(f"https://{instance_url}/api/v1/directory?local={local}&order={order}&limit=80&offset={offset}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)

                if response.status_code == 200:
                    users = response.json()
                    instance_directory.extend(users)
                    if len(users) < 80:
                        self.logger.info(f"Crawled {len(instance_directory)} users from the directory of instance {instance_url}")
                        return instance_directory
                    else:
                        self.logger.info(f"Crawled {len(instance_directory)} users from the directory of instance {instance_url}")
                        offset += 80
                else:
                    self.logger.error(f"Failed to fetch directory of instance {instance_url}. Status code: {response.status_code}")
                    return instance_directory

            except Exception as e:
                self.logger.error(f"Error occurred while crawling directory of instance {instance_url}: {str(e)}")
                return instance_directory

    def instance_directory(self, instance_url, max_limit, order='active', include_remote=False):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")

        # Check if max_limit is an integer and positive
        if not isinstance(max_limit, int) or max_limit < 1:
            raise ValueError("Invalid value for 'max_limit'. It must be a positive integer.")
        
        # Check if order is valid
        if order not in ['active', 'new']:
            raise ValueError("Invalid value for 'order'. It must be 'active' or 'new'.")

        # Check if include_remote is a boolean
        if not isinstance(include_remote, bool):
            raise ValueError("Invalid value for 'include_remote'. It must be a boolean.")
        
        local='true'
        if include_remote:
            local='false'
        
        instance_directory = []
        offset = 0
        items_crawled = 0
        while items_crawled < max_limit:
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                limit = min((max_limit - items_crawled), 80)
                response = requests.get(f"https://{instance_url}/api/v1/directory?local={local}&order={order}&limit={limit}&offset={offset}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)

                if response.status_code == 200:
                    users = response.json()
                    instance_directory.extend(users)
                    items_crawled += len(users)
                    if len(users) < limit:
                        self.logger.info(f"Crawled {len(instance_directory)} users from the directory of instance {instance_url}")
                        return instance_directory
                    else:
                        self.logger.info(f"Crawled {len(instance_directory)} users from the directory of instance {instance_url}")
                        offset += limit
                else:
                    self.logger.error(f"Failed to fetch directory of instance {instance_url}. Status code: {response.status_code}")
                    return instance_directory

            except Exception as e:
                self.logger.error(f"Error occurred while crawling directory of instance {instance_url}: {str(e)}")
                return instance_directory
        
        return instance_directory

    def instance_timeline_all(self, instance_url, only_local=False, only_remote=False, only_media=False):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")

        # Check if only_local is a boolean
        if not isinstance(only_local, bool):
            raise ValueError("Invalid value for 'only_local'. It must be a boolean.")

        # Check if only_remote is a boolean
        if not isinstance(only_remote, bool):
            raise ValueError("Invalid value for 'only_remote'. It must be a boolean.")
        
        # Check if only_media is a boolean
        if not isinstance(only_media, bool):
            raise ValueError("Invalid value for 'only_media'. It must be a boolean.")

        # Check if both only_local and only_remote are True
        if only_local and only_remote:
            raise ValueError("only_local and only_remote cannot be True at the same time.")

        only_local = str(only_local).lower()
        only_remote = str(only_remote).lower()
        only_media = str(only_media).lower()
        
        items = []
        url = f"https://{instance_url}/api/v1/timelines/public?local={only_local}&remote={only_remote}&only_media={only_media}&limit=40"

        while True:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)
                
                response = requests.get(url, timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} statuses from timeline of instance {instance_url}")
                    else:
                        self.logger.info(f"Crawled {len(items)} statuses from timeline of instance {instance_url}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch statuses from timeline of instance {instance_url}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling statuses from timeline of instance {instance_url}: {str(e)}")
                return items    

    def instance_timeline(self, instance_url, max_limit, only_local=False, only_remote=False, only_media=False):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")

        # Check if max_limit is an integer and positive
        if not isinstance(max_limit, int) or max_limit < 1:
            raise ValueError("Invalid value for 'max_limit'. It must be a positive integer.")

        # Check if only_local is a boolean
        if not isinstance(only_local, bool):
            raise ValueError("Invalid value for 'only_local'. It must be a boolean.")

        # Check if only_remote is a boolean
        if not isinstance(only_remote, bool):
            raise ValueError("Invalid value for 'only_remote'. It must be a boolean.")
        
        # Check if only_media is a boolean
        if not isinstance(only_media, bool):
            raise ValueError("Invalid value for 'only_media'. It must be a boolean.")

        # Check if both only_local and only_remote are True
        if only_local and only_remote:
            raise ValueError("only_local and only_remote cannot be True at the same time.")

        only_local = str(only_local).lower()
        only_remote = str(only_remote).lower()
        only_media = str(only_media).lower()
        
        items = []
        items_crawled = 0
        url = f"https://{instance_url}/api/v1/timelines/public?local={only_local}&remote={only_remote}&only_media={only_media}"

        while items_crawled < max_limit:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                limit = min((max_limit - items_crawled), 40)
                response = requests.get(f"{url}&limit={limit}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    items_crawled += len(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} statuses from timeline of instance {instance_url}")
                    else:
                        self.logger.info(f"Crawled {len(items)} statuses from timeline of instance {instance_url}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch statuses from timeline of instance {instance_url}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling statuses from timeline of instance {instance_url}: {str(e)}")
                return items
                
        return items
                
    def user_lookup(self, username):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social") 
        
        try:
            instance_url = username.split('@')[1]
            
            # Check rate limit for this instance
            remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
            if remaining_requests is not None and remaining_requests < 5:
                wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                if wait_time > 0:
                    self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                    time.sleep(wait_time)
    
            response = requests.get(f"https://{instance_url}/api/v1/accounts/lookup?acct={username}", timeout=120)
                
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            reset_time_str = response.headers.get('X-RateLimit-Reset')
            reset_time = datetime.fromisoformat(reset_time_str[:-1])
            self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
            if response.status_code == 200:
                self.logger.info(f"Crawled profile of user {username}.")
                return [response.json()]
            else:
                self.logger.error(f"Failed to fetch profile of user {username}. Status code: {response.status_code}")
                return []
    
        except Exception as e:
            self.logger.error(f"Error occurred while crawling profile of user {username}: {str(e)}")
            return []

    def user_statuses_all(self, username, only_media=False, exclude_replies=False, exclude_reblogs=False, only_pinned=False):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social")

        # Check if only_media is a boolean
        if not isinstance(only_media, bool):
            raise ValueError("Invalid value for 'only_media'. It must be a boolean.")
        
        # Check if exclude_replies is a boolean
        if not isinstance(exclude_replies, bool):
            raise ValueError("Invalid value for 'exclude_replies'. It must be a boolean.")
        
        # Check if exclude_reblogs is a boolean
        if not isinstance(exclude_reblogs, bool):
            raise ValueError("Invalid value for 'exclude_reblogs'. It must be a boolean.")
        
        # Check if only_pinned is a boolean
        if not isinstance(only_pinned, bool):
            raise ValueError("Invalid value for 'only_pinned'. It must be a boolean.")

        only_media = str(only_media).lower()
        exclude_replies = str(exclude_replies).lower()
        exclude_reblogs = str(exclude_reblogs).lower()
        only_pinned = str(only_pinned).lower()
        
        user_profile = self.user_lookup(username)

        user_id = None

        if len(user_profile) > 0:
            user_id = user_profile[0]['id']
        else:
            return []

        instance_url = username.split('@')[1]
        
        items = []
        url = f"https://{instance_url}/api/v1/accounts/{user_id}/statuses?only_media={only_media}&exclude_replies={exclude_replies}&exclude_reblogs={exclude_reblogs}&pinned={only_pinned}&limit=40"

        while True:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)
                
                response = requests.get(url, timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} statuses of user {username}")
                    else:
                        self.logger.info(f"Crawled {len(items)} statuses of user {username}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch statuses of user {username}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling statuses of user {username}: {str(e)}")
                return items

    def user_statuses(self, username, max_limit, only_media=False, exclude_replies=False, exclude_reblogs=False, only_pinned=False):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social")

        # Check if max_limit is an integer and positive
        if not isinstance(max_limit, int) or max_limit < 1:
            raise ValueError("Invalid value for 'max_limit'. It must be a positive integer.")

        # Check if only_media is a boolean
        if not isinstance(only_media, bool):
            raise ValueError("Invalid value for 'only_media'. It must be a boolean.")
        
        # Check if exclude_replies is a boolean
        if not isinstance(exclude_replies, bool):
            raise ValueError("Invalid value for 'exclude_replies'. It must be a boolean.")
        
        # Check if exclude_reblogs is a boolean
        if not isinstance(exclude_reblogs, bool):
            raise ValueError("Invalid value for 'exclude_reblogs'. It must be a boolean.")
        
        # Check if only_pinned is a boolean
        if not isinstance(only_pinned, bool):
            raise ValueError("Invalid value for 'only_pinned'. It must be a boolean.")

        only_media = str(only_media).lower()
        exclude_replies = str(exclude_replies).lower()
        exclude_reblogs = str(exclude_reblogs).lower()
        only_pinned = str(only_pinned).lower()
        
        user_profile = self.user_lookup(username)

        user_id = None

        if len(user_profile) > 0:
            user_id = user_profile[0]['id']
        else:
            return []

        instance_url = username.split('@')[1]
        
        items = []
        items_crawled = 0
        url = f"https://{instance_url}/api/v1/accounts/{user_id}/statuses?only_media={only_media}&exclude_replies={exclude_replies}&exclude_reblogs={exclude_reblogs}&pinned={only_pinned}"

        while items_crawled < max_limit:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                limit = min((max_limit - items_crawled), 40)
                response = requests.get(f"{url}&limit={limit}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    items_crawled += len(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} statuses of user {username}")
                    else:
                        self.logger.info(f"Crawled {len(items)} statuses of user {username}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch statuses of user {username}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling statuses of user {username}: {str(e)}")
                return items
                
        return items

    def user_followers_all(self, username):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social")
        
        user_profile = self.user_lookup(username)

        user_id = None

        if len(user_profile) > 0:
            user_id = user_profile[0]['id']
        else:
            return []

        instance_url = username.split('@')[1]
        
        items = []
        url = f"https://{instance_url}/api/v1/accounts/{user_id}/followers?limit=80"

        while True:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)
                
                response = requests.get(url, timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} followers of user {username}")
                    else:
                        self.logger.info(f"Crawled {len(items)} followers of user {username}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch followers of user {username}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling followers of user {username}: {str(e)}")
                return items

    def user_followers(self, username, max_limit):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social")

        # Check if max_limit is an integer and positive
        if not isinstance(max_limit, int) or max_limit < 1:
            raise ValueError("Invalid value for 'max_limit'. It must be a positive integer.")
        
        user_profile = self.user_lookup(username)

        user_id = None

        if len(user_profile) > 0:
            user_id = user_profile[0]['id']
        else:
            return []

        instance_url = username.split('@')[1]
        
        items = []
        items_crawled = 0
        url = f"https://{instance_url}/api/v1/accounts/{user_id}/followers?"

        while items_crawled < max_limit:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                limit = min((max_limit - items_crawled), 80)
                response = requests.get(f"{url}&limit={limit}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    items_crawled += len(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} followers of user {username}")
                    else:
                        self.logger.info(f"Crawled {len(items)} followers of user {username}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch followers of user {username}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling followers of user {username}: {str(e)}")
                return items
                
        return items

    def user_following_all(self, username):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social")
        
        user_profile = self.user_lookup(username)

        user_id = None

        if len(user_profile) > 0:
            user_id = user_profile[0]['id']
        else:
            return []

        instance_url = username.split('@')[1]
        
        items = []
        url = f"https://{instance_url}/api/v1/accounts/{user_id}/following?limit=80"

        while True:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)
                
                response = requests.get(url, timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} followees of user {username}")
                    else:
                        self.logger.info(f"Crawled {len(items)} followees of user {username}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch followees of user {username}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling followees of user {username}: {str(e)}")
                return items

    def user_following(self, username, max_limit):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social")

        # Check if max_limit is an integer and positive
        if not isinstance(max_limit, int) or max_limit < 1:
            raise ValueError("Invalid value for 'max_limit'. It must be a positive integer.")
        
        user_profile = self.user_lookup(username)

        user_id = None

        if len(user_profile) > 0:
            user_id = user_profile[0]['id']
        else:
            return []

        instance_url = username.split('@')[1]
        
        items = []
        items_crawled = 0
        url = f"https://{instance_url}/api/v1/accounts/{user_id}/following?"

        while items_crawled < max_limit:      
            try:
                # Check rate limit for this instance
                remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
                if remaining_requests is not None and remaining_requests < 5:
                    wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                    if wait_time > 0:
                        self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                        time.sleep(wait_time)

                limit = min((max_limit - items_crawled), 80)
                response = requests.get(f"{url}&limit={limit}", timeout=120)
                
                remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
                reset_time_str = response.headers.get('X-RateLimit-Reset')
                reset_time = datetime.fromisoformat(reset_time_str[:-1])
                self.rate_limits[instance_url] = (remaining_requests, reset_time)
    
                if response.status_code == 200:
                    items.extend(response.json())
                    items_crawled += len(response.json())
                    if 'next' in response.links:
                        url = response.links['next']['url']
                        self.logger.info(f"Crawled {len(items)} followees of user {username}")
                    else:
                        self.logger.info(f"Crawled {len(items)} followees of user {username}")
                        return items
                else:
                    self.logger.error(f"Failed to fetch followees of user {username}. Status code: {response.status_code}")
                    return items
    
            except Exception as e:
                self.logger.error(f"Error occurred while crawling followees of user {username}: {str(e)}")
                return items
                
        return items
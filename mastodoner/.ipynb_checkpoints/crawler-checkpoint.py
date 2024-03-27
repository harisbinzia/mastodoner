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

    def local_instance_directory_all(self, instance_url):
            
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

                response = requests.get(f"https://{instance_url}/api/v1/directory?local=true&order=active&limit=80&offset={offset}", timeout=120)
                
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

    def local_instance_directory(self, instance_url, order='active', limit=40, offset=0):

        # Check if instance_url is a string
        if not isinstance(instance_url, str):
            raise ValueError("Invalid value for 'instance_url'. It must be a string.")

         # Check if order is valid
        if order not in ['active', 'new']:
            raise ValueError("Invalid value for 'order'. It must be 'active' or 'new'.")
        
        # Check if limit is an integer within valid range
        if not isinstance(limit, int) or not 1 <= limit <= 80:
            raise ValueError("Invalid value for 'limit'. It must be an integer between 1 and 80.")
        
        # Check if offset is an integer and non-negative
        if not isinstance(offset, int) or offset < 0:
            raise ValueError("Invalid value for 'offset'. It must be a non-negative integer.")
        
        instance_directory = []
        try:
            # Check rate limit for this instance
            remaining_requests, reset_time = self.rate_limits.get(instance_url, (None, None))
            if remaining_requests is not None and remaining_requests < 5:
                wait_time = (reset_time - datetime.utcnow()).total_seconds() + 1
                if wait_time > 0:
                    self.logger.info(f"Waiting for {wait_time} seconds to reset rate limit for instance {instance_url}")
                    time.sleep(wait_time)

            response = requests.get(f"https://{instance_url}/api/v1/directory?local=true&order={order}&limit={limit}&offset={offset}", timeout=120)
                
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            reset_time_str = response.headers.get('X-RateLimit-Reset')
            reset_time = datetime.fromisoformat(reset_time_str[:-1])
            self.rate_limits[instance_url] = (remaining_requests, reset_time)

            if response.status_code == 200:
                users = response.json()
                instance_directory.extend(users)
                self.logger.info(f"Crawled {len(instance_directory)} users from the directory of instance {instance_url}")
                return instance_directory
            else:
                self.logger.error(f"Failed to fetch directory of instance {instance_url}. Status code: {response.status_code}")
                return instance_directory

        except Exception as e:
            self.logger.error(f"Error occurred while crawling directory of instance {instance_url}: {str(e)}")
            return instance_directory

    def user_lookup(self, username):

        # Check if username is a string
        if not isinstance(username, str):
            raise ValueError("Invalid value for 'username'. It must be a string.")
        
        # Check if username follows the format 'user@domain'
        if '@' not in username or username.count('@') != 1:
            raise ValueError("Invalid format for 'username'. It must be in the format 'user@domain' e.g. ignactro@mastodon.social")
        
        instance_url = username.split('@')[1]
        
        try:
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

import time
from selenium.webdriver.common.by import By
import random 
import os 
from PageHandler.Helper import PATH_MANAGER, NoCredentialsError
from difflib import SequenceMatcher


class DriverNavigator(): 
    def __init__(self, driver, stack, require_login) -> None:
        self.require_login = require_login
        self.driver = driver
        self.url_handlers = {}
        self.stack = stack
        self.fail_url = []
        self.login_url = "https://leetcode.com/accounts/login/"

    def add_url_handlers(self, url, handler): 
        self.url_handlers[url] = handler

    def process_page(self): 
        url = self.driver.current_url
        for i in self.url_handlers: 
            if i in url: 
                handler = self.url_handlers[i]
                try: 
                    handler.process_page()
                    self.handle_success(handler, url)
                    return 
                except NoCredentialsError: 
                    url = self.stack.pop()
                    print(url + " require login but no credetials passed")
                    return 
                except Exception as e: 
                    print(url, e)
                    self.handle_fail(url)
                    return 
        print("invalid url")
        self.stack.pop()


    def handle_success(self, handler, url): 
        if(is_same_link(url1=url, url2=self.stack[-1])): 
            self.stack.pop()
            handler.log_data()

    def handle_fail(self, url):
        self.fail_url.append(url)
        if(is_same_link(url1=url, url2=self.stack[-1])): 
            self.stack.pop()

    def need_to_relogin(self): 
        is_logged_out = self.driver.find_elements(By.ID, "navbar_sign_in_button") 
        login_url_is_not_queued = self.login_url not in self.driver.current_url 
        is_need_to_authenticate = self.require_login
        return is_logged_out and login_url_is_not_queued and is_need_to_authenticate


    def run(self): 
        while len(self.stack) > 0: 
            print("Queue: " + str(len(self.stack)))
            self.driver.get(self.stack[-1])
            if (self.need_to_relogin()):
                self.stack.append(self.login_url)
                continue
            time.sleep(random.randint(1,5))
            self.process_page()
        self.log_failed_urls()
            
    def log_failed_urls(self): 
        if(len(self.fail_url) ==0):
            return 
        with open(os.path.join(PATH_MANAGER.target_path, 'fail_urls.txt'), 'w') as f:
            for line in self.fail_url:
                f.write(f"{line}\n")


def is_same_link(url1, url2): 
    return SequenceMatcher(None, url1, url2).ratio() > 0.9

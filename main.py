import argparse
from DriverNavigator import DriverNavigator
from selenium import webdriver
from PageHandler.CompanyProblemPageHandler import CompanyProblemPageHandler
from PageHandler.MainTableHandler import MainTableHandler
from PageHandler.LoginPageHandler import LoginPageHandler
from PageHandler.ProblemPageHandler import ProblemPageHandler
import sys
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse 

def read_from_file(path, target_stack): 
    with open(path, "r") as f: 
        for i in f.readlines(): 
            target_stack.append(i)
    
def get_driver(): 
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/60.0.3112.50 Safari/537.36"
    options = Options()
    options.add_argument(f'user-agent={user_agent}')
    # options.headless = True 
    driver = webdriver.Chrome(options= options)
    return driver

def run_scrapper(stack, username = "" , password = "", require_login = False):
    driver = get_driver()
    navigator = DriverNavigator(driver=driver, stack = stack, require_login = require_login)
    navigator.add_url_handlers("https://leetcode.com/problemset/all/", MainTableHandler(driver))
    navigator.add_url_handlers("https://leetcode.com/problem-list/", MainTableHandler(driver))
    navigator.add_url_handlers("https://leetcode.com/company/", CompanyProblemPageHandler(driver))
    navigator.add_url_handlers("https://leetcode.com/accounts/login/", LoginPageHandler(driver, username , password))
    navigator.add_url_handlers("https://leetcode.com/subscribe/", LoginPageHandler(driver, username , password))
    navigator.add_url_handlers("https://leetcode.com/problems/",ProblemPageHandler(driver))
    navigator.run()     

if __name__ == "__main__": 
    stack = []
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    parser.add_argument("run", nargs= '*')
    args  = parser.parse_args()
    
    if args.username == None and args.password != None or args.username != None and args.password == None : 
        print('Username or password missing')
        sys.exit()
    
    for i in args.run: 
        if ".txt" in i: 
            read_from_file(i, stack)
        else: 
            stack.append(i)
            
    credential_is_passed = (args.username != None)
    print("Running Scrapper")
    run_scrapper(stack= stack, username=args.username, password= args.password, require_login = credential_is_passed)
    
    
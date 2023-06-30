  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from PageHandler.Helper import NoCredentialsError
from urllib.parse import urlparse
from PageHandler.Helper import log_data
from selenium.common.exceptions import NoSuchElementException


class StudyPlanPageHandler(): 
    def __init__(self, driver) -> None:
        self.driver = driver
        self.data = {}

    
    def log_data(self): 
        url_data = urlparse(self.driver.current_url)
        folder_name = url_data.path.split("/")[1]
        file_name = url_data.path.split("/")[2]
        self.data["studyPlan"] = file_name
        log_data(self.data, folder_name=folder_name, file_name=file_name)

    def process_page(self): 
        self.check_page()
        if self.username == "" or self.username == None: 
            raise NoCredentialsError(self.driver.current_url)
        self.data = self.get_study_plan_data()

    def check_page(self): 
        WebDriverWait(self.driver, timeout=100).until(lambda d: d.find_element(By.CLASS_NAME,"css-yw0m6t"))

    def get_study_plan_data(self): 
        sections = self.driver.find_elements(By.CLASS_NAME, "css-yw0m6t")
        data = {}
        for i in sections: 
            title = i.find_element(By.CLASS_NAME, "text-lc-text-primary").text
            problems = i.find_elements(By.CLASS_NAME, "truncate")
            problem_data = []
            for problem in problems: 
                problem_data.append(problem.text)
            data[title] = problem_data
        return data



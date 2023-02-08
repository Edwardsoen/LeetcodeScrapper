from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from PageHandler.Helper import log_data
from urllib.parse import urlparse
import re

class MainTableHandler(): 
    def __init__(self, driver) -> None:
        self.driver = driver
        self.data = {}

    def check_page(self): 
        WebDriverWait(self.driver, timeout=100).until(lambda d: d.find_element(By.CSS_SELECTOR,"div[role='rowgroup']"))

    def log_data(self): 
        url_data = urlparse(self.driver.current_url)
        file_name = url_data.query 
        file_name = re.sub(r'[^\w]', ' ', file_name)
        self.data["page"] = file_name.split(" ")[-1]
        folder_name = url_data.path.split("/")[1]
        log_data(self.data, folder_name=folder_name, file_name=file_name)

    def process_page(self): 
        self.check_page()
        time.sleep(1)
        table = self.driver.find_elements(by = By.CSS_SELECTOR, value = "div[role='rowgroup']")[0]
        rows = table.find_elements(by = By.CSS_SELECTOR, value = "div[role='row']")
        complete_data = []
        for i in rows: 
            row_data = self.get_row_data(i)
            complete_data.append(row_data)
        self.data["tableData"] = complete_data

    def get_current_page(self): 
        return self.driver.current_url.split("=")[-1]

    def get_row_data(self, row): 
        cells = row.find_elements(by = By.CSS_SELECTOR, value = "div[role='cell']")
        is_premium = (cells[0].find_elements(by = By.CLASS_NAME, value = "text-brand-orange") or None) != None
        problem_name = cells[1].text
        have_solution = len(cells[2].find_elements(by = By.TAG_NAME, value = "svg")) != 0 
        solution_is_premium = len(cells[2].find_elements(by = By.CLASS_NAME, value = "text-purple")) != 0 
        acceptence = cells[3].text
        difficulty = cells[4].text
        frequency = None
        if (cells[-1].find_elements(by = By.CLASS_NAME, value = "bg-brand-orange") or None != None): 
            frequency =  str(cells[-1].find_element(by = By.CLASS_NAME, value = "bg-brand-orange").get_attribute('style')).split(": ")[-1].replace(";", "")
        url = cells[1].find_element(by = By.TAG_NAME, value = "a").get_attribute('href')
        row_data = {
            "isPremium": is_premium, 
            "problemName": problem_name,
            "haveSolution": have_solution, 
            "isVideoSolution":solution_is_premium, 
            "acceptance":acceptence, 
            "difficulty": difficulty, 
            "frequency":frequency, 
            "url":url
        }
        return row_data


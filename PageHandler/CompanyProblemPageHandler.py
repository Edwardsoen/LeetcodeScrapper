
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from  urllib.parse import urlparse
from PageHandler.Helper import log_data


class CompanyProblemPageHandler(): 
    def __init__(self, driver) -> None:
        self.driver = driver
        self.problem_lists = []
        self.data = {}
        
    def clear_data(self): 
        self.problem_lists = []
        self.data = {}

    def log_data(self):
        url_data = urlparse(self.driver.current_url)
        folder_name = url_data.path.split("/")[1]
        file_name = url_data.path.split("/")[2]
        self.data["companyName"] = file_name.split()
        log_data(self.data, folder_name=folder_name, file_name= file_name)

    def process_page(self): 
        self.clear_data()
        WebDriverWait(self.driver, timeout=100).until(lambda d: d.find_element(By.ID,"react-select-2--value-item"))
        options_id = ['0', '1', '2', '3']
        for option_id in options_id: 
            option_element_name =  "react-select-2--option-" + option_id
            self.click_drop_down()
            time.sleep(1)
            if(self.is_option_exist(option_element_name)): 
                self.driver.find_element(By.ID, option_element_name).click()
                time.sleep(1)
                data = self.get_table_data(duration=self.get_duration())
                self.problem_lists.append(data)
                breakpoint()
        self.data["data"] = self.problem_lists
                            
    def click_drop_down(self): 
        time_drop_down = self.driver.find_element(By.ID, "react-select-2--value-item")
        time_drop_down.click()
        time.sleep(0.5) 
        return time_drop_down.text

    def get_duration(self): 
        return self.driver.find_element(By.ID, "react-select-2--value-item").text

    def is_option_exist(self, element_id): 
        if len(self.driver.find_elements(By.ID, element_id)) == 0: 
            self.click_drop_down()
            return False
        return True

    def get_table_data(self, duration):
        script = '''
        const rows = document.getElementsByClassName('reactable-data')[0].children;
        const problems = [];
        for (const row of rows) {
            const problem = {}
            const cols = row.children;
            const tags = Array.from(cols[3].querySelectorAll('a')).map(t => t.innerText.trim()).join(', ');
            const frequency = parseFloat(row.getElementsByClassName('progress-bar')[0].style.width);
            const link = cols[2].querySelector('a').href;
            problem["problemId"] = cols[1].innerText.trim()
            problem["problemName"] = cols[2].innerText.trim()
            problem["acceptance"] = cols[3].innerText.trim()
            problem["difficulty"] = cols[4].innerText.trim()
            problem["frequency"] = frequency
            problem["url"] = link
            problems.push(problem)
        }
        return problems
        '''
        companyProblemsData = self.driver.execute_script(script)
        data ={"duration": duration, "problemData":companyProblemsData }
        return data
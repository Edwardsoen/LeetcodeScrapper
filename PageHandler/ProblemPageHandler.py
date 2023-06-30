from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from PageHandler.Helper import log_data, NoCredentialsError
from urllib.parse import urlparse
from selenium.common.exceptions import NoSuchElementException

class ProblemPageHandler(): 
    def __init__(self, driver) -> None:
        self.driver = driver
        self.data = {"tags":[], "problem": ""}

    def remove_on_focus_listener(self):
        script = '''
            Object.defineProperty(window.document,'hidden',{get:function(){return false;},configurable:true});
    Object.defineProperty(window.document,'visibilityState',{get:function(){return 'visible';},configurable:true});
    window.document.dispatchEvent(new Event('visibilitychange'));
''' 
        self.driver.execute_script(script)

    def get_problem_innerHTML(self): 
        return self.driver.find_element(By.CLASS_NAME, "_1l1MA").get_attribute('innerHTML')

    def get_tags_bar(self):
        left_section = self.driver.find_elements(By.CLASS_NAME,"ssg__qd-splitter-primary-h")[0]
        flex_wrap = left_section.find_elements(By.CLASS_NAME, "flex-wrap")
        if(len(flex_wrap) <= 1): 
            return None 
        return flex_wrap[0] 

    def check_page(self): 
        try: 
            WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.ID,"qd-content"))
        except Exception as e: 
            if self.switch_to_new_version() == False: 
                raise e

    def get_similar_questions(self): 
        try: 
            similar_question_tab = self.driver.find_elements(By.CLASS_NAME, "translate-y-0")[0]
            questions = similar_question_tab.find_elements(By.CLASS_NAME, "w-full")
            data = []
            for question in questions: 
                question_name = question.find_elements(By.TAG_NAME, "a")[0].text
                difficulty = question.find_elements(By.CLASS_NAME, "text-xs")[0].text
                question_data = {"questionName": question_name, "difficulty": difficulty}
                data.append(question_data)
            return data 
        except Exception as e: 
            return []

    def open_all_lower_tab(self): 
        tabs = self.driver.find_elements(By.CLASS_NAME, "py-3")
        for tab in tabs: 
            pointers = tab.find_elements(By.CLASS_NAME, "cursor-pointer")
            if len(pointers) != 0: 
                pointers[0].click()
        time.sleep(1.5)

            
    def get_related_topics(self): 
        try: 
            related_topic_tab = self.driver.find_elements(By.CLASS_NAME, "translate-y-0")[1]
            data = []
            tags = related_topic_tab.find_elements(By.TAG_NAME, "a")
            for tag in tags: 
                data.append(tag.text)
            return data 
        except Exception as e:
            return []
            

    def require_subscription(self): 
        return len(self.driver.find_elements(By.CLASS_NAME, "text-2xl")) > 0

    def switch_to_new_version(self):
        new_btn = self.driver.find_elements(By.CLASS_NAME, "css-ly0btt-NewDiv")
        if len(new_btn) >0: 
            new_btn[0].click()
            return True
        return False


    def get_companies_tags(self): 
        try: 
            tags_bar = self.get_tags_bar()
            if tags_bar == None:
                return 
            tags_bar.find_elements(By.CLASS_NAME, "cursor-pointer")[-1].click()
            WebDriverWait(self.driver, timeout=5).until(lambda d: d.find_element(By.CSS_SELECTOR,"div[role='dialog']"))
            dialog = self.driver.find_element(By.CSS_SELECTOR,"div[role='dialog']")
            tag_data = self.get_tag_data(dialog=dialog)
            return tag_data
        except Exception as e: 
            return []
        

    def process_page(self):
        self.check_page()
        self.remove_on_focus_listener()
        time.sleep(2)
        if self.require_subscription(): 
            raise NoCredentialsError(self.driver.current_url)
        self.open_all_lower_tab()
        self.data["relatedTopics"] = self.get_related_topics()
        self.data["similarQuestions"] = self.get_similar_questions()
        self.data["problem"] = self.get_problem_innerHTML()
        self.data["tags"] = self.get_companies_tags()   
        self.data["editorial"] = self. get_editorial()
        
    def get_editorial(self): 
        self.driver.get(self.driver.current_url + "editorial")
        time.sleep(2)
        return self.driver.find_element(By.CLASS_NAME, "break-words").get_attribute('innerHTML')



    def get_tag_data(self, dialog): 
        buttons = dialog.find_element(By.CLASS_NAME, "space-x-9").find_elements(By.CLASS_NAME, "cursor-pointer")
        tag_data = []
        for button in buttons: 
            button.click()
            time.sleep(2)
            duration = button.text
            companies = []
            datas = dialog.find_elements(By.CLASS_NAME, "mt-3")
            for data in datas: 
                text = data.text
                companies.append([duration, text])
            tag_data.append({"duration": duration, "companies": companies})
        return tag_data

    def log_data(self): 
        url_data = urlparse(self.driver.current_url)
        folder_name = url_data.path.split("/")[1]
        file_name = url_data.path.split("/")[2]
        self.data["problemName"] = file_name
        log_data(self.data, folder_name=folder_name, file_name=file_name)


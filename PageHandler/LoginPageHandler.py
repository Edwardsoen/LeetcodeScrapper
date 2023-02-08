  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from PageHandler.Helper import NoCredentialsError
from selenium.common.exceptions import NoSuchElementException

class LoginPageHandler(): 
    def __init__(self, driver , username, password) -> None:
        self.driver = driver
        self.username = username
        self.password = password
    
    def log_data(self): 
        pass
    
    def is_capcha_required(self): 
        iframes = self.driver.find_elements(By.CSS_SELECTOR,"iframe")
        if len(iframes) ==4: 
            print("Captcha required, press any key after solving captcha")
            self.driver.maximize_window()
            input()
            self.try_click_login_btn()


    def check_page(self): 
        WebDriverWait(self.driver, timeout=100).until(lambda d: d.find_element(By.ID,"id_login"))

    def try_click_login_btn(self): 
        try: 
             self.driver.find_element(By.CLASS_NAME, "btn-content__2V4r").click()
        except NoSuchElementException: 
            pass

    def process_page(self):
        self.check_page()
        if self.username == "" or self.username == None: 
            raise NoCredentialsError(self.driver.current_url)
        time.sleep(1)
        self.driver.find_element(by = By.ID, value = "id_login").send_keys(self.username)
        self.driver.find_element(by = By.ID, value = "id_password").send_keys(self.password)
        self.try_click_login_btn()
        time.sleep(3)
        self.is_capcha_required()


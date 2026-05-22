from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@type='submit']")
        self.dashboard = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, user, pwd):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username)
        ).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.dashboard)
            )
            return True
        except:
            return False

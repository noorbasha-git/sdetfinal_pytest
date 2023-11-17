import pytest
from selenium.webdriver.common.by import By


class Signin:

    def __init__(self,driver):
        self.driver=driver
    def sign(self):
        self.driver.get('https://saucedemo.com')
        self.driver.find_element(By.ID, "user-name").send_keys('standard_user')
        self.driver.find_element(By.ID, "password").send_keys('secret_sauce')
        self.driver.find_element(By.ID, "login-button").click()



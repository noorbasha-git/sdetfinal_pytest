import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from porta.signin import Signin


@pytest.fixture(scope='module')
def driver():
    drive=webdriver.Edge()
    return drive
@pytest.mark.usefixtures('driver')
class TestLogin:
    def test_title(self,driver):
        s=Signin(driver)
        s.sign()

        text = driver.find_element(By.CLASS_NAME, 'app_logo').text
        print(text)
        assert text == 'Swag Labs'

    def test_addcart(self, driver):

        driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        cnt = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        print(cnt)
        assert cnt == '1'
        driver.find_element(By.ID, 'react-burger-menu-btn').click()
        print("clicking on menu")
        time.sleep(2)
        driver.find_element(By.ID, 'logout_sidebar_link').click()
        print("clicking on logout")
        driver.quit()
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginpage import LoginPage

class Test_001_Login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

    def test_login_valid(self):
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()

        page_title = self.driver.find_element(By.CLASS_NAME, "app_logo").text
        if page_title != "Swag Labs":  # check if it matches
            self.driver.save_screenshot(f"screenshots/error_{time.time()}.png")  # take screenshot
            assert False, f"Expected 'Swag Labs' but got '{page_title}'"

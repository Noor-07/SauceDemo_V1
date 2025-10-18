from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


class LoginPage:
    inputbox_username_id = "user-name"
    inputbox_password_id = "password"
    btn_login_name = "login-button"
    error_message_xpath = "//h3[@data-test='error']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.inputbox_username_id).send_keys (username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.inputbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.btn_login_name).click()

    def get_errorMessage(self):
       return self.driver.find_element(By.XPATH, self.error_message_xpath).text



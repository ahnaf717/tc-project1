from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class loginPage:
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_box(self):
        element: WebElement = self.driver.find_element(By.ID, "Username")
        return element

    def select_password_box(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def select_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "ebutton")
        return element


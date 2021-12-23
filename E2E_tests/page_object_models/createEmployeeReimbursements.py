from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class createReimbursements:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username(self):
        element: WebElement = self.driver.find_element(By.ID, "Username")
        return element

    def select_password(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def select_loginbutton(self):
        element: WebElement = self.driver.find_element(By.ID, "ebutton")
        return element


    def select_reimbursement_code(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementCode")
        return element

    def select_reimbursement_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementAmount")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, '/html/body/div/form/button')
        return element


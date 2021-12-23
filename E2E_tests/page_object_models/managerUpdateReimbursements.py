from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class updateReimbursements:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_reimbursement_id(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementID")
        return element

    def select_reimbursement_status(self):
        element: WebElement = self.driver.find_element(By.ID, "status")
        return element

    def select_reimbursement_comments(self):
        element: WebElement = self.driver.find_element(By.ID, "managercomments")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, '/html/body/div[2]/form/button')
        return element

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class decisionReimbursements:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def select_decision_button(self):
        element: WebElement = self.driver.find_element(By.ID, "decisionbutton")
        return element
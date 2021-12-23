from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class pendingReimbursements:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def select_pending_button(self):
        element: WebElement = self.driver.find_element(By.ID, "pendingbutton")
        return element
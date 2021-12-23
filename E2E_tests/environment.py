from behave.runner import Context
from selenium import webdriver

from E2E_tests.page_object_models.createEmployeeReimbursements import createReimbursements
from E2E_tests.page_object_models.employeeViewReimbursements import employeeReimbursements
from E2E_tests.page_object_models.loginpage import loginPage
from E2E_tests.page_object_models.managerDecisionsReimbursement import decisionReimbursements
from E2E_tests.page_object_models.managerLogin import managerLoginPage
from E2E_tests.page_object_models.managerNewReimbursements import addressReimbursements
from E2E_tests.page_object_models.managerUpdateReimbursements import updateReimbursements
from E2E_tests.page_object_models.managerPendingReimbursements import pendingReimbursements


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.loginpage = loginPage(context.driver)
    context.pReimbursement=pendingReimbursements(context.driver)
    context.dReimbursement=decisionReimbursements(context.driver)
    context.aReimbursement=addressReimbursements(context.driver)
    context.mloginpage=managerLoginPage(context.driver)
    context.uReimbursement=updateReimbursements(context.driver)
    context.eReimbursement=employeeReimbursements(context.driver)
    context.cReimbursement=createReimbursements(context.driver)


def after_all(context:Context):
    context.driver.quit()



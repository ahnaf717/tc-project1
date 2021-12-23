from behave import Given, When, Then
from selenium.webdriver.common.alert import Alert
import time


@Given(u'The manager is on the Manager Dashboard Page')
def step_impl(context):
   
    context.driver.get("http://127.0.0.1:5500/Mdashboard.html")


@When(u'The manager fills out the reimbursement ID section {value}')
def step_impl(context,value):
    time.sleep(3)
    context.uReimbursement.select_reimbursement_id().send_keys(value)

@When(u'The manager fills out the reimbursement status sectionApproved')
def step_impl(context):
    time.sleep(3)
    context.uReimbursement.select_reimbursement_status().send_keys("Approved")
    

@When(u'The manager fills out the manager comments sectionApproved')
def step_impl(context):
    time.sleep(2)
    context.uReimbursement.select_reimbursement_comments().send_keys("Approved")


"""
@When(u'The manager fills out the reimbursement status section {value1}')
def step_impl(context,value1):
    time.sleep(5)
    context.uReimbursement.select_reimbursement_status().send_keys(value1)
    


@When(u'The manager fills out the manager comments section {value2}')
def step_impl(context,value2):
    time.sleep(2)
    context.uReimbursement.select_reimbursement_comments().send_keys(value2)
"""

@When(u'The manager clicks on the submit request button')
def step_impl(context):
    time.sleep(1)
    context.uReimbursement.select_submit_button().click()


@Then(u'The reimbursement request should be updated successfully')
def step_impl(context):
    alert = Alert(context.driver)
    time.sleep(4)
    assert alert.text == "Request Has Been Updated Successfully"



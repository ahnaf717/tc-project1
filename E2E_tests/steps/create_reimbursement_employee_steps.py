from behave import Given,When,Then
import time

from selenium.webdriver.common.alert import Alert


@Given(u'The Employee is attempting to login on the login page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/index.html")


@When(u'The employee fills in his username {value}')
def step_impl(context,value):
    context.cReimbursement.select_username().send_keys(value)
   


@When(u'The employee fills in his password {value1}')
def step_impl(context,value1):
    time.sleep(2)
    context.cReimbursement.select_password().send_keys(value1)


@When(u'The Employee clicks on login')
def step_impl(context):
    context.cReimbursement.select_loginbutton().click()


@When(u'The employee fills in the desired reimbursement code {value2} on the employee dashboard page')
def step_impl(context,value2):
    time.sleep(2)
    context.cReimbursement.select_reimbursement_code().send_keys(value2)


@When(u'The employee fills in the desired reimbursement amount {value3}')
def step_impl(context,value3):
    context.cReimbursement.select_reimbursement_amount().send_keys(value3)


@When(u'The employee clicks on the submit request button')
def step_impl(context):
    time.sleep(1)
    context.cReimbursement.select_submit_button().click()


@Then(u'The employee will be able to submit a reimbursement request')
def step_impl(context):
    alert = Alert(context.driver)
    time.sleep(4)
    assert alert.text == "Request Has Been Submitted Successfully"
    

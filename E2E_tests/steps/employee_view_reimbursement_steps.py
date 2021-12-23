from behave import Given, When, Then
import time

@Given(u'The Employee logs into the employee page successfully')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/index.html")


@When(u'The employee fills out his username ahnaf')
def step_impl(context):
    context.eReimbursement.select_username().send_keys("ahnaf")


@When(u'The employee fills out his passwordtahmid')
def step_impl(context):
    context.eReimbursement.select_password().send_keys("tahmid")
   
@When(u'Employee selects the login in button')
def step_impl(context):
    time.sleep(2)
    context.eReimbursement.select_loginbutton().click()


@When(u'The employee clicks the view reimbursement button on the employee dashboard page')
def step_impl(context):
    time.sleep(4)
    context.eReimbursement.select_reimbursement_button().click()


@Then(u'The employee should see his reimbursement requests')
def step_impl(context):
    title = context.driver.title
    time.sleep(2)
    assert title == "Dashboard"

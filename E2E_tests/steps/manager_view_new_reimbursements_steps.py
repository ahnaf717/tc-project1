from behave import Given,When,Then
import time

@Given(u'Manager is on the Manager Reimbursement Dashboard Page.')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/Mdashboard.html")


@When(u'The Manager clicks on the Your New  Reimbursement Requests Button')
def step_impl(context):
    context.aReimbursement.select_new_button().click()


@Then(u'The Manage should be able to view reimbursement requests on the manager dashboard page')
def step_impl(context):
    title = context.driver.title
    time.sleep(1)
    assert title == "Manager Dashboard"







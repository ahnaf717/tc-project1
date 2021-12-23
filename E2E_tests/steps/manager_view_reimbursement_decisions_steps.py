from behave import Given, When, Then
import time


@Given(u'The Manager is on the Manager Reimbursement Dashboard Page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/Mdashboard.html")


@When(u'The Manager clicks on the View Your Past Reimbursement Decisions Button')
def step_impl(context):
    context.dReimbursement.select_decision_button().click()


@Then(u'The Manage should be able to view his past reimbursement decisions for the reimbursement requests on the directed webpage')
def step_impl(context):
    title = context.driver.title
    time.sleep(1)
    assert title == "Your Reimbursement Decisions"
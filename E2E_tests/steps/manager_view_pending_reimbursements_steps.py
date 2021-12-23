from behave import Given,When,Then
import time
@Given(u'The Manager is on the Manager Dashboard Page.')
def step_impl(context):
        context.driver.get("http://127.0.0.1:5500/Mdashboard.html")


@When(u'The Manager clicks on the View Your Pending Reimbursements Button.')
def step_impl(context):
    context.pReimbursement.select_pending_button().click()


@Then(u'The Manage should be able to view his pending reimbursement requests.')
def step_impl(context):
    title = context.driver.title
    time.sleep(1)
    assert title == "Your Pending Reimbursements"


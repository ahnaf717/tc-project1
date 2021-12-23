from behave import Given,When,Then
import time

@Given(u'The Manager is on the login page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/index.html")


@When(u'The Manager enters their username {value}')
def step_impl(context,value):
    context.mloginpage.select_username_box().send_keys(value)


@When(u'The Manager enters their password {value1}')
def step_impl(context,value1):
    time.sleep(3)
    context.mloginpage.select_password_box().send_keys(value1)


@When(u'The Manager clicks on the login button')
def step_impl(context):
    time.sleep(5)
    context.mloginpage.select_login_button().click()


@Then(u'The Manager should be directed to the {title}')
def step_impl(context,title):
    time.sleep(2)
    assert context.driver.title == "Manager Dashboard"

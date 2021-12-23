
from behave import Given,When,Then
import time

@Given(u'The Employee is on the homepage')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/index.html")


@When(u'The Employee enters their username{value}')
def step_impl(context,value:str):
    context.loginpage.select_username_box().send_keys("John")
    


@When(u'The Employee enters their password{value1}')
def step_impl(context,value1:str):
    context.loginpage.select_password_box().send_keys("John")


@When(u'The Employee clicks on the login button')
def step_impl(context):
    
    context.loginpage.select_login_button().click()



@Then(u'The Employee should be directed to the employee dashboard webpage{title}')
def step_impl(context,title):
    
    assert context.driver.title =="Dashboard"


from behave import step
from configparser import ConfigParser


@step('I insert valid credentials')
def step_impl(context):
    cfg = ConfigParser()
    cfg.read('../moni/config/config.cfg')
    user = cfg.get('login_credentials', 'user')
    password = cfg.get('login_credentials', 'password')
    context.authentication.login_ap(user, password)


@step('I am logged with valid user')
def step_impl(context):
    context.execute_steps(
        u'''Given I go to the Sign in page
            When I insert valid credentials
            And I click on "Sign in" button'''
    )

from behave import step
from nose.tools import assert_equal
from random import choice


@step('I am on the Automation Practice page')
def step_impl(context):
    context.home_page.navigate("http://automationpractice.com")
    assert_equal(context.home_page.get_page_title(), "My Store")


@step('I go to the Sign in page')
def step_impl(context):
    context.home_page.click_sing_in()


@step('I insert valid "{field}" in "{section}" section')
def step_impl(context, field, section):
    if field == 'Email address':
        num = ''.join(choice('0123456789abcdef') for _ in range(5))
        user = 'test_{}@testmail.com'.format(num)
        context.authentication.insert_value_in_section(field, section, user)
    else:
        context.user_account_page.insert_value_in_section(field, section)


@step('I click on "{button}" button')
def step_impl(context, button):
    if button == 'Create an account' or button == 'Sign in':
        context.authentication.click_button(button)
    elif button == 'Register':
        context.user_account_page.click_button()


@step('I see the "{title}" form to complete')
def step_impl(context, title):
    assert_equal(context.user_account_page.get_form_title(), title)


@step('I select an state')
def step_impl(context):
    context.user_account_page.select_state()


@step('I see "{page}" page')
def step_impl(context, page):
    assert_equal(context.home_page.get_page_title(), page)


@step('I see "{username}" user logged')
def step_impl(context, username):
    assert_equal(context.user_account_page.get_user_registered(), username)

from behave import step
from nose.tools import assert_equal

@step('I go to "WOMEN" category')
def step_impl(context):
    context.order_page.select_category()


@step('I select the clothes "Faded Short Sleeve T-shirts"')
def step_impl(context):
    context.order_page.select_clothes()


@step('I press "{option}"')
def step_impl(context, option):
    if option == 'Add to Cart':
        context.order_page.add_to_cart()
    elif option == 'Proceed to checkout':
        context.order_page.proceed_to_checkout()


@step('I check Summary and proceed to checkout')
def step_impl(context):
    context.order_page.proceed_to_checkout_summary()


@step('I check the delivery address data and proceed to checkout')
def step_impl(context):
    context.order_page.proceed_to_checkout_address()


@step('I accept the terms of service and proceed to checkout')
def step_impl(context):
    context.order_page.accept_terms_service()
    context.order_page.proceed_to_checkout_shipping()


@step('I select the payment method "{method}"')
def step_impl(context, method):
    context.order_page.hook_payment(method)


@step('I confirm my order')
def step_impl(context):
    context.order_page.confirm_order()


@step('I see the "{message}" message')
def step_impl(context, message):
        assert_equal(context.order_page.message_order_successfully(), message)
from features.pages.authentication_page import AuthenticationPage
from features.pages.user_account_page import UserAccountPage
from features.pages.home_page import HomePage
from features.pages.order_page import OrderPage


def before_all(context):
    context.home_page = HomePage()
    context.authentication = AuthenticationPage()
    context.user_account_page = UserAccountPage()
    context.order_page = OrderPage()


def after_all(context):
    context.home_page.close()


def after_tag(context, tag):
    if tag == 'LOGIN' or 'USER_ACCOUNT':
        context.authentication.log_out()

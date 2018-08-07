from selenium.webdriver.common.by import By
from features.browser import Browser


class AuthenticationPageLocator(object):
    # Authentication Page Locators

    EMAIL_ADDRESS_CREATE = (By.ID, 'email_create')
    EMAIL_ADDRESS = (By.ID, 'email')
    LOGIN_PASSWORD = (By.ID, 'passwd')
    CREATE_ACCOUNT_BUTTON = (By.ID, 'SubmitCreate')
    SIGN_IN_BUTTON = (By.ID, 'SubmitLogin')
    LOGOUT = (By.CLASS_NAME, 'logout')

    sections = {
        'CREATE AN ACCOUNT': {'Email address': EMAIL_ADDRESS_CREATE},
        'SING IN': {'Email address': EMAIL_ADDRESS,
                    'Password': LOGIN_PASSWORD}
    }

    buttons = {
        'Create an account': CREATE_ACCOUNT_BUTTON,
        'Sign in': SIGN_IN_BUTTON
    }


class AuthenticationPage(Browser):
    # Authentication Page Actions

    def insert_value_in_section(self, field, section, value):
        fields = AuthenticationPageLocator.sections[section]
        self.driver.find_element(*fields[field]).send_keys(value)

    def click_button(self, button):
        self.driver.find_element(*AuthenticationPageLocator.buttons[button]).click()

    def login_ap(self, user, password):
        self.driver.find_element(*AuthenticationPageLocator.EMAIL_ADDRESS).send_keys(user)
        self.driver.find_element(*AuthenticationPageLocator.LOGIN_PASSWORD).send_keys(password)

    def log_out(self):
        self.driver.find_element(*AuthenticationPageLocator.LOGOUT).click()

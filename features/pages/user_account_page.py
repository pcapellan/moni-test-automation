from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.browser import Browser


class UserAccountPageLocator(object):
    # User Account Page Locators

    TITLE_FORM = (By.CLASS_NAME, 'page-subheading')
    USER_REGISTERED = (By.CLASS_NAME, 'account')
    CUSTOMER_FIRSTNAME = (By.ID, 'customer_firstname')
    CUSTOMER_LASTNAME = (By.ID, 'customer_lastname')
    CUSTOMER_PASSWORD = (By.ID, 'passwd')

    FIRSTNAME = (By.ID, 'firstname')
    LASTNAME = (By.ID, 'lastname')
    ADDRESS_1 = (By.ID, 'address1')
    CITY = (By.ID, 'city')
    STATE = (By.ID, 'id_state')
    POSTAL_CODE = (By.ID, 'postcode')
    MOBILE_PHONE = (By.ID, 'phone_mobile')
    ADDRESS_ALIAS = (By.ID, 'alias')
    REGISTER_BUTTON = (By.ID, 'submitAccount')

    sections = {
        'YOUR PERSONAL INFORMATION': {'First name': [(CUSTOMER_FIRSTNAME, 'Juan')],
                                      'Last name': [(CUSTOMER_LASTNAME, 'Perez')],
                                      'Password': [(CUSTOMER_PASSWORD, 'testing')]},
        'YOUR ADDRESS': {'First name': [(FIRSTNAME, 'Juan')],
                         'Last name': [(LASTNAME, 'Perez')],
                         'Address': [(ADDRESS_1, 'Calle 123')],
                         'City': [(CITY, 'Argentina')],
                         'Zip/Postal Code': [(POSTAL_CODE, '50123')],
                         'Mobile phone': [(MOBILE_PHONE, '34677521809')],
                         'Address alias': [(ADDRESS_ALIAS, 'Office')]}
    }


class UserAccountPage(Browser):
    # User Account Page Actions

    def get_form_title(self):
        return self.driver.find_element(*UserAccountPageLocator.TITLE_FORM).text

    def insert_value_in_section(self, val_field, section):
        fields = UserAccountPageLocator.sections[section]
        for (key, value) in fields[val_field]:
            self.driver.find_element(*fields[val_field][0][0]).send_keys(value)

    def select_state(self):
        dropdown_state = Select(self.driver.find_element(*UserAccountPageLocator.STATE))
        # Select "Texas" state
        dropdown_state.options[45].click()

    def click_button(self):
        self.driver.find_element(*UserAccountPageLocator.REGISTER_BUTTON).click()

    def get_user_registered(self):
        return self.driver.find_element(*UserAccountPageLocator.USER_REGISTERED).text

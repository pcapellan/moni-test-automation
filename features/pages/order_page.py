import time
from selenium.webdriver.common.by import By
from features.browser import Browser


class OrderPageLocator(object):
    # Order Page Locators

    TOP_MENU = (By.ID, 'block_top_menu')
    USER_REGISTERED = (By.CLASS_NAME, 'account')
    CLOTHES = (By.CLASS_NAME, 'replace-2x')
    ADD_TO_CART = (By.ID, 'add_to_cart')
    CART_NAVIGATION = (By.CLASS_NAME, 'cart_navigation')
    PROCEED_TO_CHECKOUT_CONTAINER = (By.CLASS_NAME, 'button-container')
    PROCEED_TO_CHECKOUT_CSS = (By.CSS_SELECTOR, "*[title='Proceed to checkout']")
    PROCEED_TO_CHECKOUT_ADDRESS = (By.NAME, 'processAddress')
    TERMS_OF_SERVICE = (By.ID, 'cgv')
    PROCEED_TO_CHECKOUT_SHIPPING = (By.NAME, 'processCarrier')
    HOOK_PAYMENT = (By.ID, 'HOOK_PAYMENT')
    PAY_CHECK = (By.CLASS_NAME, 'cheque')
    PAY_BANK_WIRE = (By.CLASS_NAME, 'bankwire')
    SUBMIT_ORDER = (By.CSS_SELECTOR, "*[type='submit']")
    ORDER_SUCCESSFULLY_CHECK = (By.CLASS_NAME, 'alert')
    ORDER_SUCCESSFULLY_BANK_WIRE = (By.CLASS_NAME, 'cheque-indent')


class OrderPage(Browser):
    # Order Page Actions

    def select_category(self):
        self.driver.find_element(*OrderPageLocator.TOP_MENU).find_element(By.TAG_NAME, 'li').click()

    def select_clothes(self):
        # Faded Short Sleeve T-shirts
        self.driver.find_element(*OrderPageLocator.CLOTHES).click()

    def add_to_cart(self):
        self.driver.find_element(*OrderPageLocator.ADD_TO_CART).find_element(By.NAME, 'Submit').click()

    def proceed_to_checkout(self):
        time.sleep(3)
        self.driver.find_element(*OrderPageLocator.PROCEED_TO_CHECKOUT_CONTAINER) \
            .find_element(*OrderPageLocator.PROCEED_TO_CHECKOUT_CSS).click()

    def proceed_to_checkout_summary(self):
        self.driver.find_element(*OrderPageLocator.CART_NAVIGATION) \
            .find_element(*OrderPageLocator.PROCEED_TO_CHECKOUT_CSS).click()

    def proceed_to_checkout_address(self):
        self.driver.find_element(*OrderPageLocator.PROCEED_TO_CHECKOUT_ADDRESS).click()

    def accept_terms_service(self):
        self.driver.find_element(*OrderPageLocator.TERMS_OF_SERVICE).click()

    def proceed_to_checkout_shipping(self):
        self.driver.find_element(*OrderPageLocator.PROCEED_TO_CHECKOUT_SHIPPING).click()

    def hook_payment(self, method):
        if method == 'bank wire':
            self.driver.find_element(*OrderPageLocator.HOOK_PAYMENT) \
                .find_element(*OrderPageLocator.PAY_BANK_WIRE).click()
        elif method == 'check':
            self.driver.find_element(*OrderPageLocator.HOOK_PAYMENT) \
                .find_element(*OrderPageLocator.PAY_CHECK).click()

    def confirm_order(self):
        self.driver.find_element(*OrderPageLocator.CART_NAVIGATION) \
            .find_element(*OrderPageLocator.SUBMIT_ORDER).click()

    def message_order_successfully(self):
        return self.driver.find_element(*OrderPageLocator.ORDER_SUCCESSFULLY_BANK_WIRE).text

from selenium.webdriver.common.by import By

from features.browser import Browser


class HomePageLocator(object):
    # Home Page Locators
    SIGN_IN = (By.CLASS_NAME, "login")


class HomePage(Browser):
    # Home Page Actions

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def click_sing_in(self):
        self.driver.find_element(*HomePageLocator.SIGN_IN).click()

"""
login_locators module stores the key value pair for locators used
in the LoginPage class. Future considerations should be taken for the
use of pythonic dictionaries vs the class-based approach for locators.
"""
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """
    Locators for the login module.

    design borrowed from
    https://github.com/baijum/pitracker/blob/master/test/acceptance/locators.py
    """

    login_input_field_loc = {

        'username': (By.CSS_SELECTOR, "input.text.user-name"),
        'password': (By.CSS_SELECTOR, "input.passwords")
    }

    login_button_loc = {

        'submit': (By.CSS_SELECTOR, "button.action.login-action"),
        'submit2': (By.XPATH, '//button/action')
    }

    login_text_field_loc = {

        'initial_loading': (By.CSS_SELECTOR, '.initial-loading'),
        'submit2': (By.XPATH, '//button/action'),
        'logout_message': (By.CSS_SELECTOR, '.w-Logout')
    }

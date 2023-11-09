import time
from .base_page import BasePage
from .locators import *
from Rostelecom.exeptions import CaptchaError
from selenium.webdriver.support.wait import TimeoutException


class AuthPage(BasePage):

    def enter_username(self, value):
        phone_field = self.find_element(AuthLocators.ENTER_LOGIN)
        phone_field.click()
        phone_field.send_keys(value)

    def enter_password(self, value):
        password_field = self.find_element(AuthLocators.ENTER_PASSWORD)
        password_field.click()
        password_field.send_keys(value)

    def sign_in_button_click(self):
        button = self.find_element(AuthLocators.SING_IN_BUTTON)
        button.click()

    def check_authorize_page(self):
        elem = self.find_element(AuthLocators.CHECK_AUTHORIZE)
        elem = elem.get_attribute('src')
        if elem.startswith('https://'):
            return elem
        else:
            elem = 'https://' + elem
            return elem

    def check_not_authorize_page(self):
        elem = self.find_elements(AuthLocators.CHECK_NOT_AUTHORIZE)
        return elem

    def check_active_tab_menu(self):
        tab_menu = self.find_elements(AuthLocators.ACTIVE_TAB_IN_MENU)
        check = [i.text for i in tab_menu]
        return ' '.join(check)

    def switch_to_ls(self):
        ls = self.find_element(AuthLocators.SWITCH_TO_LS)
        ls.click()

    def wait_for_captcha_input(self, wait_time=15):
        '''Метод для паузы автотеста для ручного вводa капчи'''
        try:
            captcha = self.find_element(AuthLocators.CAPTCHA, 5)
            if captcha:
                return time.sleep(wait_time)
        except TimeoutException:
            pass

    def result_of_auth(self):
        prompt = self.find_element(AuthLocators.RESULT_OF_AUTH)
        print(prompt.text)
        if prompt.text == 'Неверно введен текст с картинки':
            raise CaptchaError

    def check_correct_phone_format(self):
        error = self.find_element(AuthLocators.CHECK_CORRECT_PHONE_FORMAT)
        print(error.text)
        return error.text







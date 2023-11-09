import re
import pyperclip
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import *
from imapclient import IMAPClient
from Rostelecom.config import valid_email_restore, app_key
from selenium.webdriver.support.wait import TimeoutException


class RestorePage(BasePage):
    def go_to_restore(self):
        forgot_password = self.find_element(RestoreLocators.GO_TO_RESTORE)
        forgot_password.click()

    def enter_data(self, value):
        input_field = self.find_element(RestoreLocators.ENTER_DATA)
        input_field.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        input_field.send_keys(value)

    def wait_for_captcha_input(self, wait_time=15):
        '''Метод для паузы автотеста для ручного вводa капчи'''
        try:
            captcha = self.find_element(RestoreLocators.CAPTCHA, 10)
            if captcha:
                return time.sleep(wait_time)
        except TimeoutException:
            pass

    def restore_by_email(self):
        methods = self.find_element(RestoreLocators.RESTORE_BY_MAIL)
        methods.click()

    def restore_by_phone(self):
        methods = self.find_element(RestoreLocators.RESTORE_BY_PHONE)
        methods.click()

    def go_reset_password(self):
        reset_btn = self.find_element(RestoreLocators.GO_RESET_PASSWORD)
        reset_btn.click()

    def continue_button_click(self):
        continue_btn = self.find_element(RestoreLocators.CONTINUE_BTN)
        continue_btn.click()

    def restore(self, value):
        password_input = self.find_element(RestoreLocators.PASSWORD, 50)
        confirm_password_input = self.find_element(RestoreLocators.CONFIRM_PASSWORD)
        password_input.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
            Keys.BACKSPACE).perform()
        password_input.send_keys(value)
        confirm_password_input.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
            Keys.BACKSPACE).perform()
        confirm_password_input.send_keys(value)

    def check_auth_page(self):
        page_auth = self.find_element(RestoreLocators.WAIT_PAGE_LOAD, 30)
        return page_auth.text

    def click_save_button(self):
        save_btn = self.find_element(RestoreLocators.SAVE_BUTTON)
        save_btn.click()

    def get_verification_code(self):
        '''Метод для ожидания прихода кода подтверждения на почту через протокол IMAP'''
        imap_server = IMAPClient('imap.mail.ru', ssl=True)
        imap_server.login(valid_email_restore, app_key)
        imap_server.select_folder('INBOX')
        imap_server.idle()
        while True:
            responses = imap_server.idle_check(timeout=5)
            if responses:
                imap_server.idle_done()
                break
        messages = imap_server.search(['UNSEEN', 'FROM', 'rostelecom@info.rt.ru'])
        if messages:
            latest_message_id = messages[-1]
            message_data = imap_server.fetch([latest_message_id], ['BODY[]'])
            for message in message_data.values():
                body = message[b'BODY[]']
                if body:
                    decoded_body = body.decode('utf-8')
                    pattern = r": \d{6}"
                    match = re.search(pattern, decoded_body)
                    if match:
                        verification_code = match.group(0)[2:]
                        code = str(verification_code)
                        return code
        imap_server.logout()

    def input_code(self):
        code = self.get_verification_code()
        pyperclip.copy(code)
        input_code = self.find_element(RegisterLocators.GET_CODE)
        input_code.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    def check_active_tab_menu(self):
        tab_menu = self.find_element(AuthLocators.ACTIVE_TAB_IN_MENU)
        print(tab_menu.text)
        return tab_menu.text

    def go_to_next_field(self):
        field = self.find_element(RestoreLocators.CAPTCHA)
        field.send_keys(Keys.TAB)

    def check_error_message(self):
        error = self.find_element(RestoreLocators.CHECK_ERROR_MESSAGE)
        return error.text






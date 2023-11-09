import re
import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import *
from imapclient import IMAPClient
from Rostelecom.config import valid_email_reg, app_key


class RegisterPage(BasePage):

    def go_to_register_page(self):
        go_reg_btn = self.find_element(RegisterLocators.GO_TO_REG_BTN)
        go_reg_btn.click()

    def enter_first_name(self, value):
        first_name = self.find_element(RegisterLocators.FIRST_NAME)
        first_name.click()
        first_name.send_keys(value)

    def enter_last_name(self, value):
        last_name = self.find_element(RegisterLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys(value)

    def enter_email_or_phone(self, value):
        phone_field = self.find_element(RegisterLocators.ENTER_EMAIL)
        phone_field.click()
        phone_field.send_keys(value)

    def enter_password(self, value):
        password_field = self.find_element(RegisterLocators.ENTER_PASSWORD)
        password_field.click()
        password_field.send_keys(value)

    def confirm_password(self, value):
        password_confirm_field = self.find_element(RegisterLocators.CONFIRM_PASSWORD)
        password_confirm_field.click()
        password_confirm_field.send_keys(value)

    def enter_register_button(self):
        button = self.find_element(RegisterLocators.REGISTER_BUTTON)
        button.click()

    def check_success_reg(self):
        elem = self.find_element(RegisterLocators.CHECK_SUCCESS_REG)
        return elem.text

    def check_invalid_name_and_surname(self):
        elem = self.find_element(RegisterLocators.CHECK_UNSUCCESS_NAME_AND_SURNAME)
        return elem.text

    def check_invalid_phone_and_email(self):
        elem = self.find_element(RegisterLocators.CHECK_UNSUCCESS_PHONE_AND_EMAIL)
        print(elem.text)
        return elem.text

    def check_register_already_existing_account(self):
        elem = self.find_element(RegisterLocators.CHECK_ALREADY_EXISTING_ACCOUNT)
        return elem.text

    def check_error_message(self):
        password_errors = self.find_element(RegisterLocators.CHECK_ERROR_MESSAGE)
        print(password_errors.text)
        return password_errors.text

    def get_verification_code(self):
        '''Метод для ожидания прихода кода подтверждения на почту через протокол IMAP'''
        imap_server = IMAPClient('imap.mail.ru', ssl=True)
        imap_server.login(valid_email_reg, app_key)
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
                        print(code)
                        return code
        imap_server.logout()

    def input_code(self):
        code = self.get_verification_code()
        pyperclip.copy(code)
        input_code = self.find_element(RegisterLocators.GET_CODE)
        input_code.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

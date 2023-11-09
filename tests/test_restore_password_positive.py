import pytest
from Rostelecom.config import *
from Rostelecom.pages.restore_password_page import RestorePage


@pytest.mark.positive
@pytest.mark.restore
def test_success_restore_password_by_phone(browser):
    '''Проверка восстановления пароля по номеру телефона через СМС'''
    page = RestorePage(browser)
    page.go_to_site()
    page.go_to_restore()
    page.enter_data(valid_phone_restore)
    page.wait_for_captcha_input()
    page.go_reset_password()
    page.restore_by_phone()
    page.continue_button_click()
    page.restore(new_password_restore)
    page.click_save_button()
    auth_page = page.check_auth_page()
    assert 'Авторизация' in auth_page


@pytest.mark.positive
@pytest.mark.restore
def test_success_restore_password_by_email(browser):
    '''Проверка восстановления пароля через почту'''
    page = RestorePage(browser)
    page.go_to_site()
    page.go_to_restore()
    page.enter_data(valid_email_restore)
    page.wait_for_captcha_input()
    page.go_reset_password()
    page.restore_by_email()
    page.continue_button_click()
    page.input_code()
    page.restore(new_password_restore)
    page.click_save_button()
    auth_page = page.check_auth_page()
    assert 'Авторизация' in auth_page

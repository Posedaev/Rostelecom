import pytest
from Rostelecom.config import *
from Rostelecom.pages.auth_page import AuthPage


@pytest.mark.auth
@pytest.mark.negative
def test_auth_empty_userdata(browser):
    '''Проверка авторизайци с пустыми полями данных'''
    page = AuthPage(browser)
    page.go_to_site()
    page.wait_for_captcha_input()
    page.sign_in_button_click()
    text_error = page.check_authorize_page()
    assert text_error


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [invalid_email, invalid_phone, invalid_login, invalid_ls],
                         ids=[invalid_email, invalid_phone, invalid_login, invalid_ls])
def test_auth_with_invalid_userdata(browser, username):
    '''Проверка авторизации пользователя с неверными данными'''
    page = AuthPage(browser)
    page.go_to_site()
    if username == valid_ls:
        page.switch_to_ls()
    page.enter_username(username)
    page.enter_password(invalid_password)
    page.wait_for_captcha_input()
    page.sign_in_button_click()
    page.result_of_auth()
    text_error = page.check_authorize_page()
    assert text_error


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [valid_email, valid_phone, valid_login, valid_ls], ids=[valid_email, valid_phone, valid_login, valid_ls])
def test_auth_with_valid_username_and_invalid_password(browser, username):
    '''Проверка авторизации с верным телефоном/почтой/логином/ЛС и неверным паролем'''
    page = AuthPage(browser)
    page.go_to_site()
    if username == valid_ls:
        page.switch_to_ls()
    page.enter_username(username)
    page.enter_password(invalid_password)
    page.wait_for_captcha_input()
    page.sign_in_button_click()
    page.result_of_auth()
    text_error = page.check_authorize_page()
    assert text_error


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [invalid_email, invalid_phone, invalid_login, invalid_ls],
                         ids=[invalid_email, invalid_phone, invalid_login, invalid_ls])
def test_auth_with_invalid_username_and_valid_password(browser, username):
    '''Проверка авторизации с неверным телефоном/почтой/логином/ЛС и верным паролем'''
    page = AuthPage(browser)
    page.go_to_site()
    if username == invalid_ls:
        page.switch_to_ls()
    page.enter_username(username)
    page.enter_password(invalid_password)
    page.wait_for_captcha_input()
    page.sign_in_button_click()
    page.result_of_auth()
    text_error = page.check_authorize_page()
    assert text_error


@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('phone', [incorrect_phone_format_1, incorrect_phone_format_2, incorrect_phone_format_3])
def test_with_incorrect_phone_format(browser, phone):
    '''Проверка авторизации с некорректным номером телефона'''
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_username(phone)
    page.enter_password(valid_password)
    page.sign_in_button_click()
    elem = page.check_correct_phone_format()
    assert 'Неверный формат' in elem

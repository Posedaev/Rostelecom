import pytest
import requests
from Rostelecom.config import *
from Rostelecom.pages.auth_page import AuthPage


@pytest.mark.positive
@pytest.mark.xfail()
@pytest.mark.parametrize('username', [valid_email, valid_phone, valid_login, valid_ls],
                         ids=['valid_email', 'valid_phone', 'valid_login', 'valid_ls'])
def test_switch_tab_menu(browser, username):
    '''Проверка автоматического переключения таб выбора аунтефикации'''
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_username(username)
    page.enter_password(valid_password)
    if username == valid_email:
        assert page.check_active_tab_menu() == 'Почта'
    elif username == valid_phone:
        assert page.check_active_tab_menu() == 'Телефон'
    elif username == valid_login:
        assert page.check_active_tab_menu() == 'Логин'
    elif username == valid_ls:
        assert page.check_active_tab_menu() == 'Лицевой счёт'
        '''При вводе лицевого счета таб меню принимает его за номер телефона и не переключается на ЛС'''


@pytest.mark.positive
@pytest.mark.auth
def test_auth_with_phone(browser):
    '''проверка авторизации по номеру телефона'''
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_username(valid_phone)
    page.enter_password(valid_password)
    page.sign_in_button_click()
    check = page.check_authorize_page()
    avatar = requests.get(check)
    assert avatar.status_code == 200


@pytest.mark.positive
@pytest.mark.auth
def test_auth_with_email(browser):
    '''проверка авторизации по почте'''
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    tab = page.check_active_tab_menu()
    assert 'Почта' in tab
    page.sign_in_button_click()
    check = page.check_authorize_page()
    avatar = requests.get(check)
    assert avatar.status_code == 200

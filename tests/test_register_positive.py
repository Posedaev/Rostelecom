import pytest
from Rostelecom.config import *
from Rostelecom.pages.register_page import RegisterPage


@pytest.mark.register
@pytest.mark.positive
def test_success_register(browser):
    '''Проверка регистрации нового пользователя'''
    page = RegisterPage(browser)
    page.go_to_site()
    page.go_to_register_page()
    page.enter_first_name(valid_name_reg)
    page.enter_last_name(valid_surname_reg)
    page.enter_email_or_phone(valid_email_reg)
    page.enter_password(valid_password_reg)
    page.confirm_password(valid_password_reg)
    page.enter_register_button()
    page.input_code()
    elem = page.check_success_reg()
    assert 'данные' in elem




import pytest
from Rostelecom.config import *
from Rostelecom.pages.register_page import RegisterPage


@pytest.mark.register
@pytest.mark.negative
@pytest.mark.parametrize('firstname', ['', '  ', 'alex', 'x', '12345', '1', '#@$%;:"(){}[]', '†✉§©☯☭?$£¢'],
                         ids=['empty', 'two_pases', 'english_name', 'char', "numbers", 'digit', 'spec_symbols',
                              'unicode_symbols'])
def test_register_with_invalid_firstname(browser, firstname):
    '''Проверка страницы регистрации с неверным форматом имени'''
    page = RegisterPage(browser)
    page.go_to_site()
    page.go_to_register_page()
    page.enter_first_name(firstname)
    page.enter_last_name(valid_surname_reg)
    page.enter_email_or_phone(valid_email_reg)
    page.enter_password(valid_password_reg)
    page.confirm_password(valid_password_reg)
    page.enter_register_button()
    error_message = page.check_error_message()
    assert 'Необходимо заполнить поле кириллицей' in error_message


@pytest.mark.register
@pytest.mark.negative
@pytest.mark.parametrize('lastname', ['', '  ', 'ivanov', 'i', '12345', '1', '#@$%;:"(){}[]', '†✉§©☯☭?$£¢'],
                         ids=['empty', 'two_pases', 'english_surname', 'char', "numbers", 'digit', 'spec_symbols',
                              'unicode_symbols'])
def test_register_with_invalid_lastname(browser, lastname):
    '''Проверка страницы регистрации с неверным форматом фамилии'''
    page = RegisterPage(browser)
    page.go_to_site()
    page.go_to_register_page()
    page.enter_first_name(valid_name_reg)
    page.enter_last_name(lastname)
    page.enter_email_or_phone(valid_email_reg)
    page.enter_password(valid_password_reg)
    page.confirm_password(valid_password_reg)
    page.enter_register_button()
    error_message = page.check_invalid_name_and_surname()
    assert 'Необходимо заполнить поле кириллицей' in error_message


@pytest.mark.register
@pytest.mark.negative
@pytest.mark.parametrize('email_phone', ['9', '012345698', '96300', 'pochta@', '@.', '@gmail.com'],
                         ids=['one_digit', '9 numbers', '5 numbers', 'invalid format email', '@.', '@gmail.com'])
def test_register_with_invalid_phone_and_email(browser, email_phone):
    '''Тест для проверки ввода номере телефона и почты в неверном формате при регистрации'''
    page = RegisterPage(browser)
    page.go_to_site()
    page.go_to_register_page()
    page.enter_last_name(valid_surname_reg)
    page.enter_first_name(valid_name_reg)
    page.enter_email_or_phone(email_phone)
    page.enter_password(valid_password_reg)
    page.confirm_password(valid_password_reg)
    elem = page.check_invalid_phone_and_email()
    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in elem


@pytest.mark.register
@pytest.mark.negative
def test_register_already_existing_account(browser):
    '''Проверка регистрации через почту уже существующего аккаунта'''
    page = RegisterPage(browser)
    page.go_to_site()
    page.go_to_register_page()
    page.enter_last_name(valid_surname_reg)
    page.enter_first_name(valid_name_reg)
    page.enter_email_or_phone(valid_email)
    page.enter_password(valid_password_reg)
    page.confirm_password(valid_password_reg)
    page.enter_register_button()
    modal_card = page.check_register_already_existing_account()
    assert "Учётная запись уже существует" in modal_card


@pytest.mark.register
@pytest.mark.negative
@pytest.mark.parametrize('password', ['', '1', '7136245', 'QwertyAsdfg123789456L', 'qawsedrft1', 'QAWSEDRFT1'],
                         ids=['empty', 'digit', '7 digits', '21 digits', 'lowwercase letters', 'big letters'])
def test_register_with_invalid_password(browser, password):
    '''Проверка регистрации c разлитчными комбинациями возможных паролей неверного формата'''
    page = RegisterPage(browser)
    page.go_to_site()
    page.go_to_register_page()
    page.enter_last_name(valid_surname_reg)
    page.enter_first_name(valid_name_reg)
    page.enter_email_or_phone(valid_email)
    page.enter_password(password)
    page.confirm_password(password)
    page.enter_register_button()
    password_errors = page.check_error_message()
    assert (password_errors == 'Длина пароля должна быть не менее 8 символов'
            or password_errors == 'Длина пароля должна быть не более 20 символов'
           or password_errors == 'Пароль должен содержать хотя бы одну заглавную букву'
           or password_errors == 'Пароль должен содержать хотя бы одну строчную букву')


@pytest.mark.register
@pytest.mark.negative
def test_with_different_passwords(browser):
    '''Проверка регистрации c разными паролями'''
    page = RegisterPage(browser)
    page.go_to_site()
    page.go_to_register_page()
    page.enter_last_name(valid_surname_reg)
    page.enter_first_name(valid_name_reg)
    page.enter_email_or_phone(valid_email)
    page.enter_password(valid_password_reg)
    page.confirm_password(valid_password_reg2)
    page.enter_register_button()
    password_errors = page.check_error_message()
    assert 'Пароли не совпадают' in password_errors

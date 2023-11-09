import pytest
from Rostelecom.config import *
from Rostelecom.pages.restore_password_page import RestorePage


@pytest.mark.negative
@pytest.mark.restore
@pytest.mark.xfail()
@pytest.mark.parametrize('username', [valid_email_restore, valid_phone_restore, valid_login_restore, valid_ls_restore],
                         ids=['email', 'phone', 'login', 'ls'])
def test_restore_check_switch_tab_menu(browser, username):
    '''Проверка переключения таб меню
    При вводе лицевого счета вкладка таб меню переключается на номер телефона'''
    page = RestorePage(browser)
    page.go_to_site()
    page.go_to_restore()
    page.enter_data(username)
    page.go_to_next_field()
    active_tab = page.check_active_tab_menu()
    if username == valid_email_restore:
        assert active_tab == 'Почта'
    elif username == valid_phone:
        assert active_tab == 'Телефон'
    elif username == valid_login:
        assert active_tab == 'Логин'
    elif username == valid_ls:
        assert active_tab == 'Лицевой счёт'


@pytest.mark.negative
@pytest.mark.restore
def test_restore_password_via_email(browser, passwords):
    '''Проверка требований при создании нового пароля'''
    page = RestorePage(browser)
    page.go_to_site()
    page.go_to_restore()
    page.enter_data(valid_email)
    page.wait_for_captcha_input()
    page.go_reset_password()
    page.restore_by_email()
    page.continue_button_click()
    page.input_code()
    for i in passwords:
        page.restore(i)
        page.click_save_button()
        error_message = page.check_error_message()
        assert (error_message == 'Длина пароля должна быть не менее 8 символов'
                or error_message == 'Длина пароля должна быть не более 20 символов'
                or error_message == 'Пароль должен содержать хотя бы одну заглавную букву'
                or error_message == 'Пароль должен содержать хотя бы одну строчную букву')

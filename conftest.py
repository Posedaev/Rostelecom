import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def passwords():
    '''Набор паролей для негативных проверок'''
    return ['1', '1234567', 'QWERTYU', 'qwertyu', '123456qwerty789014hJK',  '†✉§©☯☭?$£¢', '#@$%;:"(){}[]']

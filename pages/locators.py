from selenium.webdriver.common.by import By


class AuthLocators:
    CAPTCHA = (By.CSS_SELECTOR, '.rt-captcha.login-form__captcha')
    TAB_MENU = (By.CSS_SELECTOR, '.rt-tabs.rt-tabs--orange .rt-tab.rt-tab--small')
    ENTER_LOGIN = (By.ID, 'username')
    ENTER_PASSWORD = (By.ID, 'password')
    SING_IN_BUTTON = (By.ID, 'kc-login')
    CHECK_AUTHORIZE = (By.TAG_NAME, 'img')
    ACTIVE_TAB_IN_MENU = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')
    CHECK_NOT_AUTHORIZE = (By.XPATH, '//h1')
    SWITCH_TO_LS = (By.ID, 't-btn-tab-ls')
    RESULT_OF_AUTH = (By.ID, 'form-error-message')
    CHECK_CORRECT_PHONE_FORMAT = (By.XPATH, '//span[contains(text(), "Неверный формат")]')


class RegisterLocators:
    GO_TO_REG_BTN = (By.ID, 'kc-register')
    FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    SELECT_CITY = (By.CLASS_NAME, 'rt-input__input rt-select__input')
    ENTER_EMAIL = (By.ID, 'address')
    CONFIRM_MAIL_CODE = (By.ID, 'verification_code_input')
    ENTER_PASSWORD = (By.ID, 'password')
    CONFIRM_PASSWORD = (By.ID, 'password-confirm')
    REGISTER_BUTTON = (By.NAME, 'register')
    CHECK_SUCCESS_REG = (By.CSS_SELECTOR, 'h3[class="card-title"]:nth-child(2)')
    CHECK_UNSUCCESS_NAME_AND_SURNAME = (By.XPATH, '//span[contains(text(), "Необходимо заполнить поле")]')
    CHECK_UNSUCCESS_PHONE_AND_EMAIL = (By.XPATH, '//span[contains(text(), "Введите телефон в формате ")]')
    CHECK_ALREADY_EXISTING_ACCOUNT = (By.XPATH, '//h2[contains(text(), "Учётная запись уже существует")]')
    CHECK_ERROR_MESSAGE = (By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')
    ALERT = (By.CSS_SELECTOR, '.card-modal__card-wrapper')
    GET_CODE = (By.ID, 'rt-code-0')


class RestoreLocators:
    GO_TO_RESTORE = (By.ID, 'forgot_password')
    ENTER_DATA = (By.ID, 'username')
    RESTORE_BY_MAIL = (By.XPATH, '//span[(text() ="По e-mail")]')
    RESTORE_BY_PHONE = (By.XPATH, '//span[(text() ="По номеру телефона")]')
    GO_RESET_PASSWORD = (By.ID, 'reset')
    CONTINUE_BTN = (By.CSS_SELECTOR, '.rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.reset-choice-form__reset-btn')
    PASSWORD = (By.ID, 'password-new')
    CONFIRM_PASSWORD = (By.ID, 'password-confirm')
    SAVE_BUTTON = (By.ID, 't-btn-reset-pass')
    CAPTCHA = (By.ID, 'captcha')
    WAIT_PAGE_LOAD = (By.XPATH, '//h1[contains(text(), "Авторизация")]')
    CHECK_RESTORE = (By.ID, 'form-error-message')
    CHECK_ERROR_MESSAGE = (By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')





from selenium.webdriver.common.by import By
from pageobjects.base.page import Page
from pageobjects.components.header import Header
from retry import retry
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class LoginPage(Page):
    def open(self, *args, **kwargs):
        super().open("login")

    @property
    def div_login_error(self):
        return self.driver.find_element(by=By.ID, value="login-validation-box")

    @property
    def div_password_error(self):
        return self.driver.find_element(by=By.ID, value="password-validation-box")

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.ID, value="login-button")

    @property
    def input_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    @property
    def input_login(self):
        return self.driver.find_element(by=By.ID, value="login")

    @retry(StaleElementReferenceException)
    def fill_login(self, login):
        self.input_login.send_keys(login)

    @retry(StaleElementReferenceException)
    def fill_password(self, password):
        self.input_password.send_keys(password)

    @retry((StaleElementReferenceException, ValueError))
    def login(self, login, password):
        self.wait_last_event()
        self.fill_login(login)
        self.fill_password(password)

        # Сохраняем в переменную (а не используем свойство) для того,
        # т.к. если выполнять поиск элемента перед кликом, мы рискуем,
        # что страница перерисуется и ввод опять сбросится
        btn_enter = self.btn_enter

        # Проверяем, что ввод не сбросился
        value = self.input_password.get_attribute('value')
        if len(value) == 0:
            raise ValueError

        btn_enter.click()

    @retry(StaleElementReferenceException)
    def logout(self):
        Header.create(self.driver).logout()

    def wait_for_redirect(self):
        self.driver.find_element(by=By.ID, value="createTeamBtnId")

    def is_login_error_exists(self):
        return self.is_element_exists(selector="login-validation-box")

    @retry((StaleElementReferenceException, NoSuchElementException), tries=5)
    def login_error_text(self):
        return self.div_login_error.text

    def is_password_error_exists(self):
        return self.is_element_exists(selector="password-validation-box")

    @retry((StaleElementReferenceException, NoSuchElementException), tries=5)
    def password_error_text(self):
        return self.div_password_error.text

from selenium.webdriver.common.by import By
from pageobjects.base.page import Page
from pageobjects.components.header import Header
from retry import retry
from selenium.common.exceptions import StaleElementReferenceException


class LoginPage(Page):

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.ID, value="login-button")

    @property
    def input_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    @property
    def input_login(self):
        return self.driver.find_element(by=By.ID, value="login")

    def open(self, *args, **kwargs):
        super().open("login")

    @retry(StaleElementReferenceException)
    def fill_login(self, login):
        self.input_login.send_keys(login)

    @retry(StaleElementReferenceException)
    def fill_password(self, password):
        self.input_password.send_keys(password)

    @retry(StaleElementReferenceException)
    def login(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.btn_enter.click()

    @retry(StaleElementReferenceException)
    def logout(self):
        Header.create(self.driver).logout()

    def wait_for_redirect(self):
        self.driver.find_element(by=By.ID, value="createTeamBtnId")

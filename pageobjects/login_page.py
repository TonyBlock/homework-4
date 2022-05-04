from selenium.webdriver.common.by import By

from pageobjects.page import Page


class LoginPage(Page):

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.ID, value="login-button")

    @property
    def input_login(self):
        return self.driver.find_element(by=By.ID, value="login")

    def open(self, *args, **kwargs):
        super().open("login")

    def fill_login(self, login):
        pass

    def fill_password(self, password):
        pass

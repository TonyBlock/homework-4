from selenium.webdriver.common.by import By
from pageobjects.base.page import Page
from selenium.common.exceptions import StaleElementReferenceException
from retry import retry


class ProfilePage(Page):

    @property
    def btn_avatar(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=".button.profile-box__button")

    @property
    def btn_save(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=".button.profile-box__save-btn")

    @property
    def input_avatar(self):
        return self.driver.find_element(by=By.ID, value="avatarId")

    @property
    def input_login(self):
        return self.driver.find_element(by=By.ID, value="login")

    @property
    def input_email(self):
        return self.driver.find_element(by=By.ID, value="email")

    @property
    def input_new_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    @property
    def input_new_password_repeat(self):
        return self.driver.find_element(by=By.ID, value="passwordRepeat")

    @property
    def input_old_password(self):
        return self.driver.find_element(by=By.ID, value="oldPassword")

    def open(self, *args, **kwargs):
        super().open("profile")

    @retry(StaleElementReferenceException)
    def upload_avatar(self, avatar_path):
        self.input_avatar.send_keys(avatar_path)

from selenium.webdriver.common.by import By
from pageobjects.base.page import Page
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from retry import retry


class ProfilePage(Page):

    def click_save_if_page_not_repainted(self):
        save_btn = self.btn_save
        # Проверяем, что ввод не сбросился
        value = self.input_old_password.get_attribute('value')
        if len(value) == 0:
            raise ValueError

        save_btn.click()

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

    @property
    def div_avatar_error(self):
        return self.driver.find_element(by=By.ID, value="avatar-validation-box")

    def open(self, *args, **kwargs):
        super().open("profile")

    @retry(StaleElementReferenceException)
    def upload_avatar(self, avatar_path):
        self.input_avatar.send_keys(avatar_path)

    def is_avatar_error_exists(self):
        return self.is_element_exists(selector="avatar-validation-box")

    @retry((StaleElementReferenceException, ElementNotInteractableException))
    def set_input_login(self, text):
        login_input = self.input_login
        login_input.clear()
        login_input.send_keys(text)

    @retry(StaleElementReferenceException)
    def set_input_email(self, text):
        email_input = self.input_email
        email_input.clear()
        email_input.send_keys(text)

    @retry((StaleElementReferenceException, ElementNotInteractableException))
    def set_input_new_password(self, text):
        self.input_new_password.send_keys(text)

    @retry((StaleElementReferenceException, ElementNotInteractableException))
    def set_input_new_password_repeat(self, text):
        self.input_new_password_repeat.send_keys(text)

    @retry((StaleElementReferenceException, ElementNotInteractableException))
    def set_old_password(self, text):
        self.input_old_password.send_keys(text)

    @retry((StaleElementReferenceException, ElementNotInteractableException))
    def click_save_btn(self):
        self.btn_save.click()

    @property
    @retry((StaleElementReferenceException, ValueError))
    def input_email_text(self):
        value = self.input_email.get_attribute('value')
        if len(value) == 0:
            raise ValueError
        return value

    @property
    @retry((StaleElementReferenceException, ValueError))
    def input_login_text(self):
        value = self.input_login.get_attribute('value')
        if len(value) == 0:
            raise ValueError
        return value

    @retry(StaleElementReferenceException)
    def input_login_clear(self):
        self.input_login.clear()

    @retry((StaleElementReferenceException, ValueError))
    def change_login(self, new_login, password):
        self.wait_last_event()
        self.set_input_login(new_login)
        self.set_old_password(password)
        self.click_save_if_page_not_repainted()

    @retry((StaleElementReferenceException, ValueError))
    def change_email(self, new_email, password):
        self.wait_last_event()
        self.set_input_email(new_email)
        self.set_old_password(password)
        self.click_save_if_page_not_repainted()

    def is_input_error_exists(self):
        return self.is_element_exists(by=By.CSS_SELECTOR, selector=".error.error_margin")

    def is_login_error_exists(self):
        return self.is_element_exists(selector="login-validation-box")

    # Страница может перерисоваться после того как мы ввели данные.
    # В таком случае (ValueError) вводим данные повторно.
    @retry((StaleElementReferenceException, ValueError))
    def change_password(self, new_password, new_password_repeat, old_password):
        self.wait_last_event()
        self.set_input_new_password(new_password)
        self.set_input_new_password_repeat(new_password_repeat)
        self.set_old_password(old_password)
        self.click_save_if_page_not_repainted()

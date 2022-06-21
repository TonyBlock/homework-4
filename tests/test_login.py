from pageobjects.pages.login import LoginPage
from pageobjects.components.header import Header
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data
from utils.utils import generate_unique_login


class LoginTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)

    def test_login(self):
        self.page.open()
        self.page.login(authorization_data["login"], authorization_data["password"])
        self.page.wait_for_redirect()
        self.assertEqual(authorization_data["login"], Header.create(self.driver).user_name,
                         "Ожидался успешный вход в аккаунт, а в хедере отображается логин пользователя")
        self.page.logout()

    def test_invalid_login(self):
        self.page.open()
        self.page.login("x", authorization_data["password"])
        self.assertTrue(self.page.is_login_error_exists(), "Ожидался вывод контейнера с ошибкой")
        self.assertEqual(self.page.login_error_text(), "Введите логин длиной от 3 до 20 символов",
                         "Ожидался вывод сообщения о не корректной длине логина")

    def test_invalid_password(self):
        self.page.open()
        self.page.login(authorization_data["login"], "x")
        self.assertTrue(self.page.is_password_error_exists(), "Ожидался вывод контейнера с ошибкой")
        self.assertEqual(self.page.password_error_text(), "Введите пароль длиной от 6 до 25 символов",
                         "Ожидался вывод сообщения о не корректной длине пароля")

    def test_invalid_auth_data(self):
        self.page.open()
        self.page.login(generate_unique_login(), authorization_data["password"])
        self.assertTrue(self.page.is_password_error_exists(), "Ожидался вывод контейнера с ошибкой для поля с паролем")
        self.assertTrue(self.page.is_login_error_exists(), "Ожидался вывод контейнера с ошибкой для поля с логином")
        self.assertEqual(self.page.password_error_text(), "Неверный логин или пароль",
                         "Ожидался вывод сообщения о неверном логине или пароле")

    def tearDown(self):
        super().tearDown()

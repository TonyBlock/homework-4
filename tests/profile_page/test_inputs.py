from pageobjects.pages.profile import ProfilePage
from pageobjects.components.header import Header
from tests.base_test_case import TestCaseWithLoginLogout
import utils.constants as constants
import utils.utils as utils


class ProfileInputTest(TestCaseWithLoginLogout):
    def setUp(self):
        super().setUp()

        self.page = ProfilePage(self.driver)
        self.page.open()

    def test_change_login_busy(self):
        self.page.change_login("busylogin", constants.authorization_data["password"])
        self.page.refresh()
        self.assertEqual(self.page.input_login_text,
                         constants.authorization_data["login"],
                         "Логин должен остаться прежним, т.к. новый логин уже занят")
        self.assertEqual(Header.create(self.driver).user_name,
                         constants.authorization_data["login"],
                         "Логин в хедере должен остаться прежним, т.к. новый логин уже занят")

    def test_change_login_invalid(self):
        self.page.change_login("не корректный логин", constants.authorization_data["password"])
        self.assertTrue(self.page.is_login_error_exists(), "Ожидался вывод контейнера с ошибкой о не корретном логине")

    def test_change_login_success(self):
        new_login = utils.generate_unique_login()
        self.page.change_login(new_login, constants.authorization_data["password"])
        self.page.refresh()

        current_login_header = Header.create(self.driver).user_name
        current_login_input = self.page.input_login_text
        self.page.change_login(constants.authorization_data["login"], constants.authorization_data["password"])

        self.assertEqual(current_login_input, new_login,
                         "Логин должен смениться, в инпуте отобжается новый логин")

        self.assertEqual(current_login_header, new_login,
                         "Логин должен смениться, в хедере отобжается новый логин")

    def test_change_email_success(self):
        original_email = self.page.input_email_text
        new_email = utils.generate_unique_email()
        self.page.change_email(new_email, constants.authorization_data["password"])
        self.page.refresh()

        current_email_input = self.page.input_email_text
        self.page.change_email(original_email, constants.authorization_data["password"])

        self.assertEqual(current_email_input, new_email,
                         "Email должен смениться, в инпуте отобжается новый email")

    def test_change_email_busy(self):
        original_email = self.page.input_email_text
        self.page.change_email("busylogin@busylogin", constants.authorization_data["password"])
        self.page.refresh()
        self.assertEqual(self.page.input_email_text, original_email,
                         "Email должен остаться прежним, т.к. новый email уже занят")

    def test_email_invalid(self):
        self.page.change_email("invalid_email", constants.authorization_data["password"])
        self.assertTrue(self.page.is_input_error_exists(), "Ожидался вывод сообщения о не корректном email")

    def test_password_change_success(self):
        new_password = utils.generate_unique_password()
        self.page.change_password(new_password=new_password,
                                  new_password_repeat=new_password,
                                  old_password=constants.authorization_data["password"])
        self.login_page.logout()
        self.login_page.open()
        self.login_page.login(constants.authorization_data["login"], new_password)
        self.login_page.wait_for_redirect()
        self.assertEqual(constants.authorization_data["login"], Header.create(self.driver).user_name,
                         "Ожидался успешный вход в аккаунт по новому паролю")
        self.page.open()
        self.page.change_password(new_password=constants.authorization_data["password"],
                                  new_password_repeat=constants.authorization_data["password"],
                                  old_password=new_password)

    def test_password_change_mismatch(self):
        self.page.change_password(new_password="password1234",
                                  new_password_repeat="password1231",
                                  old_password=constants.authorization_data["password"])
        self.assertTrue(self.page.is_input_error_exists(), "Ожидался вывод сообщения о не корректной паре паролей")

    def test_password_invalid(self):
        self.page.change_password(new_password="1234password",
                                  new_password_repeat="1234password",
                                  old_password=constants.authorization_data["password"])
        self.assertTrue(self.page.is_input_error_exists(), "Ожидался вывод сообщения о не корректном пароле")

from pageobjects.pages.profile import ProfilePage
from pageobjects.components.header import Header
from tests.base_test_case import TestCaseWithLoginLogout
import utils.constants as constants
import utils.utils as utils


class LoginTest(TestCaseWithLoginLogout):
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

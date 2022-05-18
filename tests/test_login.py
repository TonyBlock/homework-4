from pageobjects.pages.login import LoginPage
from pageobjects.components.header import Header
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data


class LoginTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)

    def test_login(self):
        self.page.open()
        self.page.login(authorization_data["login"], authorization_data["password"])
        self.page.wait_for_redirect()
        self.assertEqual(authorization_data["login"], Header.create(self.driver).user_name)

    def tearDown(self):
        self.page.logout()
        super().tearDown()


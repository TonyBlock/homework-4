from pageobjects.pages.profile import ProfilePage
from pageobjects.pages.login import LoginPage
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data


class LoginTest(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.open()
        self.loginPage.login(authorization_data["login"], authorization_data["password"])
        self.loginPage.wait_for_redirect()

        self.page = ProfilePage(self.driver)
        self.page.open()

    def test_correct_avatar_change(self):
        # time.sleep(3)
        self.page.upload_avatar("data/bread.png")
        # time.sleep(5)

    def tearDown(self):
        self.loginPage.logout()
        super().tearDown()

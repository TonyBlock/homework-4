import datetime
from pageobjects.login_page import LoginPage
from tests.base_test_case import BaseTestCase


class SimpleTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)

    def test_login(self):
        self.page.open()
        print(self.page.btn_enter.text)
        self.assertEqual(1, 1, "1==1")

    def test_two(self):
        self.assertEqual(2, 2, "2==2")

    def tearDown(self):
        super().tearDown()

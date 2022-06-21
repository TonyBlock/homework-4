from pageobjects.pages.profile import ProfilePage
from tests.base_test_case import TestCaseWithLoginLogout


class ProfileAvatarTest(TestCaseWithLoginLogout):
    def setUp(self):
        super().setUp()

        self.page = ProfilePage(self.driver)
        self.page.open()

    def test_correct_avatar_change(self):
        self.page.upload_avatar("data/bread.png")
        self.assertFalse(self.page.is_avatar_error_exists(), "Проверка загруки корректного аватара")

    def test_incorrect_avatar_change(self):
        self.page.upload_avatar("data/2hoursLater.png")
        self.assertTrue(self.page.is_avatar_error_exists(), "Проверка загруки не корректного "
                                                            "аватара (размер более 500 кб)")

from pageobjects.pages.board import BoardPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.components.modal_settings import ModalSettings
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data


class ModalWindowSettings(BaseTestCase):
    def setUp(self):
        super().setUp()
        super().login()
        self.page = BoardPage(self.driver)
        self.page.open()

    def test_modal_window_settings_open(self):
        self.page.btn_modal_window_settings.click()
        self.modal_settings = ModalSettings.create(self.driver)
        self.modal_settings.locate()

    def test_modal_window_settings_failed_creation(self):
        self.page.btn_modal_window_settings.click()
        self.modal_settings = ModalSettings.create(self.driver)
        self.modal_settings.fill_modal("")
        self.assertEqual(self.modal_settings.get_error_text(), "Название доски слишком короткое")
        self.modal_settings.close()

    def test_modal_window_settings_rename(self):
        self.page.btn_modal_window_settings.click()
        self.modal_settings = ModalSettings.create(self.driver)
        self.modal_settings.fill_modal("test")
        self.assertEqual("test", self.page.board_name)

        # cleanup
        self.page.btn_modal_window_settings.click()
        self.modal_settings = ModalSettings.create(self.driver)
        self.modal_settings.fill_modal("board_name")

    def test_modal_window_settings_reject_deletion(self):
        self.page.btn_modal_window_settings.click()
        self.modal_settings = ModalSettings.create(self.driver)
        self.modal_settings.delete_board(True)
        WebDriverWait(self.driver, 20).until_not(EC.presence_of_element_located("boardSettingPopUpDeleteConfirmBtnId")
        self.modal_settings.close()

    def tearDown(self):
        super().tearDown()

from pageobjects.pages.board import BoardPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.components.modal_tags import ModalTags
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data


class ModalWindowTags(BaseTestCase):
    def setUp(self):
        super().setUp()
        super().login()
        self.page = BoardPage(self.driver)
        self.page.open()

    def test_modal_window_tags_open(self):
        self.page.btn_modal_window_tags.click()
        self.modal_tags = ModalTags.create(self.driver)
        self.modal_tags.locate()

    def test_modal_window_tags_failed_creation(self):
        self.page.btn_modal_window_tags.click()
        self.modal_tags = ModalTags.create(self.driver)
        self.modal_tags.fill_modal("")
        self.assertEqual(self.modal_tags.get_error_text(), "Название доски слишком короткое")
        self.modal_tags.close()

    def test_modal_window_tags_rename(self):
        self.page.btn_modal_window_tags.click()
        self.modal_tags = ModalTags.create(self.driver)
        self.modal_tags.fill_modal("test")
        self.assertEqual("test", self.page.board_name)

        # cleanup
        self.page.btn_modal_window_tags.click()
        self.modal_tags = ModalTags.create(self.driver)
        self.modal_tags.fill_modal("board_name")

    def test_modal_window_tags_reject_deletion(self):
        self.page.btn_modal_window_tags.click()
        self.modal_tags = ModalTags.create(self.driver)
        self.modal_tags.delete_board(True)
        WebDriverWait(self.driver, 20).until_not(EC.presence_of_element_located("boardSettingPopUpDeleteConfirmBtnId")
        self.modal_tags.close()

    def tearDown(self):
        super().tearDown()

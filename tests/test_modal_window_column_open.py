from pageobjects.pages.board import BoardPage
from pageobjects.components.modal_column import ModalColumn
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data


class ModalWindowColumnOpen(BaseTestCase):
    def setUp(self):
        super().setUp()
        super().login()
        self.page = BoardPage(self.driver)
        self.page.open()

    def test_modal_window_column_open(self):
        self.page.btn_modal_window_column.click()
        self.modal_column = ModalColumn.create(self.driver)
        self.modal_column.locate()

    def test_modal_window_column_failed_creation(self):
        self.page.btn_modal_window_column.click()
        self.modal_column = ModalColumn.create(self.driver)
        self.modal_column.fill_modal("")
        self.assertEqual(self.modal_column.get_error_text(), "Название колонки слишком короткое")
        self.modal_column.close()
        self.page.find_column_by_name("", True)

    def test_modal_window_column_create(self):
        self.page.btn_modal_window_column.click()
        self.modal_column = ModalColumn.create(self.driver)
        self.modal_column.fill_modal("test")
        self.page.find_column_by_name("test")        

    def tearDown(self):
        super().tearDown()

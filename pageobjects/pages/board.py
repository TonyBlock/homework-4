from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.base.page import Page
from pageobjects.components.modal_column import ModalColumn


class BoardPage(Page):

    @property
    def board_name(self):
        return self.driver.find_element(by=By.ID, value="board-header__name").text

    @property
    def btn_modal_window_column(self):
        return self.driver.find_element(by=By.ID, value="showCreateCardListPopUpId")

    @property
    def btn_modal_window_settings(self):
        return self.driver.find_element(by=By.ID, value="showBoardSettingPopUpId")

    def find_column_by_name(self, name, reverse = False):
        if (reverse):
          return WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element("column__title", name))
        else:
          return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element("column__title", name))


    def open(self, *args, **kwargs):
        super().open("board/38")

from pageobjects.base import component
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalSettings(component.Component):
    @staticmethod
    def create(driver):
        modal = ModalSettings(driver, "div.popup-content_settings")
        modal.locate()
        return modal

    @property
    def input_name(self):
        return self.driver.find_element(by=By.ID, value="boardSettingPopUpTitleId")

    @property
    def btn_create(self):
        return self.driver.find_element(by=By.ID, value="boardSettingPopUpSaveBtnId")

    @property
    def btn_cross(self):
        return self.driver.find_element(by=By.ID, value="boardSettingPopUpCloseId")

    @property
    def btn_delete(self):
        return self.driver.file_element(by=By.ID, value="boardSettingPopUpDeleteBtnId")

    def close(self):
        self.btn_cross.click()

    def get_error_text(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value="error").text

    def fill_board_name(self, name):
        board_name = self.driver.find_element(by=By.ID, value="boardSettingPopUpTitleId")
        self.board_name.send_keys(name)

    def fill_modal(self, name):
        self.fill_board_name(name)
        self.btn_create.click()

    def delete_board(self, reversed = False):
        self.btn_delete.click()
        if (reversed):
            self.driver.find_element(by=By.ID, value="boardSettingPopUpDeleteRejectBtnId").click()
        else:
            self.driver.find_element(by=By.ID, value="boardSettingPopUpDeleteConfirmBtnId").click()



from pageobjects.base import component
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalColumn(component.Component):
    @staticmethod
    def create(driver):
        modal = ModalColumn(driver, "div.popup-content_card-list")
        modal.locate()
        return modal

    @property
    def input_name(self):
        return self.driver.find_element(by=By.NAME, value="cardlist-name")

    @property
    def btn_create(self):
        return self.driver.find_element(by=By.ID, value="cardListPopUpCreateBtnId")

    @property
    def btn_cross(self):
        return self.driver.find_element(by=By.ID, value="cardListPopUpCloseId")

    def close(self):
        self.btn_cross.click()

    def get_error_text(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value="error").text

    def fill_column_name(self, name):
        cardlist_name = self.driver.find_element(by=By.NAME, value="cardlist-name")
        self.cardlist_name.send_keys(name)

    def fill_modal(self, name):
        self.fill_column_name(name)
        self.btn_create.click()

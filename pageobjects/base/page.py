from urllib.parse import urljoin
import selenium.webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Page(object):
    BASE_URL = 'https://brrrello.ru/'

    def __init__(self, driver):
        self.driver = driver  # type: selenium.webdriver.Remote

    def open(self, path):
        url = urljoin(self.BASE_URL, path)
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()

    def is_element_exists(self, id_selector):
        try:
            self.driver.find_element(by=By.ID, value=id_selector)
        except NoSuchElementException:
            return False
        return True

from urllib.parse import urljoin
import selenium.webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def is_element_exists(self, selector, by=By.ID):
        try:
            self.driver.find_element(by=by, value=selector)
        except NoSuchElementException:
            return False
        return True

    def wait_last_event(self):
        # Хотя для find_element задан implicitly wait, это не помогает из-за особенностей фронтенда.
        # После того как мы нашли элемент, страница может перерисоваться (не предсказуемо) и
        # элемент станет не валиден, от части это решается с помощью декоратора @retry, но в случае
        # с вводом в input'ы формы, эта проблема скорее всего вообще не решает (т.к. скорее всего
        # содержимое инпутов сбрасывается из-за перерисовки уже после того, как мы  в тесте нажимаем
        # кнопку "отправить форму")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "root")))
        self.driver.execute_script("""setTimeout(() => {
            const marker = document.createElement("div")
            marker.id="selenium-marker"
            document.getElementsByTagName("body")[0].appendChild(marker)
        }, 3000)""")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "selenium-marker")))

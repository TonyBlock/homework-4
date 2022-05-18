from urllib.parse import urljoin
import selenium.webdriver


class Page(object):
    BASE_URL = 'https://brrrello.ru/'

    def __init__(self, driver):
        self.driver = driver  # type: selenium.webdriver.Remote

    def open(self, path):
        url = urljoin(self.BASE_URL, path)
        self.driver.get(url)
        self.driver.maximize_window()

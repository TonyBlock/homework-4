import selenium.webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Component(object):
    """
    Базовый класс, для поиска корневого элемента на странице - например, модального окна.
    """

    def __init__(self, driver, css_selector):
        self.driver = driver  # type: selenium.webdriver.Remote
        self.container_selector = css_selector
        self.component = None  # type: WebElement

    def locate(self):
        self.component = WebDriverWait(self.driver, 20)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, self.container_selector)))

    @property
    def is_located(self):
        return self.component is not None

import queue
import unittest
import subprocess
import os
from selenium import webdriver
import utils.utils as utils
import utils.constants as constants
from selenium.webdriver.remote.file_detector import LocalFileDetector
from pageobjects.pages.login import LoginPage


class BaseTestCase(unittest.TestCase):
    processes = queue.Queue()
    BROWSER = ""

    @classmethod
    def setUpClass(cls):
        print("Запуск selenium-server", end="...")
        environment = os.environ.copy()
        # В PATH должен быть путь до драйверов
        bin_dir = os.path.join(os.path.abspath(os.getcwd()), "bin")
        environment["PATH"] = "{}:{}".format(bin_dir, environment["PATH"])
        process = subprocess.Popen(["java", "-jar",
                                    os.path.join(bin_dir, constants.selenium_bin_files["server"]),
                                    "standalone", "--host", constants.selenium_server["host"],
                                    "--port", str(constants.selenium_server["port"])], env=environment,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cls.processes.put(process)
        utils.sleep_while_server_not_started(constants.selenium_server["host"],
                                             constants.selenium_server["port"])
        print("  done")

    @classmethod
    def tearDownClass(cls):
        process = cls.processes.get()  # type: subprocess.Popen
        process.kill()
        utils.sleep_while_server_work(constants.selenium_server["host"],
                                      constants.selenium_server["port"])

    def setUp(self):
        self.BROWSER = os.environ.get("BROWSER")
        if self.BROWSER not in constants.browsers.keys():
            raise ValueError("задан не правильный тип браузера")
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}".format(constants.selenium_server["host"],
                                                   constants.selenium_server["port"]),
            options=constants.browsers[self.BROWSER]
        )

        # Максимальное время, которое find_element будет пытаться что-то найти
        self.driver.implicitly_wait(10)
        self.driver.file_detector = LocalFileDetector()

    def tearDown(self):
        self.driver.quit()


class TestCaseWithLoginLogout(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.login_page.login(constants.authorization_data["login"], constants.authorization_data["password"])
        self.login_page.wait_for_redirect()

    def tearDown(self):
        self.login_page.logout()
        super().tearDown()

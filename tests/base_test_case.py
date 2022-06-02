import queue
import unittest
import subprocess
import os
from selenium import webdriver
from pageobjects.pages.login import LoginPage

import utils.utils as utils
import utils.constants as constants


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

    def login(self):
        login = LoginPage(self.driver)
        login.open()
        login.login(constants.authorization_data["login"], constants.authorization_data["password"])
        # Иначе оно опять открывает login
        self.driver.get(login.BASE_URL)

    def tearDown(self):
        self.driver.quit()

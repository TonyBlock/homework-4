import queue
import unittest
import subprocess
import os

from selenium import webdriver

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
                                    "standalone", "--host", "127.0.0.1",
                                    "--port", "4444"], env=environment,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cls.processes.put(process)
        # time.sleep(2)
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
            command_executor="http://127.0.0.1:4444",
            options=constants.browsers[self.BROWSER]
        )

        # Максимальное время, которое find_element будет пытаться что-то найти
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

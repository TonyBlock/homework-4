#!/usr/bin/python3
import unittest
import sys
import utils.utils as utils
from tests.test_login import LoginTest
from tests.test_modal_window_column_open import ModalWindowColumnOpen
from tests.test_modal_window_settings import ModalWindowSettings
from tests.test_modal_window_tags import ModalWindowTags


def run_tests(dir, pattern="test*.py"):
    tests = unittest.TestLoader().discover(start_dir=dir, pattern=pattern)
    unittest.TextTestRunner().run(tests)


if __name__ == '__main__':
    utils.download_selenium(utils.urls_by_os(), force=False)

    if len(sys.argv) == 1:
        run_tests("tests")
    elif len(sys.argv) == 3 and sys.argv[1] == "--pattern":
        print("Запуск тестов удовлетворяющих паттерну: " + sys.argv[2])
        run_tests(".", sys.argv[2])
    else:
        print("Запуск тестов: "
              "\n\trun_tests.py --pattern test_*.py - запуск тестов, удовлетворяющих паттерну"
              "\n\trun_tests.py - запуск всех тестов")


def load_tests(loader, tests, pattern):
    """
    Функция подсказывает unittest какие тесты должны быть выполнены при запуске модуля через
    python -m unittest run_tests.py
    """
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(LoginTest))
    suite.addTest(unittest.makeSuite(ModalWindowColumnOpen))
    suite.addTest(unittest.makeSuite(ModalWindowSettings))
    suite.addTest(unittest.makeSuite(ModalWindowTags))
    # suite.addTest(unittest.makeSuite(SecondTestCase))
    return suite


if __name__ == "run_tests":
    print("Запуск через python -m unittest run_tests.py")
    utils.download_selenium(utils.urls_by_os(), force=True)

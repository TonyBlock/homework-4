from selenium import webdriver
import os

selenium_bin_urls = {
    # MacOS для ARM
    "Darwin": {
        "server": "https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.1.0/selenium-server-4.1.4.jar",
        "geckodriver": "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/"
                       "geckodriver-v0.31.0-macos-aarch64.tar.gz",
        "chromedriver": "https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_mac64.zip"

    },
    "Linux": {
        "server": "https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.1.0/selenium-server-4.1.4.jar",
        "geckodriver": "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/"
                       "geckodriver-v0.31.0-linux64.tar.gz",
        "chromedriver": "https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip"
    }
}

selenium_server = {
    "host": "127.0.0.1",
    "port": 4444
}

selenium_bin_files = {
    "server": "selenium-server.jar",
    "geckodriver": "geckodriver",
    "chromedriver": "chromedriver"
}


def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    return options


browsers = {
    "CHROME": get_chrome_options(),
    "FIREFOX": webdriver.FirefoxOptions()
}

authorization_data = {
    "login": os.getenv("LOGIN"),
    "password": os.getenv("PASSWORD")
}

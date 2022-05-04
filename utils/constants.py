from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


selenium_bin_urls = {
    # MacOS для ARM
    "Darwin": {
        "server": "https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.1.0/selenium-server-4.1.4.jar",
        "geckodriver": "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/"
                       "geckodriver-v0.31.0-macos-aarch64.tar.gz",
        "chromedriver": "https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_mac64_m1.zip"

    },
    "Linux": {
        "server": "https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.1.0/selenium-server-4.1.4.jar",
        "geckodriver": "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/"
                       "geckodriver-v0.31.0-linux64.tar.gz",
        "chromedriver": "https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip"
    }
}

selenium_bin_files = {
    "server": "selenium-server.jar",
    "geckodriver": "geckodriver",
    "chromedriver": "chromedriver"
}

browsers = {
    "CHROME": webdriver.ChromeOptions(),
    "FIREFOX": webdriver.FirefoxOptions()
}

authorization_data = {
    "login": None,
    "password": None
}

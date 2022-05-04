import stat

import wget
import os
import utils.constants as constants
import platform
import shutil
import tarfile
import zipfile


def is_selenium_installed():
    if os.path.isdir("bin") is False:
        return False
    if os.path.exists(os.path.join("bin", constants.selenium_bin_files["server"])) \
            and os.path.exists(os.path.join("bin", constants.selenium_bin_files["geckodriver"])) \
            and os.path.exists(os.path.join("bin", constants.selenium_bin_files["chromedriver"])):
        return True
    return False


def urls_by_os():
    system_name = platform.system()
    if system_name in constants.selenium_bin_urls.keys():
        return constants.selenium_bin_urls[system_name]
    raise ValueError("не найдены url'ы selenium для ОС \"{}\"".format(system_name))


def download_selenium(urls, force=False):
    """
    Загружаем бинарники selenium и драйверы браузеров
    :param urls: словарь с url'ами для загрузки
    :param force: нужно ли принудительно перезагрузить файлы
    """
    if is_selenium_installed() is True and force is False:
        return

    shutil.rmtree("bin", ignore_errors=True)
    os.mkdir("bin")

    print("Загрузка selenium-server...")
    wget.download(urls["server"], os.path.join("bin", constants.selenium_bin_files["server"]))

    print("Загрузка geckodriver...")
    gecko_archive_name = "{}.tar.gz".format(constants.selenium_bin_files["geckodriver"])
    wget.download(urls["geckodriver"], os.path.join("bin", gecko_archive_name))
    file = tarfile.open(os.path.join("bin", gecko_archive_name))
    file.extractall("bin")
    file.close()
    os.remove(os.path.join("bin", gecko_archive_name))

    print("Загрузка chromedriver...")
    chrome_archive_name = "{}.zip".format(constants.selenium_bin_files["chromedriver"])
    wget.download(urls["chromedriver"], os.path.join("bin", chrome_archive_name))
    with zipfile.ZipFile(os.path.join("bin", chrome_archive_name)) as file:
        file.extractall('bin')
    os.remove(os.path.join("bin", chrome_archive_name))
    os.chmod(os.path.join("bin", constants.selenium_bin_files["chromedriver"]), stat.S_IEXEC)

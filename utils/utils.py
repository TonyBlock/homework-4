import stat
import wget
import os
import utils.constants as constants
import platform
import shutil
import tarfile
import zipfile
import time
import socket
import uuid


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


def sleep_while_server_not_started(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while sock.connect_ex((host, port)) != 0:
        time.sleep(0.25)
    sock.close()


def sleep_while_server_work(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while sock.connect_ex((host, port)) == 0:
        sock.close()
        time.sleep(0.25)
    sock.close()


def generate_unique_string():
    return str(uuid.uuid1()).replace("-", "")


def generate_unique_password():
    return "x{}".format(generate_unique_string()[:24])


def generate_unique_login():
    return generate_unique_string()[:20]


def generate_unique_email():
    return generate_unique_string() + "@gmail.com"

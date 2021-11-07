import sys
import random
import string
import dataclasses

from typing import Union
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_operating_system() -> str:
    return sys.platform


def get_path_webdriver() -> str:
    system: str = get_operating_system()
    if system == "linux":
        path = "driver/chromedriver"
    else:
        raise OSError(f"Operating system {system} not supported")

    return path


def set_user_agent() -> Options:
    options = Options()
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--start-maximized")
    return options


def get_webdriver() -> webdriver.Chrome:
    options: Options = set_user_agent()
    path_driver: str = get_path_webdriver()
    webdriver_ = webdriver.Chrome(executable_path=path_driver, chrome_options=options)
    return webdriver_


def generate_random_string(size=10, chars=string.ascii_uppercase + string.digits + string.punctuation):
    random_str = ''.join(random.choice(chars) for x in range(size))
    return random_str.lower()+'A'

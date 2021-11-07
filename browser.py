import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import utils
from main import ClassName


class WebWorker:
    def __init__(self, driver: webdriver.Chrome) -> None:
        self.__driver = driver

    def go_to_url(self, url: str) -> None:
        self.__driver.get(url)

    def _check_element(self, timeout: int, element: tuple[By, str]) -> None:
        # Проверка на наличие html элемента
        WebDriverWait(self.__driver, timeout).until_not(
            EC.invisibility_of_element(element)
        )

    def _register(self, register_info: tuple[By, str]):
        self._check_element(15, register_info)
        return self.__driver.find_element(*register_info)

    def register(self, class_name: ClassName, logins: list[str]) -> tuple:
        password = []
        time.sleep(3)
        for idx, login in enumerate(logins):
            print(logins[idx])
            self._register((By.XPATH, f"//input[@id='{class_name.email}']")).send_keys(logins[idx])
            time.sleep(3)
            password.append(utils.generate_random_string())
            print(password[idx])
            self._register((By.XPATH, f"//input[@id='{class_name.password}']")).send_keys(password[idx])
            time.sleep(3)
            self._register((By.XPATH, f"//input[@id='{class_name.passwordConfirm}']")).send_keys(password[idx])
            time.sleep(3)
            self._register((By.XPATH, f"//button[text()='{class_name.sing_up}']")).click()
            time.sleep(15)
            self.__driver.execute_script("window.history.go(-1)")

        return logins, password

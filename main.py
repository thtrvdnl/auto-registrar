import dataclasses

import utils
import browser

from loader import process_file_email, write_file_login_and_password

URL = "https://www.faze.app/refer/OEWMCTDA"
FILE = "/home/thtrvdnl/apps/auto-registrar/email.xlsx"


@dataclasses.dataclass(frozen=True)
class ClassName:
    email: str = "email"
    password: str = "password"
    passwordConfirm: str = "passwordConfirm"
    sing_up: str = "Sign Up"


if __name__ == '__main__':
    logins = process_file_email(FILE, ["login"])

    webdriver = utils.get_webdriver()
    webdriver = browser.WebWorker(webdriver)

    webdriver.go_to_url(URL)
    logins, password = webdriver.register(class_name=ClassName(), logins=logins[0])

    write_file_login_and_password(logins, password)

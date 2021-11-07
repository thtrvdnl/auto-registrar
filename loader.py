import os
import pandas

from exceptions import NoFile


def process_file_email(path: str, cols: list[str]) -> list[list[str]]:
    if not os.path.isfile(path):
        raise NoFile("No such file exists")
    df = pandas.read_excel(path, usecols=cols)
    return [df[col].tolist() for col in cols]


def write_file_login_and_password(logins: list[str], password: list[str]) -> None:
    register_info = {"login": logins, "password": password}
    df = pandas.DataFrame(register_info, columns=['login', 'password'])
    df.to_excel("email_out.xlsx")

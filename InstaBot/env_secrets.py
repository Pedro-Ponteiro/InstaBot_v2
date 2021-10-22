import getpass
from typing import Tuple


def get_login_pwd() -> Tuple[str, str]:
    print("Credentials")
    return (input("Username: "), getpass.getpass("Password: "))

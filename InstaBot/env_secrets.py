import getpass
from typing import List, Tuple


def get_login_pwd() -> Tuple[str, str]:
    print("Credentials")
    return (input("Username: "), getpass.getpass("Password: "))


def get_dont_like() -> List[str]:

    words = [
        "hot",
        "india",
        "girl",
        "guy",
    ]

    return words + [w.title() for w in words] + [w.upper() for w in words]

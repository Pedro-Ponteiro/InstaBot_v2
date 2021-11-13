import json
import os
from typing import Dict, List, Tuple, Union


def get_secrets_json() -> Dict[str, Union[str, List[str]]]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(os.path.join(dir_path, "secrets.production.json"), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(
            'Didnt find file "secrets.production.json"'
            + 'Using "secrets.example.json" instead'
        )
        with open(os.path.join(dir_path, "secrets.example.json"), "r") as f:
            return json.load(f)


def get_login_pwd() -> Tuple[str, str]:

    filejson = get_secrets_json()

    print(f'Logging with user {filejson["username"]}')
    return filejson["username"], filejson["password"]


def get_tags() -> List[str]:

    filejson = get_secrets_json()

    return filejson["tags"]


def get_dont_like() -> List[str]:
    filejson = get_secrets_json()

    words = filejson.get("dont_like", None)

    return words + [w.title() for w in words] + [w.upper() for w in words]

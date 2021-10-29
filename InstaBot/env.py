import json
import os
from typing import Dict, List, Tuple, Union


def get_secrets_json() -> Dict[str, Union[str, List[str]]]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        filejson = json.load(open(os.path.join(dir_path, "secrets.dev.json"), "r"))
    except FileNotFoundError:
        print('Didnt find file "secrets.dev.json". Using "secrets.prod.json" instead')
        filejson = json.load(open(os.path.join(dir_path, "secrets.prod.json"), "r"))

    return filejson


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

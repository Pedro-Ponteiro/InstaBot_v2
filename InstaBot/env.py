import json
import os
from typing import Dict, List, Tuple, Union


def get_secrets_json() -> Dict[str, Union[str, List[str]]]:
    """Get secrets (production or example).

    Returns:
        Dict[str, Union[str, List[str]]]: json file as a dict
    """
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
    """Get login and password set at secrets.

    Returns:
        Tuple[str, str]: login and password
    """

    filejson = get_secrets_json()

    print(f'Logging with user {filejson["username"]}')
    return filejson["username"], filejson["password"]


def get_tags() -> List[str]:
    """Get Tags for liking.

    Returns:
        List[str]: list of tags
    """

    filejson = get_secrets_json()

    return filejson["tags"]


def get_dont_like() -> List[str]:
    """Get words that, if encountered at the post description,
        the driver skips it

    Returns:
        List[str]: list of "dont_like_if_contains" words
    """
    filejson = get_secrets_json()

    words = filejson["dont_like"]

    return words + [w.title() for w in words] + [w.upper() for w in words]

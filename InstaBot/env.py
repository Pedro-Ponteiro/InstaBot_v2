from typing import List


def get_tags() -> List[str]:
    return [
        "programming",
        "empreendedorismo",
        "entrepreneurship",
        "motivation",
        "startup",
    ]


def get_dont_like() -> List[str]:

    words = [
        "hot",
        "india",
        "girl",
        "guy",
    ]

    return words + [w.title() for w in words] + [w.upper() for w in words]


def get_mandatory_words() -> List[str]:

    words = [
        "machinelearning",
        "datascience",
        "machine learning",
        "data science",
        "programming",
        "software",
        "python",
        "statistics",
        "empreendedorismo",
    ]
    words = words + [w.title() for w in words]

    return words

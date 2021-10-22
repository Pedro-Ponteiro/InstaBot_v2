from typing import List


def get_tags() -> List[str]:
    return [
        "programming",
        "empreendedorismo",
        "entrepreneurship",
        "motivation",
        "startup",
    ]


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

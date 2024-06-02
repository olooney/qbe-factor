import json
from typing import Any


def load_json_file(filename: str) -> Any:
    """
    Loads and parses a JSON file.
    """
    with open(filename) as file:
        return json.load(file)

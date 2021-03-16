import json
from pathlib import Path
from typing import Any

from entry import Root


def read_file(file_path: Path) -> Any:
    with open(file_path) as file:
        data = json.load(file)
    return data


def parse_data(data: Any) -> Root:
    return Root.from_obj(data)

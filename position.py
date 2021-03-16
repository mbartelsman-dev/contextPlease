from enum import Enum, auto
from typing import Optional


class Position(Enum):
    TOP = auto()
    BOTTOM = auto()

    @staticmethod
    def from_str(pos: str) -> Optional['Position']:
        if pos is None:
            return None
        if pos.lower().strip() == "top":
            return Position.TOP
        if pos.lower().strip() == "bottom":
            return Position.TOP

        Exception("Position argument invalid. Must be one of 'Top' or 'Bottom'.")

    def to_str(self):
        if self == Position.TOP:
            return "Top"
        if self == Position.BOTTOM:
            return "Bottom"

from pathlib import PurePath
from sys import stderr
from typing import Optional, Any

import entry
from position import Position


class Entry(object):
    name: str
    text: Optional[str]
    icon: Optional[PurePath]
    pos: Optional[Position]

    def __init__(
            self,
            name: str = "Entry",
            text: Optional[str] = None,
            icon: Optional[str] = None,
            pos: Optional[str] = None,
            **kwargs
    ):
        super(Entry, self).__init__()
        self.name = name
        self.icon = PurePath(icon)
        self.pos = Position.from_str(pos)

        if text is None:
            self.text = name
        else:
            self.text = text

    @staticmethod
    def from_obj(obj: Any) -> 'Entry':

        if "cmd" in obj and "entries" in obj:
            raise Exception("Ambiguous Entry. Entries can only have one of 'cmd' and 'entries', not both.")

        elif "entries" in obj:
            res = entry.Menu.from_obj(obj)

        elif "cmd" in obj:
            res = entry.Item.from_obj(obj)

        else:
            stderr.write("Ambiguous entry. Defaulting to Item")
            res = entry.Item.from_obj(obj)

        return res

    def build_reg(self):
        pass

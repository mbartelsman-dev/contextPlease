from pathlib import PurePath
from sys import stderr
from typing import Optional, Any, Union

from context_please import entry
from context_please.position import Position
from context_please.registry_handle import RegistryHandle


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

    def build_registry_handle(self, path: Union[str, list[str]]) -> RegistryHandle:
        entries = {"MUIVerb": self.text}

        if self.icon is not None:
            entries["Icon"] = self.icon

        if self.pos is not None:
            entries["Position"] = self.pos

        handle = RegistryHandle(
            path=path,
            entries=entries,
            subkeys=[]
        )

        return handle

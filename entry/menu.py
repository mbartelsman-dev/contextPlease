from typing import Optional

import entry


class Menu(entry.Entry):
    entries: list[entry.Entry]

    def __init__(
            self,
            name: str = "Entry",
            text: Optional[str] = None,
            icon: Optional[str] = None,
            pos: Optional[str] = None,
            entries: Optional[list[entry.Entry]] = None,
            **kwargs
    ):
        super().__init__(name=name, text=text, icon=icon, pos=pos, **kwargs)
        if entries is None:
            self.entries = []
        else:
            self.entries = entries

    @staticmethod
    def from_obj(obj: dict) -> 'Menu':

        entries = []
        for e in obj.pop("entries"):
            entries.append(entry.Entry.from_obj(e))

        if "entries" in obj:
            raise Exception("obj should not have entries at this point. Investigate.")

        return Menu(entries=entries, **obj)

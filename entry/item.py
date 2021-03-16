from typing import Optional, Any

import entry


class Item(entry.Entry):
    cmd: str

    def __init__(
            self,
            name: str = "Entry",
            text: Optional[str] = None,
            icon: Optional[str] = None,
            pos: Optional[str] = None,
            cmd: str = "",
            **kwargs
    ):
        super().__init__(name=name, text=text, icon=icon, pos=pos, **kwargs)
        self.cmd = cmd

    @staticmethod
    def from_obj(obj: Any) -> 'Item':
        return Item(**obj)

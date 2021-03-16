from typing import Optional, Any

import entry
from menu_handle import MenuHandle, CommandHandle


class RootItem(entry.Root, entry.Item):
    def __init__(
            self,
            name: str = "Entry",
            text: Optional[str] = None,
            icon: Optional[str] = None,
            pos: Optional[str] = None,
            cmd: str = "",
            target: Optional[str] = None,
            is_ext: bool = False,
            **kwargs
    ):
        entry.Root.__init__(self, target=target, is_ext=is_ext, **kwargs)
        entry.Item.__init__(self, name=name, text=text, icon=icon, pos=pos, cmd=cmd, **kwargs)

    @staticmethod
    def from_obj(obj: Any) -> 'RootItem':
        return RootItem(**obj)

    def build_hkey(self):
        entries = {}

        if self.icon is not None:
            entries["Icon"] = self.icon
        if self.pos is not None:
            entries["Position"] = self.pos

        hkey = MenuHandle(
            path=self.target.to_path() + "\\shell",
            name=self.name,
            default=self.text,
            entries=entries,
            subkeys=[]
        )

        hkey.subkeys.append(
            CommandHandle(
                hkey,
                command=self.cmd
            )
        )

        return hkey

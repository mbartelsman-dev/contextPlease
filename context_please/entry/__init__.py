from pathlib import PurePath
from sys import stderr
from typing import Any, Optional, Union

from context_please.position import Position
from context_please.registry_handle import RegistryHandle


class Entry(object):
    name: str
    text: Optional[str]
    icon: Optional[str] = None
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
        self.pos = Position.from_str(pos)

        if icon is not None:
            self.icon = icon

        if text is None:
            self.text = name
        else:
            self.text = text

    @staticmethod
    def from_obj(obj: Any) -> 'Entry':

        if "cmd" in obj and "entries" in obj:
            raise Exception("Ambiguous Entry. Entries can only have one of 'cmd' and 'entries', not both.")

        elif "entries" in obj:

            res = Menu.from_obj(obj)

        elif "cmd" in obj:
            res = Item.from_obj(obj)

        else:
            stderr.write("Ambiguous entry. Defaulting to Item")
            res = Item.from_obj(obj)

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


class Item(Entry):
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

    def build_registry_handle(self, path: Union[str, list[str]]) -> RegistryHandle:
        handle = super(Item, self).build_registry_handle(path)
        handle.add_command(self.cmd)

        return handle


class Menu(Entry):
    entries: list[Entry] = []

    def __init__(
            self,
            name: str = "Entry",
            text: Optional[str] = None,
            icon: Optional[str] = None,
            pos: Optional[str] = None,
            entries: Optional[list[Entry]] = None,
            **kwargs
    ):
        super().__init__(name=name, text=text, icon=icon, pos=pos, **kwargs)
        if entries is not None:
            self.entries = entries

    @staticmethod
    def from_obj(obj: dict) -> 'Menu':

        entries = []
        for e in obj.pop("entries"):
            entries.append(Entry.from_obj(e))

        return Menu(entries=entries, **obj)

    def build_registry_handle(self, path: Union[str, list[str]]) -> RegistryHandle:
        handle = super(Menu, self).build_registry_handle(path)
        handle.entries["subcommands"] = ""

        for e in self.entries:
            sub_path: list[str] = [handle.path, "shell", e.name]
            subkey = e.build_registry_handle(sub_path)
            handle.subkeys.append(subkey)

        return handle


class Root(object):
    target: str = "*"
    is_ext: bool

    def __init__(
            self,
            target: Optional[str] = None,
            is_ext: bool = False,
            **kwargs
    ):
        super(Root, self).__init__()
        if target is not None:
            self.target = target

        self.is_ext = is_ext

    @staticmethod
    def from_obj(obj: Any) -> 'Root':
        res: Root

        if "cmd" in obj and "entries" in obj:
            raise Exception("Ambiguous Entry. Entries can only have one of 'cmd' and 'entries', not both.")

        elif "entries" in obj:
            res = RootMenu.from_obj(obj)

        elif "cmd" in obj:
            res = RootItem.from_obj(obj)

        else:
            stderr.write("Ambiguous entry. Defaulting to Item")
            res = RootItem.from_obj(obj)

        return res


class RootItem(Root, Item):
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
        Root.__init__(self, target=target, is_ext=is_ext, **kwargs)
        Item.__init__(self, name="ContextPlease." + name, text=text, icon=icon, pos=pos, cmd=cmd, **kwargs)

    @staticmethod
    def from_obj(obj: Any) -> 'RootItem':
        return RootItem(**obj)

    def build_registry_handle(self, path: Union[str, list[str], None] = None) -> RegistryHandle:
        path: list[str] = ["HKEY_CLASSES_ROOT", self.target, "shell", self.name]
        handle = super(RootItem, self).build_registry_handle(path)

        return handle


class RootMenu(Root, Menu):
    def __init__(
            self,
            name: str = "Entry",
            text: Optional[str] = None,
            icon: Optional[str] = None,
            pos: Optional[str] = None,
            entries: Optional[list[Entry]] = None,
            target: Optional[str] = None,
            is_ext: bool = False,
            **kwargs
    ):
        Root.__init__(self, target=target, is_ext=is_ext, **kwargs)
        Menu.__init__(self, name="ContextPlease." + name, text=text, icon=icon, pos=pos, entries=entries, **kwargs)

    @staticmethod
    def from_obj(obj: dict) -> 'RootMenu':
        entries = []
        for e in obj.pop("entries"):
            entries.append(Entry.from_obj(e))

        if "entries" in obj:
            raise Exception("obj should not have entries at this point. Investigate.")

        return RootMenu(entries=entries, **obj)

    def build_registry_handle(self, path: Union[str, list[str], None] = None) -> RegistryHandle:
        path: list[str] = ["HKEY_CLASSES_ROOT", self.target, "shell", self.name]
        return super(RootMenu, self).build_registry_handle(path)

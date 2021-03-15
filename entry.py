from typing import Optional, Any

import target as tgt
from sys import stderr
from target import Target
from position import Position
from pathlib import PurePath


class Entry(object):
    name: str
    icon: Optional[PurePath]
    pos: Optional[Position]

    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            **kwargs
    ):
        super(Entry, self).__init__()
        self.name = name
        self.icon = icon
        self.pos = pos

    @staticmethod
    def build(obj: Any) -> 'Entry':

        if "cmd" in obj and "entries" in obj:
            raise Exception("Ambiguous Entry. Entries can only have one of 'cmd' and 'entries', not both.")

        elif "entries" in obj:
            res = Menu.build(obj)

        elif "cmd" in obj:
            res = Item.build(obj)

        else:
            stderr.write("Ambiguous entry. Defaulting to Item")
            res = Item.build(obj)

        return res


class Root(object):
    target: Target
    is_ext: bool

    def __init__(
            self,
            target: Target = tgt.Everything,
            is_ext: bool = False,
            **kwargs
    ):
        super(Root, self).__init__()
        self.target = target
        self.is_ext = is_ext

    @staticmethod
    def build(obj: Any) -> 'Root':
        res: Root

        if "cmd" in obj and "entries" in obj:
            raise Exception("Ambiguous Entry. Entries can only have one of 'cmd' and 'entries', not both.")

        elif "entries" in obj:
            res = RootMenu.build(obj)

        elif "cmd" in obj:
            res = RootItem.build(obj)

        else:
            stderr.write("Ambiguous entry. Defaulting to Item")
            res = RootItem.build(obj)

        return res


class Item(Entry):
    cmd: str

    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            cmd: str = "",
            **kwargs
    ):
        super().__init__(name=name, icon=icon, pos=pos, **kwargs)
        self.cmd = cmd

    @staticmethod
    def build(obj: Any) -> 'Item':
        return Item(**obj)


class Menu(Entry):
    entries: list[Entry]

    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            entries: list[Entry] = [],
            **kwargs
    ):
        super().__init__(name=name, icon=icon, pos=pos, **kwargs)
        self.entries = entries

    @staticmethod
    def build(obj: dict) -> 'Menu':

        entries = []
        for entry in obj.pop("entries"):
            entries.append(Entry.build(entry))

        if "entries" in obj:
            raise Exception("obj should not have entries at this point. Investigate.")

        return Menu(entries=entries, **obj)


class RootItem(Root, Item):
    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            cmd: str = "",
            target: Target = tgt.Everything,
            is_ext: bool = False,
            **kwargs
    ):
        Root.__init__(self, target=target, is_ext=is_ext, **kwargs)
        Item.__init__(self, name=name, icon=icon, pos=pos, cmd=cmd, **kwargs)

    @staticmethod
    def build(obj: Any) -> 'RootItem':
        return RootItem(**obj)


class RootMenu(Root, Menu):
    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            entries: list[Entry] = [],
            target: Target = tgt.Everything,
            is_ext: bool = False,
            **kwargs
    ):
        Root.__init__(self, target=target, is_ext=is_ext, **kwargs)
        Menu.__init__(self, name=name, icon=icon, pos=pos, entries=entries, **kwargs)

    @staticmethod
    def build(obj: dict) -> 'RootMenu':

        entries = []
        for entry in obj.pop("entries"):
            entries.append(Entry.build(entry))

        if "entries" in obj:
            raise Exception("obj should not have entries at this point. Investigate.")

        return RootMenu(entries=entries, **obj)

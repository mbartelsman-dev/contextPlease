from typing import Optional

import target as tgt
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
    ):
        super(Entry, self).__init__()
        self.name = name
        self.icon = icon
        self.pos = pos


class Root(object):
    target: Target
    is_ext: bool

    def __init__(
            self,
            target: Target = tgt.Everything,
            is_ext: bool = False
    ):
        super(Root, self).__init__()
        self.target = target
        self.is_ext = is_ext


class Item(Entry):
    cmd: str

    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            cmd: str = "",
    ):
        super(Item, self).__init__(name, icon, pos)
        self.cmd = cmd


class Menu(Entry):
    entries: list[Entry]

    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            entries: list[Entry] = [],
    ):
        super(Entry, self).__init__(name, icon, pos)
        self.entries = entries


class RootItem(Root, Item):
    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            cmd: str = "",
            target: Target = tgt.Everything,
            is_ext: bool = False
    ):
        Root.__init__(self, target, is_ext)
        Item.__init__(self, name, icon, pos, cmd)


class RootMenu(Root, Menu):
    def __init__(
            self,
            name: str = "Entry",
            icon: Optional[PurePath] = None,
            pos: Optional[Position] = None,
            entries: list[Entry] = [],
            target: Target = tgt.Everything,
            is_ext: bool = False
    ):
        Root.__init__(self, target, is_ext)
        Menu.__init__(self, name, icon, pos, entries)

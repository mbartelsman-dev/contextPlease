from sys import stderr
from typing import Any, Optional

import entry
from target import Target


class Root(object):
    target: Target
    is_ext: bool

    def __init__(
            self,
            target: Optional[str] = None,
            is_ext: bool = False,
            **kwargs
    ):
        super(Root, self).__init__()
        self.target = Target(target)
        self.is_ext = is_ext

    @staticmethod
    def from_obj(obj: Any) -> 'Root':
        res: Root

        if "cmd" in obj and "entries" in obj:
            raise Exception("Ambiguous Entry. Entries can only have one of 'cmd' and 'entries', not both.")

        elif "entries" in obj:
            res = entry.RootMenu.from_obj(obj)

        elif "cmd" in obj:
            res = entry.RootItem.from_obj(obj)

        else:
            stderr.write("Ambiguous entry. Defaulting to Item")
            res = entry.RootItem.from_obj(obj)

        return res

    def build_reg(self):
        pass

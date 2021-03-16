from typing import Optional


class MenuHandle(object):
    path: str
    name: str
    default: Optional[str]
    entries: dict
    subkeys: list['MenuHandle']

    def __init__(
            self,
            path: str,
            name: str,
            default: Optional[str] = None,
            entries: Optional[dict] = None,
            subkeys: Optional[list['MenuHandle']] = None
    ):
        super(MenuHandle, self).__init__()
        self.path = path
        self.name = name
        self.default = default

        if entries is None:
            self.entries = {}
        else:
            self.entries = entries

        if subkeys is None:
            self.subkeys = []
        else:
            self.subkeys = subkeys


class CommandHandle(MenuHandle):
    def __init__(
            self,
            parent: MenuHandle,
            command: str
    ):
        super(CommandHandle, self).__init__(
            path=parent.path + "\\" + parent.name,
            name="command",
            default=command,
            entries={},
            subkeys=[]
        )

from typing import Optional, Union


class RegistryHandle(object):
    _path: str
    entries: dict = {}
    subkeys: list['RegistryHandle'] = []

    def __init__(
            self,
            path: Union[str, list[str], None] = None,
            entries: Optional[dict] = None,
            subkeys: Optional[list['RegistryHandle']] = None
    ):
        super(RegistryHandle, self).__init__()

        self.path = path

        if entries is not None:
            self.entries = entries

        if subkeys is not None:
            self.subkeys = subkeys

    @property
    def path(self):
        return self.path

    @path.setter
    def path(self, path: Union[str, list[str]]):
        if path is str:
            self._path = path
        else:
            self._path = "\\".join(path)

    def add_command(self, command):
        self.subkeys.append(
            RegistryHandle(
                path=[self.path, "command"],
                entries={
                    "@": command
                }
            )
        )

from pathlib import Path
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
        return self._path

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

    def build_reg_lines(self, file: list[str]) -> list[str]:
        # file.append("; Delete old entry")
        # file.append("-[" + self.path + "]")

        # file.append("; Create new entry")
        file.append("[" + self.path + "]")
        for k, v in self.entries.items():
            print("{" + str(type(k)) + ", " + str(type(v)) + "}")
            print("{" + str(k) + ", " + str(v) + "}\n")
            file.append('"' + k + '"="' + v + '"')

        for k in self.subkeys:
            k.build_reg_lines(file)

        return file

    def write_reg_installer(self, output: Path):
        lines = self.build_reg_lines(["Windows Registry Editor Version 5.00"])

        with open(str(output) + "_install.reg", "w") as file:
            file.write("\n".join(lines))

    def write_reg_uninstaller(self, output: Path):
        lines = ["Windows Registry Editor Version 5.00", "[-" + self.path + "]"]

        with open(str(output) + "_uninstall.reg", "w") as file:
            file.write("\n".join(lines))

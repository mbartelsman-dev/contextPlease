from typing import Optional, Union

from context_please import entry
from context_please.registry_handle import RegistryHandle


class Menu(entry.Entry):
    entries: list[entry.Entry] = []

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
        if entries is not None:
            self.entries = entries

    @staticmethod
    def from_obj(obj: dict) -> 'Menu':

        entries = []
        for e in obj.pop("entries"):
            entries.append(entry.Entry.from_obj(e))

        if "entries" in obj:
            raise Exception("obj should not have entries at this point. Investigate.")

        return Menu(entries=entries, **obj)

    def build_registry_handle(self, path: Union[str, list[str]]) -> RegistryHandle:
        handle = super(Menu, self).build_registry_handle(path)

        for e in self.entries:
            sub_path = [handle.path, "ExtendedSubCommandsKey", "shell"]
            subkey = e.build_registry_handle(sub_path)
            handle.subkeys.append(subkey)

        return handle

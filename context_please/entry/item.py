from typing import Optional, Any, Union

from context_please import entry
from context_please.registry_handle import RegistryHandle


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

    def build_registry_handle(self, path: Union[str, list[str]]) -> RegistryHandle:
        handle = super(Item, self).build_registry_handle(path)
        handle.add_command(self.cmd)

        return handle

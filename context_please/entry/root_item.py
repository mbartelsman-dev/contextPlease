from typing import Optional, Any, Union

from context_please import entry
from context_please.registry_handle import RegistryHandle


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

    def build_registry_handle(self, path: Union[str, list[str], None] = None) -> RegistryHandle:
        path = [self.target.to_path(), "shell", self.name]
        handle = super(RootItem, self).build_registry_handle(path)

        return handle

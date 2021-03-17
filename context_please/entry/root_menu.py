from typing import Optional, Union

from context_please import entry
from context_please.registry_handle import RegistryHandle


class RootMenu(entry.Root, entry.Menu):
    def __init__(
            self,
            name: str = "Entry",
            text: Optional[str] = None,
            icon: Optional[str] = None,
            pos: Optional[str] = None,
            entries: Optional[list[entry.Entry]] = None,
            target: Optional[str] = None,
            is_ext: bool = False,
            **kwargs
    ):
        entry.Root.__init__(self, target=target, is_ext=is_ext, **kwargs)
        entry.Menu.__init__(self, name=name, text=text, icon=icon, pos=pos, entries=entries, **kwargs)

    @staticmethod
    def from_obj(obj: dict) -> 'RootMenu':
        entries = []
        for e in obj.pop("entries"):
            entries.append(entry.Entry.from_obj(e))

        if "entries" in obj:
            raise Exception("obj should not have entries at this point. Investigate.")

        return RootMenu(entries=entries, **obj)

    def build_registry_handle(self, path: Union[str, list[str], None] = None) -> RegistryHandle:
        path = [self.target.to_path(), "shell", self.name]
        return super(RootMenu, self).build_registry_handle(path)

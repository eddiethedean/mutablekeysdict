from typing import Any, ItemsView, Iterator, KeysView, Mapping, ValuesView


class MutableKeysDict:
    def __init__(self, data: Mapping) -> None:
        self.data: dict = dict(data)

    def __getitem__(self, key) -> Any:
        return self.data[key]
    
    def __setitem__(self, key, value) -> None:
        self.data[key] = value

    def __delitem__(self, key) -> None:
        del self.data[key]
    
    def __iter__(self) -> Iterator:
        return iter(self.keys())
    
    def __len__(self) -> int:
        return len(self.keys())
    
    def __contains__(self, value: Any) -> bool:
        return value in self.keys()
    
    def __eq__(self, other) -> bool:
        return self.data == other
    
    def __ne__(self, other) -> bool:
        return self.data != other
    
    def keys(self) -> KeysView:
        return self.data.keys()
    
    def items(self) -> ItemsView:
        return self.data.items()
    
    def values(self) -> ValuesView:
        return self.data.values()
    
    def get(self, key, default=None) -> Any:
        if default is None:
            return self.data.get(key)
        else:
            return self.data.get(key, default)
        
    def pop(self, key) -> Any:
        return self.data.pop(key)
        
    def popitem(self, key) -> tuple:
        return self.popitem(key)
    
    def clear(self) -> None:
        self.data.clear()

    def update(self, other) -> None:
        self.data.update(other)

    def setdefault(self, key, default) -> Any:
        return self.data.setdefault(key, default)
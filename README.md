# MutableKeysDict

A pure python dictionary class that allows the keys to be mutated.

## Description

Use MutableKeysDict if you need a dict that can mutate the keys and still work.
MutableKeysDict keys still need to be hashable. Use dictanykey if you need a dict that can use unhashable keys.

## Getting Started

### Dependencies

* Python>=3.6

### Installing

* pip install mutablekeysdict

### Example Code
```
from mutablekeysdict import MutableKeysDict

class HashableList(list):
    def __hash__(self):
        return hash(tuple(self))

h = HashableList([1, 2, 3])
d = MutableKeysDict({h: 6})
h.append(4)
d[h] -> 6
```

## Authors

Contributors names and contact info

Odos Matthews: odosmatthews@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
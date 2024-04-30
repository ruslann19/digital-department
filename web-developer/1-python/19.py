import re
from typing import Any

class Field:
    def __init__(self):
        self._items = dict()
        return
    
    @staticmethod
    def _convert_location(location):
        if not isinstance(location, (str, tuple)):
            raise TypeError
        location = "".join(map(str, location)).lower()
        if re.fullmatch(r"[a-z]\d+", location) is None and re.fullmatch(r"\d+[a-z]", location) is None:
            raise ValueError
        letter = re.search(r"[a-z]", location).group(0)
        number = int(re.search(r"\d+", location).group(0))
        return frozenset([letter, number])

    def __getitem__(self, location):
        return self._items.get(self._convert_location(location))

    def __setitem__(self, location, value):
        self._items[self._convert_location(location)] = value

    def __delitem__(self, location):
        del self._items[self._convert_location(location)]

    def __contains__(self, location):
        try:
            return self._convert_location(location) in self._items
        except:
            return False

    def __iter__(self):
        return iter(self._items.values())

    def __getattr__(self, location):
        if location in self:
            return self.__getitem__(location)
        return None
    
    def __setattr__(self, location, value):
        try:
            self.__setitem__(location, value)
        except:
            super(Field, self).__setattr__(location, value)
        return
    
    def __delattr__(self, location):
        if location in self:
            del self[location]
        else:
            super(Field, self).__delattr__(location)
        return

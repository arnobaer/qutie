from PyQt5 import QtCore

from .object import Object

__all__ = ['Settings']

class Settings(Object):

    QtClass = QtCore.QSettings

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, key, default=None, type=None):
        if type is not None:
            return self.qt.value(key, default, type)
        return self.qt.value(key, default)

    def setdefault(self, key, default):
        if key not in self.keys():
            self[key] = default
        return self.get(key)

    def keys(self):
        return (key for key in self.qt.allKeys())

    def values(self):
        return (self.get(key) for key in self.keys())

    def items(self):
        return ((key, self.get(key)) for key in self.keys())

    def clear(self):
        self.qt.clear()

    def __getitem__(self, key):
        return self.qt.value(key)

    def __setitem__(self, key, value):
        return self.qt.setValue(key, value)

    def __delitem__(self, key):
        print("DEL")
        self.qt.remove(key)

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return len(self.qt.allKeys())

from PyQt5 import QtCore

__all__ = [
    'Base',
]

class Base:

    QtClass = NotImplemented

    def __init__(self, *args):
        self.__qt = self.QtClass(*args)

    @property
    def qt(self):
        return self.__qt

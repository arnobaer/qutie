from PyQt5 import QtCore, QtGui, QtWidgets

from .base import Base
from .widget import BaseWidget

__all__ = ['Select']

class Select(BaseWidget):

    QtClass = QtWidgets.QComboBox

    def __init__(self, values=None, current=None, readonly=True, changed=None, **kwargs):
        super().__init__(**kwargs)
        if values is not None:
            self.values = values
        if values and current is None:
            current = values[0]
        self.current = current
        self.readonly = readonly

        self.changed = changed
        def changed_event(index):
            if callable(self.changed):
                value = self.values[index]
                self.changed(value)
        self.qt.currentIndexChanged.connect(changed_event)

    @property
    def values(self):
        return [self.qt.itemData(index) for index in range(self.qt.count())]

    @values.setter
    def values(self, values):
        self.clear()
        for value in values:
            self.append(value)

    def clear(self):
        self.qt.clear()

    def append(self, value):
        self.qt.addItem(format(value), value)

    def insert(self, index, value):
        if index < 0:
            index = max(0, len(self) + index)
        self.qt.insertItem(index, format(value), value)

    def remove(self, value):
        self.qt.removeItem(self.qt.findData(value))

    @property
    def current(self):
        return self.qt.itemData(self.qt.currentIndex())

    @current.setter
    def current(self, value):
        index = self.qt.findData(value)
        self.qt.setCurrentIndex(index)

    @property
    def readonly(self):
        return not self.qt.isEditable()

    @readonly.setter
    def readonly(self, value):
        self.qt.setEditable(not value)

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, changed):
        self.__changed = changed

    def __len__(self):
        return self.qt.count()

    def __getitem__(self, index):
        return self.qt.itemData(index)

    def __iter__(self):
        return (self.qt.itemData(index) for index in range(len(self)))
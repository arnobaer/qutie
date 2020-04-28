from PyQt5 import QtCore, QtGui, QtWidgets

from .base import Base
from .widget import BaseWidget

__all__ = ['List']

class List(BaseWidget):

    QtClass = QtWidgets.QListWidget

    def __init__(self, values=None, *, changed=None, **kwargs):
        super().__init__(**kwargs)
        if values is not None:
            self.values = values

        self.changed = changed
        def changed_event(index):
            if callable(self.changed):
                value = self.values[index]
                self.changed(value, index)
        self.qt.currentRowChanged[int].connect(changed_event)

    @property
    def values(self):
        return list(self)

    @values.setter
    def values(self, values):
        self.clear()
        for value in values:
            self.append(value)

    @property
    def current(self):
        item = self.qt.currentItem()
        if item:
            return item.data(ListItem.QtPropertyRole)
        return None

    @current.setter
    def current(self, item):
        index = self.qt.row(item.qt)
        if index < 0:
            raise IndexError(item)
        self.qt.setCurrentItem(item.qt)

    def clear(self):
        self.qt.clear()

    def append(self, item):
        if not isinstance(item, ListItem):
            item = ListItem(item)
        self.qt.addItem(item.qt)
        return item

    def insert(self, index, item):
        if index < 0:
            index = max(0, len(self) + index)
        if not isinstance(item, ListItem):
            item = ListItem(item)
        self.qt.insertItem(index, item.qt)
        return item

    def remove(self, item):
        if item is not None:
            index = self.qt.row(item.qt)
            if index < 0:
                raise IndexError(item)
            self.qt.takeItem(index)

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, changed):
        self.__changed = changed

    def __len__(self):
        return self.qt.count()

    def __getitem__(self, index):
        item = self.qt.item(index)
        if not item:
            raise KeyError(index)
        return item.data(ListItem.QtPropertyRole)

    def __setitem__(self, index, value):
        item = ListItem(value)
        self.qt.takeItem(index)
        self.qt.insertItem(index, item.qt)

    def __iter__(self):
        return (self[row] for row in range(len(self)))

class ListItem(Base):

    QtClass = QtWidgets.QListWidgetItem

    QtPropertyRole = QtCore.Qt.UserRole + 1

    def __init__(self, value, *, color=None, background=None, enabled=True,
                 checked=None, checkable=False, **kwargs):
        super().__init__(**kwargs)
        self.qt.setData(self.QtPropertyRole, self)
        self.__default_foreground = self.qt.foreground()
        self.__default_background = self.qt.background()
        self.value = value
        self.color = color
        self.background = background
        self.enabled = enabled
        self.checkable = checkable
        self.checked = checked

    @property
    def value(self):
        return self.qt.data(QtCore.Qt.UserRole)

    @value.setter
    def value(self, value):
        self.qt.setData(QtCore.Qt.UserRole, value)
        self.qt.setText(format(value))

    @property
    def color(self):
        return self.qt.foreground().color().name()

    @color.setter
    def color(self, value):
        if value is None:
            brush = self.__default_foreground
        else:
            brush = self.qt.foreground()
            brush.setColor(QtGui.QColor(value))
        self.qt.setForeground(brush)

    @property
    def background(self):
        return self.qt.background().color().name()

    @background.setter
    def background(self, value):
        if value is None:
            brush = self.__default_background
        else:
            brush = self.qt.background()
            brush.setStyle(QtCore.Qt.SolidPattern)
            brush.setColor(QtGui.QColor(value))
        self.qt.setBackground(brush)

    @property
    def enabled(self):
        return bool(self.qt.flags() & QtCore.Qt.ItemIsEnabled)

    @enabled.setter
    def enabled(self, value):
        if value:
            self.qt.setFlags(self.qt.flags() | QtCore.Qt.ItemIsEnabled)
        else:
            self.qt.setFlags(self.qt.flags() & ~QtCore.Qt.ItemIsEnabled)

    @property
    def checked(self):
        return self.qt.checkState() == QtCore.Qt.Checked

    @checked.setter
    def checked(self, value):
        if value is None:
            flags = self.qt.flags() & ~QtCore.Qt.ItemIsUserCheckable
            self.qt.setFlags(flags)
        else:
            self.qt.setCheckState(QtCore.Qt.Checked if value else QtCore.Qt.Unchecked)

    @property
    def checkable(self):
        return self.qt.flags() & QtCore.Qt.ItemIsUserCheckable == True

    @checkable.setter
    def checkable(self, value):
        if value:
            flags = self.qt.flags() | QtCore.Qt.ItemIsUserCheckable
            self.qt.setCheckState(self.checked)
        else:
            flags = self.qt.flags() & ~QtCore.Qt.ItemIsUserCheckable
        self.qt.setFlags(flags)

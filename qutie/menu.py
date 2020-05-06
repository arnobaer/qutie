from PyQt5 import QtGui
from PyQt5 import QtWidgets

from .action import Action
from .widget import BaseWidget

__all__ = ['Menu']

class Menu(BaseWidget):

    QtClass = QtWidgets.QMenu

    def __init__(self, *items, text=None, **kwargs):
        super().__init__(**kwargs)
        for items in items:
            self.append(items)
        if text is not None:
            self.text = text

    @property
    def text(self):
        return self.qt.title()

    @text.setter
    def text(self, value):
        self.qt.setTitle(value)

    def append(self, item):
        if isinstance(item, Action):
            self.qt.addAction(item.qt)
        elif isinstance(item, Menu):
            self.qt.addMenu(item.qt)
        elif isinstance(item, str):
            item = Action(item)
            self.qt.addAction(item.qt)
        else:
            raise ValueError(item)
        return item

    def insert(self, before, item):
        if isinstance(item, Action):
            if isinstance(before, Menu):
                self.qt.insertAction(before.qt.menuAction(), action.qt)
            else:
                self.qt.insertAction(before.qt, action.qt)
        elif isinstance(item, Menu):
            if isinstance(before, Menu):
                self.qt.insertMenu(before.qt.menuAction(), menu.qt)
            else:
                self.qt.insertMenu(before.qt, menu.qt)
        elif isinstance(item, str):
            tem = Action(item)
            if isinstance(before, Menu):
                self.qt.insertAction(before.qt.menuAction(), action.qt)
            else:
                self.qt.insertAction(before.qt, action.qt)
        else:
            raise ValueError(item)
        return item

    def __getitem__(self, index):
        item = self.qt.actions()[index]
        return item.property(self.QtProperty)

    def __iter__(self):
        return iter(item.property(self.QtProperty) for item in self.qt.actions())

    def __len__(self):
        return len(self.qt.actions())

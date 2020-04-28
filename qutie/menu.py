from PyQt5 import QtGui, QtWidgets

from .action import Action
from .widget import BaseWidget

__all__ = ['Menu']

class Menu(BaseWidget):

    QtClass = QtWidgets.QMenu

    def __init__(self, text=None, **kwargs):
        super().__init__(**kwargs)
        if text is not None:
            self.text = text

    @property
    def text(self):
        return self.qt.title()

    @text.setter
    def text(self, value):
        self.qt.setTitle(value)

    def append_menu(self, menu):
        if isinstance(menu, str):
            menu = Menu(text=menu)
        self.qt.addMenu(menu.qt)
        return menu

    def insert_menu(self, before, menu):
        if isinstance(menu, str):
            menu = Menu(text=menu)
        if isinstance(before, Menu):
            self.qt.insertMenu(before.qt.menuAction(), menu.qt)
        else:
            self.qt.insertMenu(before.qt, menu.qt)
        return menu

    def append_action(self, action):
        if isinstance(action, str):
            action = Action(text=action)
        self.qt.addAction(action.qt)
        return action

    def insert_action(self, before, action):
        if isinstance(menu, str):
            action = Action(text=action)
        if isinstance(before, Menu):
            self.qt.insertAction(before.qt.menuAction(), action.qt)
        else:
            self.qt.insertAction(before.qt, action.qt)
        return menu

    def append_separator(self):
        self.qt.addSeparator()

    def insert_separator(self, before):
        if isinstance(before, Menu):
            self.qt.insertSeparator(before.qt.menuAction())
        else:
            self.qt.insertSeparator(before.qt)

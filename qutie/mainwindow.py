from PyQt5 import QtWidgets

from .action import Action
from .menu import Menu
from .widget import BaseWidget

__all__ = ['MainWindow']

class MenuBar(BaseWidget):

    QtClass = QtWidgets.QMenuBar

    def __init__(self, *items, **kwargs):
        super().__init__(**kwargs)
        for item in items:
            self.append()

    def append(self, item):
        if isinstance(item, str):
            item = Menu(text=item)
        self.qt.addMenu(item.qt)
        return item

    def insert(self, before, item):
        if isinstance(item, str):
            item = Menu(text=item)
        if isinstance(before, Menu):
            self.qt.insertMenu(before.qt.menuAction(), item.qt)
        else:
            self.qt.insertMenu(before.qt, item.qt)
        return item

class StatusBar(BaseWidget):

    QtClass = QtWidgets.QStatusBar

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def append(self, widget):
        self.qt.addPermanentWidget(widget.qt)
        return widget

class MainWindow(BaseWidget):

    QtClass = QtWidgets.QMainWindow

    def __init__(self, *, layout=None, **kwargs):
        super().__init__(**kwargs)
        self.qt.setMenuBar(MenuBar().qt)
        self.qt.setStatusBar(StatusBar().qt)
        self.layout = layout

    @property
    def layout(self):
        widget = self.qt.centralWidget()
        if widget is not None:
            return widget.property(self.QtProperty)
        return None

    @layout.setter
    def layout(self, value):
        if value is None:
            self.qt.setCentralWidget(None)
        else:
            if not isinstance(value, BaseWidget):
                raise ValueError(value)
            self.qt.setCentralWidget(value.qt)

    @property
    def menubar(self):
        return self.qt.menuBar().property(self.QtProperty)

    @property
    def statusbar(self):
        return self.qt.statusBar().property(self.QtProperty)

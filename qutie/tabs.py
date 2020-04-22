from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget, Widget

__all__ = [
    'Tab',
    'Tabs'
]

class Tab(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def title(self):
        return self.qt.windowTitle()

    @title.setter
    def title(self, title):
        self.qt.setWindowTitle(title)
        if self.qt.parent():
            if self.qt.parent().parent():
                index = self.qt.parent().parent().indexOf(self.qt)
                self.qt.parent().parent().setTabText(index, title)

class Tabs(BaseWidget):

    QtClass = QtWidgets.QTabWidget

    def __init__(self, *children, **kwargs):
        super().__init__(**kwargs)
        for child in children:
            self.append(child)

    def append(self, tab):
        self.qt.addTab(tab.qt, tab.title)

    def insert(self, index, tab):
        self.qt.insertTab(index, tab.qt, tab.title)

    def remove(self, tab):
        index = self.qt.indexOf(tab.qt)
        self.qt.removeTab(index)

    @property
    def current(self):
        index = self.qt.currentIndex()
        if index is not None:
            return self.qt.widget(index).property(self.QtProperty)
        return None

    @current.setter
    def current(self, tab):
        self.qt.setCurrentIndex(self.indexOf(tab.qt))

    @property
    def children(self):
        children = []
        for index in self.qt.count():
            children.append(self.qt.widget(index).property(self.QtProperty))
        return tuple(children)

    def __len__(self):
        return self.qt.count()

    def __iter__(self):
        return iter(self.children)

    def __getitem__(self, index):
        return self.children[index]

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
    def title(self, value):
        self.qt.setWindowTitle(value)
        parent = self.qt.parent()
        if parent:
            if parent.parent():
                index = parent.parent().indexOf(self.qt)
                parent.parent().setTabText(index, value)

class Tabs(BaseWidget):

    QtClass = QtWidgets.QTabWidget

    def __init__(self, *children, changed=None, **kwargs):
        super().__init__(**kwargs)
        for child in children:
            self.append(child)

        self.changed = changed
        def changed_event(index):
            if callable(self.changed):
                self.changed(index)
        self.qt.currentChanged.connect(changed_event)

    def append(self, tab):
        self.qt.addTab(tab.qt, tab.title)

    def insert(self, index, tab):
        if index < 0:
            index = max(0, len(self) + index)
        self.qt.insertTab(index, tab.qt, tab.title)

    def remove(self, tab):
        if tab is not None:
            index = self.qt.indexOf(tab.qt)
            self.qt.removeTab(index)

    @property
    def current(self):
        index = self.qt.currentIndex()
        if index >= 0:
            return self.qt.widget(index).property(self.QtProperty)
        return None

    @current.setter
    def current(self, value):
        self.qt.setCurrentIndex(self.indexOf(value.qt))

    @property
    def children(self):
        children = []
        for index in self.qt.count():
            children.append(self.qt.widget(index).property(self.QtProperty))
        return tuple(children)

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, changed):
        self.__changed = changed

    def __len__(self):
        return self.qt.count()

    def __iter__(self):
        return iter(self.children)

    def __getitem__(self, index):
        return self.children[index]

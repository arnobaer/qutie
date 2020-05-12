from .qt import QtCore
from .qt import QtWidgets
from .qt import bind

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
        # Update tab title
        parent = self.qt.parent()
        if parent:
            if parent.parent():
                index = parent.parent().indexOf(self.qt)
                parent.parent().setTabText(index, value)

@bind(QtWidgets.QTabWidget)
class Tabs(BaseWidget):

    def __init__(self, *items, changed=None, **kwargs):
        super().__init__(**kwargs)
        for items in items:
            self.append(items)
        self.changed = changed
        # Connect signals
        self.qt.currentChanged.connect(self.__handle_changed)

    @property
    def items(self):
        return list(self)

    def append(self, tab):
        assert isinstance(tab, Tab), "must be of type Tab"
        self.qt.addTab(tab.qt, tab.title)

    def insert(self, index, tab):
        assert isinstance(tab, Tab), "must be of type Tab"
        if index < 0:
            index = max(0, len(self) + index)
        self.qt.insertTab(index, tab.qt, tab.title)

    def remove(self, tab):
        assert isinstance(tab, Tab), "must be of type Tab"
        if tab is not None:
            index = self.qt.indexOf(tab.qt)
            self.qt.removeTab(index)

    @property
    def current(self):
        index = self.qt.currentIndex()
        return self[index]

    @current.setter
    def current(self, item):
        index = self.index(item)
        self.qt.setCurrentIndex(index)

    def index(self, item):
        index = self.qt.indexOf(item.qt)
        if index < 0:
            raise ValueError("item not in tabs")
        return index

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, changed):
        self.__changed = changed

    def __handle_changed(self, index):
        if callable(self.changed):
            self.changed(index)

    def __getitem__(self, index):
        widget = self.qt.widget(index)
        if not widget:
            raise KeyError()
        return widget.property(self.QtPropertyKey)

    def __len__(self):
        return self.qt.count()

    def __iter__(self):
        return (self[index] for index in range(len(self)))

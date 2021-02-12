"""Stack module.

For more information on the underlying Qt5 object see
[QStackedWidget](https://doc.qt.io/qt-5/qstackedwidget.html).
"""

from .qutie import QtCore
from .qutie import QtWidgets

from .widget import BaseWidget

__all__ = ['Stack']

class Stack(BaseWidget):

    QtClass = QtWidgets.QStackedWidget

    changed = None

    def __init__(self, *items, changed=None, **kwargs):
        super().__init__(**kwargs)
        # Properties
        for item in items:
            self.append(item)
        # Callbacks
        self.changed = changed
        # Connect signals
        self.qt.currentChanged.connect(lambda index: self.emit(self.changed, index))

    def append(self, item):
        self.qt.addWidget(item.qt)

    def insert(self, index, item):
        if index < 0:
            index = max(0, len(self) + index)
        self.qt.insertWidget(index, item.qt)

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def remove(self, item):
        self.qt.removeWidget(item.qt)

    @property
    def current(self):
        index = self.qt.currentIndex()
        if index < 0:
            return None
        return item.reflection()

    @current.setter
    def current(self, item):
        self.qt.setCurrentIndex(self.index(item))

    def index(self, item):
        index = self.qt.indexOf(item.qt)
        if index < 0:
            raise ValueError("item not in stack")
        return index

    def __getitem__(self, key):
        item = self.qt.widget(key)
        if not item:
            raise KeyError(key)
        return item.reflection()

    def __setitem__(self, key, value):
        del self[key]
        self.insert(key, value)

    def __delitem__(self, key):
        item = self[key]
        self.qt.removeWidget(item)

    def __len__(self):
        return self.qt.count()

    def __iter__(self):
        return (self[index] for index in range(len(self)))

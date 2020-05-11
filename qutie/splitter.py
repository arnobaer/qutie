from PyQt5 import QtCore
from PyQt5 import QtWidgets

from .widget import BaseWidget

__all__ = ['Splitter']

class Splitter(BaseWidget):
    """Splitter

    >>> splitter = Splitter(orientation='vertical')
    >>> splitter.append(List(["Spam", "Eggs"]))
    >>> splitter.insert(List(["Ham", "Spam"]))
    >>> for child in splitter.children:
    ...     pass
    """

    QtClass = QtWidgets.QSplitter

    def __init__(self, *children, sizes=None, orientation=None, collapsible=True, stretch=None, **kwargs):
        super().__init__(**kwargs)
        for child in children:
            self.append(child)
        if sizes is not None:
            self.sizes = sizes
        if orientation is not None:
            self.orientation = orientation
        self.collapsible = collapsible
        if stretch is not None:
            for index, value in enumerate(stretch):
                self.qt.setStretchFactor(index, value)

    @property
    def children(self):
        children = []
        for index in range(self.qt.count()):
            children.append(self.qt.widget(index).property(self.QtProperty))
        return tuple(children)

    @property
    def sizes(self):
        return tuple(self.qt.sizes())

    @sizes.setter
    def sizes(self, value):
        self.qt.setSizes(list(value))

    @property
    def orientation(self):
        return {
            QtCore.Qt.Horizontal: "horizontal",
            QtCore.Qt.Vertical: "vertical"
        }[self.qt.orientation()]

    @orientation.setter
    def orientation(self, value):
        self.qt.setOrientation({
            "horizontal": QtCore.Qt.Horizontal,
            "vertical": QtCore.Qt.Vertical
        }[value])

    @property
    def collapsible(self):
        return self.qt.childrenCollapsible()

    @collapsible.setter
    def collapsible(self, value):
        self.qt.setChildrenCollapsible(value)

    @property
    def handle_width(self):
        return self.qt.handleWidth()

    @handle_width.setter
    def handle_width(self, value):
        self.qt.setHandleWidth(value)

    def append(self, child):
        if not isinstance(child, BaseWidget):
            raise ValueError(child)
        self.qt.addWidget(child.qt)

    def __getitem__(self, index):
        item = self.qt.widget(index)
        if item is not None:
            return item.property(self.QtProperty)
        return None

    def __len__(self):
        return self.qt.count()

    def __iter__(self):
        return (self.qt.widget(index) for index in range(self.qt.count()))

from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget

__all__ = ['Splitter']

class Splitter(BaseWidget):

    QtClass = QtWidgets.QSplitter

    def __init__(self, *children, orientation=None, collapsible=True, stretch=None, **kwargs):
        super().__init__(**kwargs)
        for child in children:
            self.append(child)
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
    def orientation(self):
        return {
            QtCore.Qt.Horizontal: "horizontal",
            QtCore.Qt.Vertical: "vertical"
        }[self.qt.orientation()]

    @orientation.setter
    def orientation(self, orientation):
        self.qt.setOrientation({
            "horizontal": QtCore.Qt.Horizontal,
            "vertical": QtCore.Qt.Vertical
        }[orientation])

    @property
    def collapsible(self):
        return self.qt.childrenCollapsible()

    @collapsible.setter
    def collapsible(self, enable):
        self.qt.setChildrenCollapsible(enable)

    def append(self, child):
        if not isinstance(child, BaseWidget):
            raise ValueError(child)
        self.qt.addWidget(child.qt)

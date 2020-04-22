from PyQt5 import QtWidgets

from .widget import BaseWidget

__all__ = ['Column', 'Row', 'Spacer']

class BoxLayout(BaseWidget):

    QtLayoutClass = QtWidgets.QBoxLayout

    def __init__(self, *children, stretch=None, **kwargs):
        super().__init__(**kwargs)
        self.qt.setLayout(self.QtLayoutClass())
        self.qt.layout().setContentsMargins(0, 0, 0, 0)
        for child in children:
            self.append(child)
        if stretch is not None:
            for index, value in enumerate(stretch):
                self.qt.layout().setStretch(index, value)

    @property
    def children(self):
        children = []
        for index in range(self.qt.layout().count()):
            children.append(self.qt.layout().itemAt(index).widget().property(self.QtProperty))
        return tuple(children)

    def append(self, child):
        print("XXX", child)
        self.qt.layout().addWidget(child.qt)

    def insert(self, index, child):
        self.qt.layout().insertWidget(child.qt)

    def remove(self, child):
        index = self.qt.layout().indexOf(child.qt)
        self.qt.layout().takeAt(index)

class Column(BoxLayout):

    QtLayoutClass = QtWidgets.QVBoxLayout

class Row(BoxLayout):

    QtLayoutClass = QtWidgets.QHBoxLayout

class Spacer(BaseWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qt.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

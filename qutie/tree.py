from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget

__all__ = ['Tree']

class Tree(BaseWidget):

    QtClass = QtWidgets.QTreeWidget

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

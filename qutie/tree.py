from PyQt5 import QtCore, QtWidgets

from .base import to_alignment, from_alignment
from .base import BaseWidget

__all__ = ['Tree']

class Tree(BaseWidget):

    QtClass = QtWidgets.QTreeWidget

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

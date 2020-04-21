from PyQt5 import QtCore, QtWidgets

from .base import to_alignment, from_alignment
from .base import BaseWidget

__all__ = ['Table']

class Table(BaseWidget):

    QtClass = QtWidgets.QTableWidget

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

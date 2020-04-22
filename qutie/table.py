from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget

__all__ = ['Table']

class Table(BaseWidget):

    QtClass = QtWidgets.QTableWidget

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

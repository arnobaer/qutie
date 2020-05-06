from PyQt5 import QtCore
from PyQt5 import QtWidgets

from .widget import BaseWidget

__all__ = ['Label']

class Label(BaseWidget):

    QtClass = QtWidgets.QLabel

    def __init__(self, text=None, **kwargs):
        super().__init__(**kwargs)
        if text is not None:
            self.text = text

    @property
    def text(self):
        return self.qt.text()

    @text.setter
    def text(self, value):
        self.qt.setText(value)

from PyQt5 import QtCore, QtWidgets

from .object import to_alignment, from_alignment
from .widget import BaseWidget

__all__ = ['Label']

class Label(BaseWidget):

    QtClass = QtWidgets.QLabel

    def __init__(self, *, alignment=None, text=None, **kwargs):
        super().__init__(**kwargs)
        if alignment is not None:
            self.alignment = alignment
        if text is not None:
            self.text = text

    @property
    def alignment(self):
        return from_alignment(self.qt.alignment())

    @alignment.setter
    def alignment(self, value):
        self.qt.setAlignment(to_alignment(value))

    @property
    def text(self):
        return self.qt.text()

    @text.setter
    def text(self, value):
        self.qt.setText(value)

from PyQt5 import QtCore, QtWidgets

from .base import BaseWidget

__all__ = ['Button']

class Button(BaseWidget):

    QtClass = QtWidgets.QPushButton

    def __init__(self, *, text=None, clicked=None, **kwargs):
        super().__init__(**kwargs)
        self.text = text or ""
        self.clicked = clicked
        def clicked_event():
            if callable(self.clicked):
                self.clicked()
        self.qt.clicked.connect(clicked_event)

    @property
    def text(self):
        return self.qt.text()

    @text.setter
    def text(self, text):
        self.qt.setText(text)

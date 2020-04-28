import os

from PyQt5 import QtWidgets

from .widget import BaseWidget

__all__ = ['TextArea']

class TextArea(BaseWidget):

    QtClass = QtWidgets.QTextEdit

    def __init__(self, *, text=None, readonly=False, richtext=False, **kwargs):
        super().__init__(**kwargs)
        if text is not None:
            self.text = text
        self.readonly = readonly
        self.richtext = richtext

    @property
    def text(self):
        return self.qt.toPlainText()

    @text.setter
    def text(self, value):
        self.qt.setPlainText(value)

    @property
    def readoly(self):
        return self.qt.readOnly()

    @readoly.setter
    def readoly(self, value):
        self.qt.setReadOnly(value)

    @property
    def richtext(self):
        return self.qt.acceptRichText()

    @richtext.setter
    def richtext(self, value):
        self.qt.setAcceptRichText(value)

    def append(self, text):
        self.text = os.linesep.join((self.text, text))

    def insert(self, text):
        self.qt.insertPlainText(text)

    def clear(self):
        self.qt.clear()

    def select_all(self):
        self.qt.selectAll()

    def redo(self):
        self.qt.redo()

    def undo(self):
        self.qt.undo()

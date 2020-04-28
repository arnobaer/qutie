from PyQt5 import QtWidgets

from .widget import Widget

__all__ = ['FieldSet']

class FieldSet(Widget):

    QtClass = QtWidgets.QGroupBox

    def __init__(self, title=None, **kwargs):
        super().__init__(**kwargs)
        if title is not None:
            self.title = title

    @property
    def title(self):
        return self.qt.title()

    @title.setter
    def title(self, value):
        self.qt.setTitle(value)

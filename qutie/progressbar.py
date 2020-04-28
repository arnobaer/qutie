from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget

__all__ = ['ProgressBar']

class ProgressBar(BaseWidget):

    QtClass = QtWidgets.QProgressBar

    def __init__(self, value=0, *, minimum=0, maximum=100, **kwargs):
        super().__init__(**kwargs)
        self.minimum = minimum
        self.maximum = maximum
        self.value = value

    @property
    def value(self):
        return self.qt.value()

    @value.setter
    def value(self, value):
        self.qt.setValue(value)

    @property
    def minimum(self):
        return self.qt.minimum()

    @minimum.setter
    def minimum(self, value):
        self.qt.setMinimum(value)

    @property
    def maximum(self):
        return self.qt.maximum()

    @maximum.setter
    def maximum(self, value):
        self.qt.setMaximum(value)

    @property
    def range(self):
        return self.minimum, self.maximum

    @range.setter
    def range(self, value):
        self.minimum = value[0]
        self.maximum = value[1]

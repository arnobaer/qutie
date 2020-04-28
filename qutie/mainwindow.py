from PyQt5 import QtWidgets

from .action import Action
from .widget import BaseWidget

__all__ = ['MainWindow']

class MainWindow(BaseWidget):

    QtClass = QtWidgets.QMainWindow

    def __init__(self, *, layout=None, **kwargs):
        super().__init__(**kwargs)
        self.qt.menuBar()
        self.qt.statusBar()
        self.layout = layout

    @property
    def layout(self):
        widget = self.qt.centralWidget()
        if widget is not None:
            return widget.property(self.QtProperty)
        return None

    @layout.setter
    def layout(self, value):
        if value is None:
            self.qt.setCentralWidget(None)
        else:
            if not isinstance(value, BaseWidget):
                raise ValueError(value)
            self.qt.setCentralWidget(value.qt)

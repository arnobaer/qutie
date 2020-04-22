from PyQt5 import QtWidgets

from .widget import BaseWidget

__all__ = ['MainWindow']

class MainWindow(BaseWidget):

    QtClass = QtWidgets.QMainWindow

    def __init__(self, *, layout=None, **kwargs):
        super().__init__(**kwargs)
        self.layout = layout

    @property
    def layout(self):
        widget = self.qt.centralWidget()
        if widget is not None:
            return widget.property(self.QtProperty)
        return None

    @layout.setter
    def layout(self, layout):
        if layout is None:
            self.qt.setCentralWidget(None)
        else:
            if not isinstance(layout, BaseWidget):
                raise ValueError(layout)
            self.qt.setCentralWidget(layout.qt)

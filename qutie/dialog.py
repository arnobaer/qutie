from PyQt5 import QtWidgets

from .widget import Widget

__all__ = ['Dialog']

class Dialog(Widget):

    QtClass = QtWidgets.QDialog

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        return self.qt.exec_()

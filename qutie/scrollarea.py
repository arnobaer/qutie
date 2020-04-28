from PyQt5 import QtGui, QtWidgets

from .widget import Widget

__all__ = ['ScrollArea']

class ScrollArea(Widget):

    QtClass = QtWidgets.QScrollArea

    def __init__(self, layout=None, **kwargs):
        super().__init__(**kwargs)
        self.qt.setWidgetResizable(True)
        self.qt.setWidget(Widget().qt)
        self.qt.setBackgroundRole(QtGui.QPalette.Base) # fix background
        if layout is not None:
            self.layout = layout

    @property
    def layout(self):
        return self.qt.widget().property(self.QtProperty).layout

    @layout.setter
    def layout(self, value):
        if self.qt.widget():
            self.qt.widget().property(self.QtProperty).layout = value

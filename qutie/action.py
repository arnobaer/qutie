from PyQt5 import QtGui, QtWidgets

from .object import Object

__all__ = ['Action']

class Action(Object):

    QtClass = QtWidgets.QAction

    def __init__(self, text=None, *, checkable=None, checked=False, tooltip=None,
                 statustip=None, shortcut=None, triggered=None, toggled=None,
                 **kwargs):
        super().__init__(**kwargs)
        if text is not None:
            self.text = text
        if checkable is not None:
            self.checkable = checkable
        self.checked = checked
        if tooltip is not None:
            self.tooltip = tooltip
        if statustip is not None:
            self.statustip = statustip
        if shortcut is not None:
            self.shortcut = shortcut

        self.triggered = triggered
        def triggered_event():
            if callable(self.triggered):
                self.triggered()
        self.qt.triggered.connect(triggered_event)

        self.toggled = toggled
        def toggled_event(checked):
            if callable(self.toggled):
                self.toggled(checked)
        self.qt.toggled.connect(toggled_event)

    @property
    def text(self):
        return self.qt.text()

    @text.setter
    def text(self, value):
        self.qt.setText(value)

    @property
    def checked(self):
        return self.qt.isChecked()

    @checked.setter
    def checked(self, value):
        self.qt.setChecked(value)

    @property
    def checkable(self):
        return self.qt.isCheckable()

    @checkable.setter
    def checkable(self, value):
        self.qt.setCheckable(value)

    @property
    def tooltip(self):
        return self.qt.toolTip()

    @tooltip.setter
    def tooltip(self, value):
        self.qt.setToolTip(value)

    @property
    def statustip(self):
        return self.qt.statusTip()

    @statustip.setter
    def statustip(self, value):
        self.qt.setStatusTip(value)

    @property
    def shortcut(self):
        return self.qt.shortcut().toString() or None

    @shortcut.setter
    def shortcut(self, value):
        if value is None:
            self.qt.setShortcut(QtGui.QKeySequence())
        else:
            self.qt.setShortcut(QtGui.QKeySequence(value))

    def trigger(self):
        self.qt.trigger()

    def toggle(self):
        self.qt.toggle()

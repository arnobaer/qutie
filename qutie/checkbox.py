from PyQt5 import QtCore
from PyQt5 import QtWidgets

from .widget import BaseWidget

__all__ = ['CheckBox']

class CheckBox(BaseWidget):

    QtClass = QtWidgets.QCheckBox

    def __init__(self, text=None, *, checked=False, changed=None, **kwargs):
        super().__init__(**kwargs)
        if text is not None:
            self.text = text
        self.checked = checked

        self.changed = changed
        def changed_event(state):
            if callable(self.changed):
                self.changed(state == QtCore.Qt.Checked)
        self.qt.stateChanged.connect(changed_event)

    @property
    def text(self):
        return self.qt.text()

    @text.setter
    def text(self, value):
        self.qt.setText(value)

    @property
    def checked(self):
        return self.qt.checkState() == QtCore.Qt.Checked

    @checked.setter
    def checked(self, value):
        self.qt.setChecked(QtCore.Qt.Checked if value else QtCore.Qt.Unchecked)

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, value):
        self.__changed = value

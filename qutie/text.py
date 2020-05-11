from PyQt5 import QtCore
from PyQt5 import QtWidgets

from .widget import BaseWidget

__all__ = ['Text']

class Text(BaseWidget):

    QtClass = QtWidgets.QLineEdit

    def __init__(self, value=None, *, readonly=False, clearable=False,
                 changed=None, editing_finished=None, **kwargs):
        super().__init__(**kwargs)
        self.readonly = readonly
        self.clearable = clearable
        if value is not None:
            self.value = value

        self.changed = changed
        def changed_event(text):
            if callable(self.changed):
                self.changed(text)
        self.qt.textChanged.connect(changed_event)

        self.editing_finished = editing_finished
        def editing_finished_event():
            if callable(self.editing_finished):
                self.editing_finished()
        self.qt.editingFinished.connect(editing_finished_event)

    @property
    def value(self):
        return self.qt.text()

    @value.setter
    def value(self, value):
        self.qt.setText(value)

    @property
    def readonly(self):
        return self.qt.isReadOnly()

    @value.setter
    def readonly(self, value):
        self.qt.setReadOnly(value)

    @property
    def clearable(self):
        return self.qt.clearButtonEnabled()

    @clearable.setter
    def clearable(self, value):
        self.qt.setClearButtonEnabled(value)

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, value):
        self.__changed = value

    @property
    def editing_finished(self):
        return self.__editing_finished

    @editing_finished.setter
    def editing_finished(self, value):
        self.__editing_finished = value

    def clear(self):
        self.qt.clear()

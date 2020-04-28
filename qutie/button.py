from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget

__all__ = ['Button']

class Button(BaseWidget):

    QtClass = QtWidgets.QPushButton

    def __init__(self, text=None, *, checkable=None, checked=None,
                 default=False, auto_default=False, clicked=None, toggled=None,
                 pressed=None, released=None, **kwargs):
        super().__init__(**kwargs)
        if text is not None:
            self.text = text
        if checkable is not None:
            self.checkable = checkable
        if checked is not None:
            self.checked = checked
        if default is not None:
            self.default = default
        if auto_default is not None:
            self.auto_default = auto_default
        
        self.clicked = clicked
        def clicked_event():
            if callable(self.clicked):
                self.clicked()
        self.qt.clicked.connect(clicked_event)

        self.toggled = toggled
        def toggled_event(checked):
            if callable(self.toggled):
                self.toggled(checked)
        self.qt.toggled.connect(toggled_event)

        self.pressed = pressed
        def pressed_event():
            if callable(self.pressed):
                self.pressed()
        self.qt.pressed.connect(pressed_event)

        self.released = released
        def released_event():
            if callable(self.released):
                self.released()
        self.qt.released.connect(released_event)

    @property
    def text(self):
        return self.qt.text()

    @text.setter
    def text(self, value):
        self.qt.setText(value)

    @property
    def checkable(self):
        return self.qt.isCheckable()

    @checkable.setter
    def checkable(self, value):
        self.qt.setCheckable(value)

    @property
    def checked(self):
        return self.qt.isChecked()

    @checked.setter
    def checked(self, value):
        self.qt.setChecked(value)

    @property
    def default(self):
        return self.qt.isDefault()

    @default.setter
    def default(self, value):
        self.qt.setDefault(value)

    @property
    def auto_default(self):
        return self.qt.isAutoDefault()

    @auto_default.setter
    def auto_default(self, value):
        self.qt.setAutoDefault(value)

    def click(self):
        self.qt.click()

    def toggle(self):
        self.qt.toggle()

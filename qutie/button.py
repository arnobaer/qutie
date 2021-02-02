from .qutie import QtGui
from .qutie import QtWidgets
from .qutie import ArrowType

from .icon import Icon
from .object import Object
from .widget import Widget

__all__ = ['Button', 'PushButton', 'ToolButton', 'RadioButton', 'ButtonGroup']

class AbstractButton(Widget):

    QtClass = QtWidgets.QAbstractButton

    def __init__(self, text=None, *, checkable=None, checked=None, icon=None,
                 clicked=None, toggled=None, pressed=None, released=None,
                 **kwargs):
        super().__init__(**kwargs)
        if text is not None:
            self.text = text
        if checkable is not None:
            self.checkable = checkable
        if checked is not None:
            self.checked = checked
        if icon is not None:
            self.icon = icon
        self.clicked = clicked
        self.pressed = pressed
        self.released = released
        self.toggled = toggled
        # Connect signals
        self.qt.clicked.connect(self.__handle_clicked)
        self.qt.pressed.connect(self.__handle_pressed)
        self.qt.released.connect(self.__handle_released)
        self.qt.toggled.connect(self.__handle_toggled)

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
    def icon(self):
        icon = self.qt.icon()
        if icon.isNull():
            return None
        return Icon(qt=icon)

    @icon.setter
    def icon(self, value):
        if value is None:
            self.qt.setIcon(QtGui.QIcon())
        else:
            if not isinstance(value, Icon):
                value = Icon(value)
            self.qt.setIcon(value.qt)

    @property
    def clicked(self):
        return self.__clicked

    @clicked.setter
    def clicked(self, value):
        self.__clicked = value

    def __handle_clicked(self, _):
        if callable(self.clicked):
            self.clicked()

    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value

    def __handle_pressed(self):
        if callable(self.pressed):
            self.pressed()

    @property
    def released(self):
        return self.__released

    @released.setter
    def released(self, value):
        self.__released = value

    def __handle_released(self):
        if callable(self.released):
            self.released()

    @property
    def toggled(self):
        return self.__toggled

    @toggled.setter
    def toggled(self, value):
        self.__toggled = value

    def __handle_toggled(self, checked):
        if callable(self.toggled):
            self.toggled(checked)

    def click(self):
        self.qt.click()

class PushButton(AbstractButton):

    QtClass = QtWidgets.QPushButton

    def __init__(self, text=None, *, default=False, auto_default=False,
                 flat=None, **kwargs):
        super().__init__(text=text, **kwargs)
        if default is not None:
            self.default = default
        if auto_default is not None:
            self.auto_default = auto_default
        if flat is not None:
            self.flat = flat

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

    @property
    def flat(self):
        return self.qt.isFlat()

    @flat.setter
    def flat(self, value):
        self.qt.setFlat(value)

Button = PushButton

class ToolButton(AbstractButton):

    QtClass = QtWidgets.QToolButton

    def __init__(self, text=None, *, arrow_type=None, auto_raise=None,
                 **kwargs):
        super().__init__(text=text, **kwargs)
        if arrow_type is not None:
            self.arrow_type = arrow_type
        if auto_raise is not None:
            self.auto_raise = auto_raise

    @property
    @ArrowType.getter
    def arrow_type(self):
        return self.qt.arrowType()

    @arrow_type.setter
    @ArrowType.setter
    def arrow_type(self, value):
        self.qt.setArrowType(value)

    @property
    def auto_raise(self):
        return self.qt.autoRaise()

    @auto_raise.setter
    def auto_raise(self, value):
        self.qt.setAutoRaise(value)

class RadioButton(AbstractButton):

    QtClass = QtWidgets.QRadioButton

class ButtonGroup(Object):

    QtClass = QtWidgets.QButtonGroup

    def __init__(self, *buttons, exclusive=True, **kwargs):
        super().__init__(**kwargs)
        self.update(buttons)
        self.exclusive = exclusive

    @property
    def exclusive(self):
        return self.qt.exclusive()

    @exclusive.setter
    def exclusive(self, value):
        self.qt.setExclusive(value)

    def add(self, button):
        self.qt.addButton(button.qt)

    def remove(self, button):
        self.qt.removeButton(button.qt)

    def update(self, buttons):
        for button in buttons:
            self.add(button)

    def clear(self):
        for button in list(self):
            self.remove(button)

    def __len__(self):
        return len(self.qt.buttons())

    def __iter__(self):
        return (button.reflection for button in self.qt.buttons())

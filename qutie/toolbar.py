from .qutie import QtCore
from .qutie import QtWidgets
from .qutie import Orientation
from .qutie import ToolButtonStyle

from .action import Action
from .menu import Menu
from .mixins import OrientationMixin
from .widget import BaseWidget

__all__ = ['ToolBar']

class ToolBar(BaseWidget, OrientationMixin):

    QtClass = QtWidgets.QToolBar

    def __init__(self, *items, floatable=None, movable=None, orientation=None,
                 tool_button_style=None, orientation_changed=None,
                 tool_button_style_changed=None, **kwargs):
        super().__init__(**kwargs)
        if floatable is not None:
            self.floatable = floatable
        if movable is not None:
            self.movable = movable
        if orientation is not None:
            self.orientation = orientation
        if tool_button_style is not None:
            self.tool_button_style = tool_button_style
        for item in items:
            self.append(item)
        self.orientation_changed = orientation_changed
        self.tool_button_style_changed = tool_button_style_changed
        # Connect signals
        self.qt.orientationChanged.connect(self.__handle_orientation_changed)

    @property
    def floatable(self):
        return self.qt.isFloatable()

    @floatable.setter
    def floatable(self, value):
        self.qt.setFloatable(bool(value))

    @property
    def movable(self):
        return self.qt.isMovable()

    @movable.setter
    def movable(self, value):
        self.qt.setMovable(bool(value))

    @property
    @ToolButtonStyle.getter
    def tool_button_style(self):
        return self.qt.toolButtonStyle()

    @tool_button_style.setter
    @ToolButtonStyle.setter
    def tool_button_style(self, value):
        self.qt.setToolButtonStyle(value)

    def index(self, item):
        for index, action in enumerate(self):
            if action is item:
                return index
        raise ValueError("item not in list")

    def clear(self):
        while len(self):
            self.remove(self[0])

    def append(self, item):
        if isinstance(item, str):
            item = Action(text=item)
        if isinstance(item, Menu):
            self.qt.addAction(item.qt.menuAction())
        else:
            self.qt.addAction(item.qt)
        return item

    def insert(self, index, item):
        if index < 0:
            index = max(0, len(self) + index)
        if isinstance(item, str):
            item = Action(text=item)
        before = self[index] if len(self) else None
        if isinstance(before, type(None)):
            self.qt.insertAction(None, item.qt)
        elif isinstance(before, Menu):
            self.qt.insertAction(before.qt.menuAction(), item.qt)
        else:
            self.qt.insertAction(before.qt, item.qt)
        return item

    def remove(self, item):
        index = self.index(item)
        self.qt.removeAction(self.qt.actions()[index])

    def _get_action_or_menu(self, action):
        if hasattr(action, 'reflection'):
            return action.reflection()
        return action.menu().reflection()

    def __getitem__(self, index):
        action = self.qt.actions()[index]
        return self._get_action_or_menu(action)

    def __iter__(self):
        return iter(self._get_action_or_menu(action) for action in self.qt.actions())

    def __len__(self):
        return len(self.qt.actions())

    @property
    def orientation_changed(self):
        return self.__orientation_changed

    @orientation_changed.setter
    def orientation_changed(self, value):
        self.__orientation_changed = value

    def __handle_orientation_changed(self, value):
        if callable(self.orientation_changed):
            self.orientation_changed(value)

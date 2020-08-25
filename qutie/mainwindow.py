from .qt import QtCore
from .qt import QtWidgets
from .qt import bind

from .action import Action
from .menu import Menu
from .widget import BaseWidget

__all__ = ['MainWindow', 'ToolBar']

@bind(QtWidgets.QMenuBar)
class MenuBar(BaseWidget):

    def __init__(self, *items, **kwargs):
        super().__init__(**kwargs)
        for item in items:
            self.append(item)

    def index(self, item):
        for index, action in enumerate(self):
            if action and action is item.qt.property(self.QtPropertyKey):
                return index
        raise ValueError("item not in list")

    def clear(self):
        while len(self):
            self.qt.removeAction(self[0])

    def append(self, item):
        if isinstance(item, str):
            item = Menu(text=item)
        print('MenuBarappendXXXXXXXXXX', item.qt.property(self.QtPropertyKey))
        self.qt.addMenu(item.qt)
        return item

    def insert(self, index, item):
        if index < 0:
            index = max(0, len(self) + index)
        if isinstance(item, str):
            item = Menu(text=item)
        before = self[index]
        if isinstance(before, Menu):
            self.qt.insertMenu(before.qt.menuAction(), item.qt)
        elif isinstance(before, type(None)):
            self.qt.insertMenu(None, item.qt)
        else:
            self.qt.insertMenu(before.qt, item.qt)
        return item

    def remove(self, item):
        self.qt.removeAction(item.qt)

    def __getitem__(self, index):
        item = self.qt.actions()[index]
        return item.property(self.QtPropertyKey)

    def __iter__(self):
        return iter(item.menu().property(self.QtPropertyKey) for item in self.qt.actions())

    def __len__(self):
        return len(self.qt.actions())

@bind(QtWidgets.QStatusBar)
class StatusBar(BaseWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def append(self, widget):
        self.qt.addPermanentWidget(widget.qt)
        return widget

@bind(QtWidgets.QToolBar)
class ToolBar(BaseWidget):

    def __init__(self, *items, floatable=None, movable=None, orientation=None,
                 **kwargs):
        super().__init__(**kwargs)
        if floatable is not None:
            self.floatable = floatable
        if movable is not None:
            self.movable = movable
        if orientation is not None:
            self.orientation = orientation
        for item in items:
            self.append(item)

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
    def orientation(self):
        return {
            QtCore.Qt.Horizontal: 'horizontal',
            QtCore.Qt.Vertical: 'vertical'
        }[self.qt.orientation()]

    @orientation.setter
    def orientation(self, value):
        self.qt.setOrientation({
            'horizontal': QtCore.Qt.Horizontal,
            'vertical': QtCore.Qt.Vertical
        }[value])

    def index(self, item):
        for index, action in enumerate(self):
            if action and action.qt.property(self.QtPropertyKey) is item.qt.property(self.QtPropertyKey):
                return index
        raise ValueError("item not in list")

    def clear(self):
        while len(self):
            self.qt.removeAction(self[0])

    def append(self, item):
        if isinstance(item, str):
            item = Action(text=item)
        self.qt.addAction(item.qt)
        return item

    def insert(self, index, item):
        if index < 0:
            index = max(0, len(self) + index)
        if isinstance(item, str):
            item = Action(text=item)
        before = self[index]
        if isinstance(before, Menu):
            self.qt.addAction(before.qt.menuAction(), item.qt)
        else:
            self.qt.addAction(before.qt, item.qt)
        return item

    def remove(self, item):
        self.qt.removeAction(item.qt)

    def __getitem__(self, index):
        item = self.qt.actions()[index]
        return item.property(self.QtPropertyKey)

    def __iter__(self):
        return iter(item.property(self.QtPropertyKey) for item in self.qt.actions())

    def __len__(self):
        return len(self.qt.actions())

@bind(QtWidgets.QMainWindow)
class MainWindow(BaseWidget):

    def __init__(self, *, layout=None, **kwargs):
        super().__init__(**kwargs)
        self.qt.setMenuBar(MenuBar().qt)
        self.qt.setStatusBar(StatusBar().qt)
        self.layout = layout

    @property
    def layout(self):
        widget = self.qt.centralWidget()
        if widget is not None:
            return widget.property(self.QtPropertyKey)
        return None

    @layout.setter
    def layout(self, value):
        if value is None:
            self.qt.setCentralWidget(None)
        else:
            if not isinstance(value, BaseWidget):
                raise ValueError(value)
            self.qt.setCentralWidget(value.qt)

    @property
    def menubar(self):
        return self.qt.menuBar().property(self.QtPropertyKey)

    @property
    def statusbar(self):
        return self.qt.statusBar().property(self.QtPropertyKey)

    def append(self, item):
        self.qt.addToolBar(item.qt)

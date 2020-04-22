from PyQt5 import QtCore, QtWidgets

from .base import Base
from .widget import BaseWidget

__all__ = ['Tree']

class Tree(BaseWidget):
    """Tree
    >>> tree = Tree(header=["Key", "Value"])
    >>> tree.append(["Spam", "Eggs"])
    >>> for item in tree:
    ...     item[0].checked =True
    ...     item[1].color = "blue"
    ...     child = item.append(["Ham", "Spam"])
    ...     child.checked = False
    >>> tree.clear()
    """

    QtClass = QtWidgets.QTreeWidget

    def __init__(self, header=None, activated=None, changed=None, clicked=None,
                 double_clicked=None, selected=None, **kwargs):
        super().__init__(**kwargs)
        self.header = header or []

        self.activated = activated
        def activated_event(item, index):
            if callable(self.activated):
                data = item.data(0, item.UserType)
                if data is not None:
                    self.activated(index, data)
        self.qt.itemActivated.connect(activated_event)

        self.changed = changed
        def changed_event(item, index):
            if callable(self.changed):
                data = item.data(0, item.UserType)
                if data is not None:
                    self.changed(index, data)
        self.qt.itemChanged.connect(changed_event)

        self.clicked = clicked
        def clicked_event(item, index):
            if callable(self.clicked):
                data = item.data(0, item.UserType)
                if data is not None:
                    self.clicked(index, data)
        self.qt.itemClicked.connect(clicked_event)

        self.double_clicked = double_clicked
        def double_clicked_event(item, index):
            if callable(self.double_clicked):
                data = item.data(0, item.UserType)
                if data is not None:
                    self.double_clicked(index, data)
        self.qt.itemDoubleClicked.connect(double_clicked_event)

        self.selected = selected
        def selected_event():
            if callable(self.selected):
                items = self.qt.selectedItems()
                if items:
                    first = items[0].data(0, items[0].UserType)
                    self.selected(first)
        self.qt.itemSelectionChanged.connect(selected_event)

    @property
    def header(self):
        return self.qt.headerLabels()

    @header.setter
    def header(self, items):
        self.qt.setColumnCount(len(items))
        self.qt.setHeaderLabels(items)

    def append(self, item):
        """Append item or item labels, returns appended item.
        >>> tree.append(TreeItem(["Spam", "Eggs"]))
        or
        >>> tree.append(["Spam", "Eggs"])
        """
        if not isinstance(item, TreeItem):
            item = TreeItem(item)
        self.qt.addTopLevelItem(item.qt)
        item.expanded = True
        return item

    def insert(self, index, item):
        """Insert item or item labels at index, returns inserted item.
        >>> tree.insert(0, TreeItem(["Spam", "Eggs"]))
        or
        >>> tree.insert(0, ["Spam", "Eggs"])
        """
        if not isinstance(item, TreeItem):
            item = TreeItem(item)
        self.qt.insertTopLevelItem(index, item.qt)
        item.expanded = True
        return item

    def clear(self):
        self.qt.clear()

    @property
    def current(self):
        """Returns current tree item or None."""
        item = self.qt.currentItem()
        if item is not None:
            return item.data(0, item.UserType)

    @property
    def stretch(self):
        return self.qt.header().stretchLastSection()

    @stretch.setter
    def stretch(self, state):
        self.qt.header().setStretchLastSection(state)

    def fit(self):
        for column in range(self.qt.columnCount()):
            self.qt.resizeColumnToContents(column)

    def __getitem__(self, index):
        item = self.qt.topLevelItem(index)
        return item.data(0, item.UserType)

    def __setitem__(self, index, items):
        self.qt.removeRow(row)
        self.qt.insertRow(row)
        for column, item in enumerate(items):
            if not isinstance(item, TableItem):
                item = TableItem(value=item)
            self.qt.setItem(row, column, item.qt)

    def __len__(self):
        return self.qt.topLevelItemCount()

    def __iter__(self):
        items = []
        for index in range(self.qt.topLevelItemCount()):
            items.append(self[index])
        return iter(items)

class TreeItem(Base):

    QtClass = QtWidgets.QTreeWidgetItem

    def __init__(self, values, **kwargs):
        super().__init__(**kwargs)
        self.qt._default_foreground = self.qt.foreground(0)
        self.qt._default_background = self.qt.background(0)
        for column, value in enumerate(values):
            self.qt.setData(column, self.qt.Type, value)
            self.qt.setData(column, self.qt.UserType, self)

    @property
    def children(self):
        items = []
        for index in range(self.qt.childCount()):
            item = self.qt.child(index)
            items.append(item.data(0, item.UserType))
        return items

    def append(self, item):
        if not isinstance(item, TreeItem):
            item = TreeItem(item)
        self.qt.addChild(item.qt)
        return item

    def insert(self, index, item):
        if not isinstance(item, TreeItem):
            item = TreeItem(item)
        self.qt.insertChild(index, item.qt)
        return item

    @property
    def expanded(self):
        return self.qt.isExpanded()

    @expanded.setter
    def expanded(self, expand):
        self.qt.setExpanded(expand)

    def __getitem__(self, index):
        return TreeItemColumn(index, self.qt)

class TreeItemColumn:

    def __init__(self, column, qt):
        self.column = column
        self.qt = qt

    @property
    def value(self):
        return self.qt.data(self.column, self.qt.Type)

    @value.setter
    def value(self, value):
        return self.qt.setData(self.column, self.qt.Type, value)

    @property
    def color(self):
        return self.qt.foreground(self.column).color().name()

    @color.setter
    def color(self, color):
        if color is None:
            brush = self.qt._default_foreground
        else:
            brush = self.qt.foreground(self.column)
            brush.setColor(QtGui.QColor(color))
        self.qt.setForeground(self.column, brush)

    @property
    def background(self):
        return self.qt.background(self.column).color().name()

    @background.setter
    def background(self, color):
        if color is None:
            brush = self.qt._default_background
        else:
            brush = self.qt.background(self.column)
            brush.setStyle(QtCore.Qt.SolidPattern)
            brush.setColor(QtGui.QColor(color))
        self.qt.setBackground(self.column, brush)

    @property
    def checked(self):
        return self.qt.checkState(self.column) == QtCore.Qt.Checked

    @checked.setter
    def checked(self, state):
        if state is None:
            flags = self.qt.flags() & ~QtCore.Qt.ItemIsUserCheckable
            self.qt.setFlags(flags)
        else:
            flags = self.qt.flags() | QtCore.Qt.ItemIsUserCheckable
            self.qt.setFlags(flags)
            self.qt.setCheckState(self.column, QtCore.Qt.Checked if state else QtCore.Qt.Unchecked)

    @property
    def checkable(self):
        return self.qt.flags() & ~QtCore.Qt.ItemIsUserCheckable

    @checkable.setter
    def checkable(self, state):
        if state:
            flags = self.qt.flags() | QtCore.Qt.ItemIsUserCheckable
        else:
            flags = self.qt.flags() & ~QtCore.Qt.ItemIsUserCheckable
        self.qt.setFlags(flags)

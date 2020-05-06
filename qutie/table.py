from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from .base import Base
from .icon import Icon
from .widget import BaseWidget

__all__ = ['Table']

class Table(BaseWidget):
    """Table
    >>> table = Table(header=["Key", "Value"])
    >>> table.append(["Spam", "Eggs"])
    >>> table.insert(["Ham", "Spam"])
    >>> for row in table:
    ...     for item in row:
    ...         item.color = "blue"
    >>> table.clear()
    """

    QtClass = QtWidgets.QTableWidget

    def __init__(self, header=None, rows=None, stretch=True, sortable=False,
                 activated=None, changed=None, clicked=None,
                 double_clicked=None, selected=None, **kwargs):
        super().__init__(**kwargs)
        self.header = header or []
        for row in rows or []:
            self.append(row)
        self.stretch = stretch
        self.sortable = sortable
        self.activated = activated
        def activated_event():
            if callable(self.activated):
                if callable(self.activated):
                    data = item.data(item.UserType)
                    if data is not None:
                        self.activated(data)
        self.qt.itemActivated.connect(activated_event)

        self.changed = changed
        def changed_event(item):
            if callable(self.changed):
                data = item.data(item.UserType)
                if data is not None:
                    self.changed(data)
        self.qt.itemChanged.connect(changed_event)

        self.clicked = clicked
        def clicked_event(item):
            if callable(self.clicked):
                data = item.data(item.UserType)
                if data is not None:
                    self.clicked(data)
        self.qt.itemClicked.connect(clicked_event)

        self.double_clicked = double_clicked
        def double_clicked_event(item):
            if callable(self.double_clicked):
                data = item.data(item.UserType)
                if data is not None:
                    self.double_clicked(data)
        self.qt.itemDoubleClicked.connect(double_clicked_event)

        self.selected = selected
        def selected_event():
            if callable(self.selected):
                data = self.qt.selectedItems()
                if data:
                    first = data[0].data(data[0].UserType)
                    self.selected(first)
        self.qt.itemSelectionChanged.connect(selected_event)

        self.qt.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.qt.horizontalHeader().setHighlightSections(False)
        self.qt.verticalHeader().setHighlightSections(False)
        self.vertical_header = False

    @property
    def header(self):
        """Horizontal header labels.

        >>> table.header = 'Key', 'Value'
        >>> table.header
        ('Key', 'Value')
        """
        return self.qt.horizontalHeaderLabels()

    @header.setter
    def header(self, value):
        self.qt.setColumnCount(len(value))
        self.qt.setHorizontalHeaderLabels(value)

    @property
    def vertical_header(self):
        return self.qt.verticalHeader().visible()

    @vertical_header.setter
    def vertical_header(self, value):
        self.qt.verticalHeader().setVisible(value)

    @property
    def sortable(self):
        return self.qt.isSortingEnabled()

    @sortable.setter
    def sortable(self, value):
        return self.qt.setSortingEnabled(value)

    def append(self, items):
        """Append items, returns appended items.

        >>> table.append(TableItem(value="Spam"), TableItem(value="Eggs"))
        or
        >>> table.append(["Spam", "Eggs"])
        """
        row = self.qt.rowCount()
        self.qt.setRowCount(self.qt.rowCount() + 1)
        return self.insert(row, items)

    def insert(self, row, items):
        """Insert items at row, returns inserted items.

        >>> table.insert(0, TableItem(value="Spam"), TableItem(value="Eggs"))
        or
        >>> table.insert(0, ["Spam", "Eggs"])
        """
        for column, item in enumerate(items):
            if not isinstance(item, TableItem):
                item = TableItem(value=item)
            self.qt.setItem(row, column, item.qt)
            self.qt.resizeRowToContents(row)
        return self[row]

    def clear(self):
        self.qt.clearContents()

    @property
    def current(self):
        """Returns current table item or None."""
        item = self.qt.currentItem()
        if item is not None:
            return item.data(item.UserType)

    @property
    def stretch(self):
        """Stretch last column.

        >>> table.stretch = True
        >>> table.stretch
        True
        """
        return self.qt.horizontalHeader().stretchLastSection()

    @stretch.setter
    def stretch(self, value):
        self.qt.horizontalHeader().setStretchLastSection(value)

    def fit(self):
        self.qt.resizeColumnsToContents()
        self.qt.resizeRowsToContents()

    def __getitem__(self, row):
        items = []
        for column in range(self.qt.columnCount()):
            item = self.qt.item(row, column)
            items.append(item.data(item.UserType) if item is not None else item)
        return items

    def __setitem__(self, row, items):
        self.qt.removeRow(row)
        self.qt.insertRow(row)
        for column, item in enumerate(items):
            if not isinstance(item, TableItem):
                item = TableItem(value=item)
            self.qt.setItem(row, column, item.qt)

    def __len__(self):
        return self.qt.rowCount()

    def __iter__(self):
        rows = []
        for row in range(self.qt.rowCount()):
            rows.append(self[row])
        return iter(rows)

class TableItem(Base):

    QtClass = QtWidgets.QTableWidgetItem

    def __init__(self, value=None, color=None, background=None, icon=None,
                 enabled=True, readonly=True, checked=None, checkable=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.qt.setData(self.qt.UserType, self)
        self.__default_foreground = self.qt.foreground()
        self.__default_background = self.qt.background()
        self.value = value
        self.color = color
        self.background = background
        if icon is not None:
            self.icon = icon
        self.enabled = enabled
        self.readonly = readonly
        if checkable is not None:
            self.checkable = checkable
        if checked is not None:
            self.checked = checked

    @property
    def value(self):
        return self.qt.data(self.qt.Type)

    @value.setter
    def value(self, value):
        return self.qt.setData(self.qt.Type, value)

    @property
    def color(self):
        return self.qt.foreground().color().name()

    @color.setter
    def color(self, value):
        if value is None:
            brush = self.__default_foreground
        else:
            brush = self.qt.foreground()
            brush.setColor(QtGui.QColor(value))
        self.qt.setForeground(brush)

    @property
    def background(self):
        return self.qt.background().color().name()

    @background.setter
    def background(self, value):
        if value is None:
            brush = self.__default_background
        else:
            brush = self.qt.background()
            brush.setStyle(QtCore.Qt.SolidPattern)
            brush.setColor(QtGui.QColor(value))
        self.qt.setBackground(brush)

    @property
    def icon(self):
        icon = self.qt.icon()
        if icon.isNull():
            return None
        return Icon(icon)

    @icon.setter
    def icon(self, value):
        if value is None:
            self.qt.setIcon(QtGui.QIcon())
        else:
            if not isinstance(value, Icon):
                value = Icon(value)
            self.qt.setIcon(value.qt)

    @property
    def enabled(self):
        return bool(self.qt.flags() & QtCore.Qt.ItemIsEnabled)

    @enabled.setter
    def enabled(self, value):
        if value:
            self.qt.setFlags(self.qt.flags() | QtCore.Qt.ItemIsEnabled)
        else:
            self.qt.setFlags(self.qt.flags() & ~QtCore.Qt.ItemIsEnabled)

    @property
    def readonly(self):
        return bool(self.qt.flags() & QtCore.Qt.ItemIsEditable)

    @readonly.setter
    def readonly(self, value):
        if value:
            self.qt.setFlags(self.qt.flags() & ~QtCore.Qt.ItemIsEditable)
        else:
            self.qt.setFlags(self.qt.flags() | QtCore.Qt.ItemIsEditable)

    @property
    def checked(self):
        return self.qt.checkState() == QtCore.Qt.Checked

    @checked.setter
    def checked(self, value):
        if value is None:
            flags = self.qt.flags() & ~QtCore.Qt.ItemIsUserCheckable
            self.qt.setFlags(flags)
        else:
            self.qt.setCheckState(QtCore.Qt.Checked if value else QtCore.Qt.Unchecked)

    @property
    def checkable(self):
        return self.qt.flags() & QtCore.Qt.ItemIsUserCheckable == True

    @checkable.setter
    def checkable(self, value):
        if value:
            flags = self.qt.flags() | QtCore.Qt.ItemIsUserCheckable
        else:
            flags = self.qt.flags() & ~QtCore.Qt.ItemIsUserCheckable
        self.qt.setFlags(flags)
        self.qt.setCheckState(self.checked)

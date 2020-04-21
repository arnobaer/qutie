from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

__all__ = [
    'Widget',
]

def to_alignment(alignment):
    return {
        "left": QtCore.Qt.AlignLeft,
        "right": QtCore.Qt.AlignRight,
        "top": QtCore.Qt.AlignTop,
        "bottom": QtCore.Qt.AlignBottom,
        "center": QtCore.Qt.AlignCenter
    }[alignment]

def from_alignment(alignment):
    return {
        QtCore.Qt.AlignLeft: "left",
        QtCore.Qt.AlignRight: "right",
        QtCore.Qt.AlignTop: "top",
        QtCore.Qt.AlignBottom: "bottom",
        QtCore.Qt.AlignHCenter: "hcenter",
        QtCore.Qt.AlignVCenter: "vcenter",
        QtCore.Qt.AlignCenter: "center"
    }[alignment]

class Base:

    QtClass = None

    def __init__(self, *args):
        self.__qt = self.QtClass(*args)
        self.__qt.setProperty("qt", self)

    @property
    def qt(self):
        return self.__qt

class BaseWidget(Base):

    QtClass = QtWidgets.QWidget

    def __init__(self, *, title=None, width=None, height=None, enabled=None,
                 visible=None, tooltip=None, tooltip_duration=None):
        super().__init__()
        self.title = title or ""
        self.width = width or 0
        self.height = height or 0
        if visible is not None:
            self.visible = visible
        if enabled is not None:
            self.enabled = enabled
        if tooltip is not None:
            self.tooltip = tooltip
        if tooltip_duration is not None:
            self.tooltip_duration = tooltip_duration

    @property
    def parent(self):
        if self.qt.parent() is not None:
            return self.qt.parent().property("qt")
        return None

    @property
    def title(self):
        return self.qt.windowTitle()

    @title.setter
    def title(self, title):
        self.qt.setWindowTitle(title)

    @property
    def width(self):
        return self.qt.width()

    @width.setter
    def width(self, width):
        self.qt.setMinimumWidth(width)

    @property
    def height(self):
        return self.qt.height()

    @height.setter
    def height(self, height):
        self.qt.setMinimumHeight(height)

    @property
    def size(self):
        return self.width, self.height

    @size.setter
    def size(self, size):
        self.width = size[0]
        self.height = size[1]

    @property
    def enabled(self):
        return self.qt.isEnabled()

    @enabled.setter
    def enabled(self, enabled):
        self.qt.setEnabled(enabled)

    @property
    def visible(self):
        return self.qt.visible()

    @visible.setter
    def visible(self, visible):
        self.qt.setVisible(visible)

    @property
    def tooltip(self):
        return self.qt.toolTip()

    @tooltip.setter
    def tooltip(self, tooltip):
        self.qt.setToolTip(tooltip)

    @property
    def tooltip_duration(self):
        return self.qt.toolTipDuration()

    @tooltip_duration.setter
    def tooltip_duration(self, duration):
        self.qt.setToolTipDuration(duration)

    def close(self):
        self.qt.close()

    def update(self):
        self.qt.update()

class Widget(BaseWidget):

    QtLayoutClass = QtWidgets.QVBoxLayout

    def __init__(self, *, layout=None, **kwargs):
        super().__init__(**kwargs)
        self.qt.setLayout(self.QtLayoutClass())
        #self.qt.layout().setContentsMargins(0, 0, 0, 0)
        if layout is not None:
            self.layout = layout

    @property
    def layout(self):
        if self.qt.layout().count():
            return self.qt.layout().itemAt(0).widget().property("qt")
        return None

    @layout.setter
    def layout(self, layout):
        while self.qt.layout().count():
            self.qt.layout().takeAt(0)
        if layout is not None:
            if not isinstance(layout, BaseWidget):
                raise ValueError(layout)
            self.qt.layout().addWidget(layout.qt)

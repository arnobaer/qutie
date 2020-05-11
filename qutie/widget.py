from PyQt5 import QtWidgets

from .icon import Icon
from .object import Object

__all__ = [
    'Widget',
]

class BaseWidget(Object):
    """Base widget for components without layout."""

    QtClass = QtWidgets.QWidget

    def __init__(self, *, title=None, width=None, height=None, enabled=None,
                 visible=None, stylesheet=None, icon=None, tooltip=None,
                 tooltip_duration=None, close_event=None, **kwargs):
        super().__init__(**kwargs)
        if title is not None:
            self.title = title
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if visible is not None:
            self.visible = visible
        if enabled is not None:
            self.enabled = enabled
        if stylesheet is not None:
            self.stylesheet = stylesheet
        if icon is not None:
            self.icon = icon
        if tooltip is not None:
            self.tooltip = tooltip
        if tooltip_duration is not None:
            self.tooltip_duration = tooltip_duration

        # Overwrite slot closeEvent
        self.close_event = close_event
        def closeEvent(event):
            if callable(self.close_event):
                if self.close_event() == False:
                    event.ignore()
                    return
            super(type(self.qt), self.qt).closeEvent(event)
        self.qt.closeEvent = closeEvent

    @property
    def title(self):
        return self.qt.windowTitle()

    @title.setter
    def title(self, value):
        self.qt.setWindowTitle(value)

    @property
    def width(self):
        return self.qt.width()

    @property
    def minimum_width(self):
        return self.qt.minimumWidth()

    @minimum_width.setter
    def minimum_width(self, value):
        self.qt.setMinimumWidth(value)

    @property
    def maximum_width(self):
        return self.qt.maximumWidth()

    @maximum_width.setter
    def maximum_width(self, value):
        self.qt.setMaximumWidth(value)

    @width.setter
    def width(self, value):
        if value is None:
            self.qt.setMinimumWidth(0)
            self.qt.setMaximumWidth(QtWidgets.QWIDGETSIZE_MAX)
        else:
            self.qt.setMinimumWidth(value)
            self.qt.setMaximumWidth(value)

    @property
    def height(self):
        return self.qt.height()

    @property
    def minimum_height(self):
        return self.qt.minimumHeight()

    @minimum_height.setter
    def minimum_height(self, value):
        self.qt.setMinimumHeight(value)

    @property
    def maximum_height(self):
        return self.qt.maximumHeight()

    @maximum_height.setter
    def maximum_height(self, value):
        self.qt.setMaximumHeight(value)

    @height.setter
    def height(self, value):
        if value is None:
            self.qt.setMinimumHeight(0)
            self.qt.setMaximumHeight(QtWidgets.QWIDGETSIZE_MAX)
        else:
            self.qt.setMinimumHeight(value)
            self.qt.setMaximumHeight(value)

    @property
    def size(self):
        return self.width, self.height

    @size.setter
    def size(self, value):
        self.width = value[0]
        self.height = value[1]

    @property
    def minimum_size(self):
        return self.qt.minimumWidth(), self.qt.minimumHeight()

    @minimum_size.setter
    def minimum_size(self, value):
        return self.qt.setMinimumSize(value[0], value[1])

    @property
    def maximum_size(self):
        return self.qt.maximumWidth(), self.qt.maximumHeight()

    @maximum_size.setter
    def maximum_size(self, value):
        return self.qt.setMaximumSize(value[0], value[1])

    @property
    def position(self):
        return self.qt.x(), self.qt.y()


    @property
    def minimized(self):
        return self.qt.isMinimized()

    @minimized.setter
    def minimized(self, value):
        if value:
            self.qt.showMinimized()
        else:
            self.qt.showNormal()

    @property
    def maximized(self):
        return self.qt.isMaximized()

    @maximized.setter
    def maximized(self, value):
        if value:
            self.qt.showMaximized()
        else:
            self.qt.showNormal()

    @property
    def enabled(self):
        return self.qt.isEnabled()

    @enabled.setter
    def enabled(self, value):
        self.qt.setEnabled(value)

    @property
    def visible(self):
        return self.qt.visible()

    @visible.setter
    def visible(self, value):
        self.qt.setVisible(value)

    @property
    def stylesheet(self):
        return self.qt.styleSheet()

    @stylesheet.setter
    def stylesheet(self, value):
        self.qt.setStyleSheet(value)

    @property
    def icon(self):
        icon = self.qt.windowIcon()
        if icon.isNull():
            return None
        return Icon(icon)

    @icon.setter
    def icon(self, value):
        if value is None:
            self.qt.setWindowIcon(QtGui.QIcon())
        else:
            if not isinstance(value, Icon):
                value = Icon(value)
            self.qt.setWindowIcon(value.qt)

    @property
    def tooltip(self):
        return self.qt.toolTip()

    @tooltip.setter
    def tooltip(self, value):
        self.qt.setToolTip(value)

    @property
    def tooltip_duration(self):
        """Tooltip duration in seconds. Minimum duration is 1 millisecond."""
        return self.qt.toolTipDuration() / 1000.

    @tooltip_duration.setter
    def tooltip_duration(self, value):
        self.qt.setToolTipDuration(value * 1000.)

    def close(self):
        self.qt.close()

    def update(self):
        self.qt.update()

    def show(self):
        self.qt.show()

    def hide(self):
        self.qt.hide()

    def resize(self, width, height):
        self.qt.resize(width, height)

    def move(self, x, y):
        self.qt.move(x, y)

class Widget(BaseWidget):
    """Widget for components with layout."""

    QtLayoutClass = QtWidgets.QVBoxLayout

    def __init__(self, *, layout=None, modal=False, **kwargs):
        super().__init__(**kwargs)
        self.qt.setLayout(self.QtLayoutClass())
        if layout is not None:
            self.layout = layout

    @property
    def layout(self):
        layout = self.qt.layout()
        if layout is not None:
            if layout.count():
                return layout.itemAt(0).widget().property(self.QtProperty)
        return None

    @layout.setter
    def layout(self, value):
        while self.qt.layout().count():
            self.qt.layout().takeAt(0)
        if value is not None:
            if not isinstance(value, BaseWidget):
                raise ValueError(value)
            self.qt.layout().addWidget(value.qt)

    @property
    def modal(self):
        return self.qt.isModal()

    @modal.setter
    def modal(self, value):
        self.qt.setModal(value)

from PyQt5 import QtWidgets

from .object import Object

__all__ = [
    'Widget',
]

class BaseWidget(Object):
    """Base widget for components without layout."""

    QtClass = QtWidgets.QWidget

    def __init__(self, *, title=None, width=None, height=None, enabled=None,
                 visible=None, stylesheet=None, tooltip=None,
                 tooltip_duration=None, **kwargs):
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
        if tooltip is not None:
            self.tooltip = tooltip
        if tooltip_duration is not None:
            self.tooltip_duration = tooltip_duration

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
        if width is None:
            self.qt.setMinimumWidth(0)
            self.qt.setMaximumWidth(QtWidgets.QWIDGETSIZE_MAX)
        else:
            self.qt.setMinimumWidth(width)
            self.qt.setMaximumWidth(width)

    @property
    def height(self):
        return self.qt.height()

    @height.setter
    def height(self, height):
        if width is None:
            self.qt.setMinimumHeight(0)
            self.qt.setMaximumHeight(QtWidgets.QWIDGETSIZE_MAX)
        else:
            self.qt.setMinimumHeight(height)
            self.qt.setMaximumHeight(height)

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
    def stylesheet(self):
        return self.qt.styleSheet()

    @stylesheet.setter
    def stylesheet(self, stylesheet):
        self.qt.setStyleSheet(stylesheet)

    @property
    def tooltip(self):
        return self.qt.toolTip()

    @tooltip.setter
    def tooltip(self, tooltip):
        self.qt.setToolTip(tooltip)

    @property
    def tooltip_duration(self):
        """Tooltip duration in seconds. Minimum duration is 1 millisecond."""
        return self.qt.toolTipDuration() / 1000.

    @tooltip_duration.setter
    def tooltip_duration(self, duration):
        self.qt.setToolTipDuration(duration * 1000.)

    def close(self):
        self.qt.close()

    def update(self):
        self.qt.update()

    def show(self):
        self.qt.show()

    def hide(self):
        self.qt.hide()

class Widget(BaseWidget):
    """Widget for components with layout."""

    QtLayoutClass = QtWidgets.QVBoxLayout

    def __init__(self, *, layout=None, **kwargs):
        super().__init__(**kwargs)
        self.qt.setLayout(self.QtLayoutClass())
        if layout is not None:
            self.layout = layout

    @property
    def layout(self):
        if self.qt.layout() is not None:
            if self.qt.layout().count():
                return self.qt.layout().itemAt(0).widget().property(self.QtProperty)
        return None

    @layout.setter
    def layout(self, layout):
        while self.qt.layout().count():
            self.qt.layout().takeAt(0)
        if layout is not None:
            if not isinstance(layout, BaseWidget):
                raise ValueError(layout)
            self.qt.layout().addWidget(layout.qt)

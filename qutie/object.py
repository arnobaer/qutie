from PyQt5 import QtCore

from .base import Base

__all__ = [
    'Object',
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

class Object(Base):
    """Object as base for all components."""

    QtClass = QtCore.QObject
    QtProperty = "qt"

    def __init__(self, *args, destroyed=None, object_name_changed=None):
        super().__init__(*args)
        self.qt.setProperty(self.QtProperty, self)

        self.destroyed = destroyed
        def destroyed_event(obj):
            if callable(self.destroyed):
                self.destroyed(obj.property(self.QtProperty))
        self.qt.destroyed.connect(destroyed_event)

        self.object_name_changed = object_name_changed
        def object_name_changed_event():
            if callable(self.destroyed):
                self.destroyed(self.object_name)
        self.qt.objectNameChanged.connect(object_name_changed_event)

    @property
    def object_name(self):
        return self.qt.objectName()

    @object_name.setter
    def object_name(self, value):
        self.qt.setObjectName(value)

    @property
    def parent(self):
        if self.qt.parent() is not None:
            return self.qt.parent().property(self.QtProperty)
        return None

    @property
    def children(self):
        return self.qt.children()

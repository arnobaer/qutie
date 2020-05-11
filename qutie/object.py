from PyQt5 import QtCore

from .base import Base

__all__ = [
    'Object',
]

class EventMixin:

    eventTriggered = QtCore.pyqtSignal(str, object, object)

class QObject(QtCore.QObject, EventMixin):

    pass

class Object(Base):
    """Object as base for all components."""

    QtClass = QObject
    QtProperty = "qt"

    def __init__(self, *args, destroyed=None, object_name_changed=None):
        super().__init__(*args)
        self.qt.setProperty(self.QtProperty, self)
        #self.qt.eventTriggered = QtCore.pyqtSignal(str, object, object)

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

        if hasattr(self.qt, 'eventTriggered'):
            def trigger_event(name, args, kwargs):
                if hasattr(self, name):
                    attr = getattr(self, name)
                    if callable(attr):
                        attr(*args, **kwargs)
            self.qt.eventTriggered.connect(trigger_event)

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

    def emit(self, _, *args, **kwargs):
        """Emit custom user event."""
        if hasattr(self.qt, 'eventTriggered'):
            self.qt.eventTriggered.emit(_, args, kwargs)

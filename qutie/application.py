import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from .icon import Icon
from .object import Object

__all__ = ['Application']

class CoreApplication(Object):

    QtClass = QtCore.QCoreApplication

    def __init__(self, name=None, *, version=None, organization=None,
                 domain=None, name_changed=None, version_changed=None,
                 organization_changed=None, domain_changed=None):
        super().__init__(sys.argv)
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if organization is not None:
            self.organization = organization
        if domain is not None:
            self.domain = domain

        self.name_changed = name_changed
        def name_changed_event():
            if callable(self.name_changed):
                self.name_changed(self.name)
        self.qt.applicationNameChanged.connect(name_changed_event)

        self.version_changed = version_changed
        def version_changed_event(*args, **kwargs):
            if callable(self.version_changed):
                self.version_changed(*args, **kwargs)
        self.qt.applicationVersionChanged.connect(version_changed_event)

        self.organization_changed = organization_changed
        def organization_changed_event(*args, **kwargs):
            if callable(self.organization_changed):
                self.organization_changed(*args, **kwargs)
        self.qt.organizationNameChanged.connect(organization_changed_event)

        self.domain_changed = domain_changed
        def domain_changed_event(*args, **kwargs):
            if callable(self.domain_changed):
                self.domain_changed(*args, **kwargs)
        self.qt.organizationDomainChanged.connect(domain_changed_event)

    @classmethod
    def instance(self):
        if self.QtClass.instance() is not None:
            return self.QtClass.instance().property(self.QtProperty)
        return None

    @property
    def name(self):
        return self.qt.applicationName()

    @name.setter
    def name(self, value):
        self.qt.setApplicationName(value)

    @property
    def version(self):
        return self.qt.applicationVersion()

    @version.setter
    def version(self, value):
        self.qt.setApplicationVersion(value)

    @property
    def organization(self):
        return self.qt.organizationName()

    @organization.setter
    def organization(self, value):
        self.qt.setOrganizationName(value)

    @property
    def domain(self):
        return self.qt.organizationDomain()

    @domain.setter
    def domain(self, value):
        self.qt.setOrganizationDomain(value)

    def run(self):
        return self.qt.exec_()

    def quit(self):
        self.qt.quit()

class GuiApplication(CoreApplication):

    QtClass = QtGui.QGuiApplication

    def __init__(self, name=None, *, display_name=None, icon=None,
                 display_name_changed=None, last_window_closed=None, **kwargs):
        super().__init__(name=name, **kwargs)
        if display_name is not None:
            self.display_name = display_name
        if icon is not None:
            self.icon = icon

        self.display_name_changed = display_name_changed
        def display_name_changed_event():
            if callable(self.display_name_changed):
                self.display_name_changed(self.display_name)
        self.qt.applicationDisplayNameChanged.connect(display_name_changed_event)

        self.last_window_closed = last_window_closed
        def last_window_closed_event():
            if callable(self.last_window_closed):
                self.last_window_closed()
        self.qt.lastWindowClosed.connect(last_window_closed_event)

    @property
    def display_name(self):
        return self.qt.applicationDisplayName()

    @display_name.setter
    def display_name(self, value):
        self.qt.setApplicationDisplayName(value)

    @property
    def icon(self):
        return Icon._from_qt(self.qt.windowIcon())

    @icon.setter
    def icon(self, value):
        if value is None:
            self.qt.setWindowIcon(QtGui.QIcon())
        else:
            if not isinstance(value, Icon):
                value = Icon(value)
            self.qt.setWindowIcon(value.qt)


class Application(GuiApplication):

    QtClass = QtWidgets.QApplication

    def __init__(self, name=None, *, focus_changed=None, **kwargs):
        super().__init__(name=name, **kwargs)

        self.focus_changed = focus_changed
        def focus_changed_event(old, now):
            if callable(self.focus_changed):
                self.focus_changed(old, now)
        self.qt.focusChanged.connect(focus_changed_event)

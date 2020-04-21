import sys

from PyQt5 import QtWidgets

from .base import Base

__all__ = ['Application']

class Application(Base):

    QtClass = QtWidgets.QApplication

    def __init__(self, *, name=None, version=None):
        super().__init__(sys.argv)
        self.name = name or ""
        self.version = version or ""

    @property
    def name(self):
        return self.qt.applicationName()

    @name.setter
    def name(self, name):
        self.qt.setApplicationName(name)

    @property
    def version(self):
        return self.qt.applicationVersion()

    @version.setter
    def version(self, version):
        self.qt.setApplicationVersion(version)

    def run(self):
        return self.qt.exec_()

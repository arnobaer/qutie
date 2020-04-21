from PyQt5 import QtWidgets

from .base import Widget

__all__ = ['Dialog']

class Dialog(Widget):

    QtClass = QtWidgets.QDialog

    def __init__(self, *, modal=None, **kwargs):
        super().__init__(**kwargs)
        self.modal = modal or False

    @property
    def modal(self):
        return self.qt.isModal()

    @modal.setter
    def modal(self, modal):
        self.qt.setModal(modal)

    def run(self):
        return self.qt.exec_()

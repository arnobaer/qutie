from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget, Widget

__all__ = ['Dialog', 'DialogButtonBox']

class Dialog(Widget):

    QtClass = QtWidgets.QDialog

    def __init__(self, *, accepted=None, rejected=None, **kwargs):
        super().__init__(**kwargs)

        self.accepted = accepted
        def accepted_event():
            if callable(self.accepted):
                self.accepted()
        self.qt.accepted.connect(accepted_event)

        self.rejected = rejected
        def rejected_event():
            if callable(self.rejected):
                self.rejected()
        self.qt.rejected.connect(rejected_event)

    def accept(self):
        return self.qt.accept()

    def reject(self):
        return self.qt.reject()

    def run(self):
        return {
            self.qt.Accepted: True,
            self.qt.Rejected: False
        }[self.qt.exec_()]

class DialogButtonBox(BaseWidget):

    QtClass = QtWidgets.QDialogButtonBox
    QtStandardButtons = {
        'ok': QtWidgets.QDialogButtonBox.Ok,
        'open': QtWidgets.QDialogButtonBox.Open,
        'save': QtWidgets.QDialogButtonBox.Save,
        'cancel': QtWidgets.QDialogButtonBox.Cancel,
        'close': QtWidgets.QDialogButtonBox.Close,
        'discard': QtWidgets.QDialogButtonBox.Discard,
        'apply': QtWidgets.QDialogButtonBox.Apply,
        'reset': QtWidgets.QDialogButtonBox.Reset,
        'restore_defaults': QtWidgets.QDialogButtonBox.RestoreDefaults,
        'help': QtWidgets.QDialogButtonBox.Help,
        'save_all': QtWidgets.QDialogButtonBox.SaveAll,
        'yes': QtWidgets.QDialogButtonBox.Yes,
        'yes_to_all': QtWidgets.QDialogButtonBox.YesToAll,
        'no': QtWidgets.QDialogButtonBox.No,
        'no_to_all': QtWidgets.QDialogButtonBox.NoToAll,
        'abort': QtWidgets.QDialogButtonBox.Abort,
        'retry': QtWidgets.QDialogButtonBox.Retry,
        'ignore': QtWidgets.QDialogButtonBox.Ignore
    }

    def __init__(self, buttons=None, orientation=None, accepted=None,
                 rejected=None, clicked=None, help_requested=None, **kwargs):
        super().__init__(**kwargs)
        if buttons is not None:
            self.buttons = buttons
        if orientation is not None:
            self.orientation = orientation

        self.accepted = accepted
        def accepted_event():
            if callable(self.accepted):
                self.accepted()
        self.qt.accepted.connect(accepted_event)

        self.rejected = rejected
        def rejected_event():
            if callable(self.rejected):
                self.rejected()
        self.qt.rejected.connect(rejected_event)

        self.clicked = clicked
        def clicked_event(button):
            if callable(self.clicked):
                button = self.qt.standardButton(button)
                for key, value in self.QtStandardButtons.items():
                    if button == value:
                        self.clicked(key)
                        break
        self.qt.clicked.connect(clicked_event)

        self.help_requested = help_requested
        def help_requested_event():
            if callable(self.help_requested):
                self.help_requested()
        self.qt.helpRequested.connect(help_requested_event)

    @property
    def buttons(self):
        buttons = []
        values = self.qt.standardButtons()
        for key, mask in self.QtStandardButtons.items():
            if values & mask:
                buttons.append(key)
        return tuple(buttons)

    @buttons.setter
    def buttons(self, value):
        buttons = 0
        for button in value:
            buttons |= self.QtStandardButtons.get(button, 0)
        self.qt.setStandardButtons(buttons)

    @property
    def orientation(self):
        return {
            QtCore.Qt.Horizontal: 'horizontal',
            QtCore.Qt.Vertical: 'vertical'
        }[self.qt.orientation()]

    @orientation.setter
    def orientation(self, value):
        self.qt.setOrientation({
            'horizontal': QtCore.Qt.Horizontal,
            'vertical': QtCore.Qt.Vertical
        }[value])

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from .widget import BaseWidget, Widget

__all__ = [
    'Dialog',
    'DialogButtonBox',
    'filename_open',
    'filenames_open',
    'directory_open',
    'filename_save',
    'get_number',
    'get_text',
    'get_item'
]

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

def filename_open(path=None, *, filter=None, title=None):
    """Shows a filename selection dialog, returns selected filename path.

    >>> filename_open("/home/user", filter="Text (*.txt)")
    '/home/user/example.txt'
    """
    return QtWidgets.QFileDialog.getOpenFileName(None, title or "Open file", path, filter)[0] or None

def filenames_open(path=None, *, filter=None, title=None):
    """Shows a multiple filenames selection dialog, returns list of selected
    filename paths.

    >>> filename_open("/home/user", filter="Text (*.txt)")
    ['/home/user/example.txt', '/home/user/another.txt']
    """
    return QtWidgets.QFileDialog.getOpenFileNames(None, title or "Open files", path, filter)[0] or None

def directory_open(path=None, *, title=None):
    """Shows a multiple filenames selection dialog, returns selected directory
    path.

    >>> filename_open(""/home/user")
    '/tmp'
    """
    return QtWidgets.QFileDialog.getExistingDirectory(None, title or "Open directory", path) or None

def filename_save(path=None, *, filter=None, title=None):
    """Shows a save filename selection dialog, returns selected filename path.

    >>> filename_save("/home/user/example.txt", filter="Text (*.txt)")
    '/home/user/other.txt'
    """
    return QtWidgets.QFileDialog.getSaveFileName(None, title or "Save file", path, filter)[0] or None

def get_number(value=0, *, minimum=None, maximum=None, decimals=0, title=None, label=None):
    """Number input dialog, optionally editable.

    >>> get_number(value=4.2, minimum=0, maximum=10, decimals=1)
    'Pear'
    """
    value = float(value)
    if minimum is None:
        minimum = float('-inf')
    if maximum is None:
        maximum = float('-inf')
    if title is None:
        title = ""
    if label is None:
        label = ""
    value, success = QtWidgets.QInputDialog.getDouble(
        None, title, label, value, minimum, maximum, decimals
    )
    if success:
        return value
    return None

def get_text(text=None, *, title=None, label=None):
    """Text input dialog.

    >>> get_text()
    'Pear'
    """
    text = format(text)
    if title is None:
        title = ""
    if label is None:
        label = ""
    value, success = QtWidgets.QInputDialog.getText(
        None, title, label, QtWidgets.QLineEdit.Normal, text
    )
    if success:
        return value
    return None

def get_item(items, *, current=0, editable=False, title=None, label=None):
    """Select item from input list dialog, optionally editable.

    >>> get_item(["Apple", "Pear", "Nut"])
    'Pear'
    """
    items = [format(item) for item in items]
    if title is None:
        title = ""
    if label is None:
        label = ""
    item, success = QtWidgets.QInputDialog.getItem(
        None, title, label, items, current, editable
    )
    if success:
        return item
    return None

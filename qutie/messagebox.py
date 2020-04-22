from PyQt5 import QtCore, QtWidgets

from .widget import BaseWidget

__all__ = [
    'show_info',
    'show_warning',
    'show_error',
    'show_exception',
    'show_question'
]

class MessageBox(BaseWidget):
    """Custom message box helper class."""

    QtClass = QtWidgets.QMessageBox

    def __init__(self, icon=None, title=None, text=None, details=None, width=None, **kwargs):
        super().__init__(**kwargs)
        self._spacer_item = QtWidgets.QSpacerItem(320, 0)
        if icon is not None:
            self.qt.setIcon(icon)
        if title is not None:
            self.title = title
        if text is not None:
            self.qt.setText(text)
        if details is not None:
            self.qt.setDetailedText(details)
        self.width = width or 460
        layout = self.qt.layout()
        # Workaround to resize message box
        layout.addItem(self._spacer_item, layout.rowCount(), 0, 1, layout.columnCount())

    @property
    def width(self):
        return self.qt.width()

    @width.setter
    def width(self, width):
        self._spacer_item.changeSize(width, 0)

    def run(self):
        return self.qt.exec_()

def show_info(text, *, title=None, details=None, **kwargs):
    """Show information message box.
    >>> show_info("Info", "NO-body expects the Spanish Inquisition!")
    """
    dialog = MessageBox(QtWidgets.QMessageBox.Information, title, text, details, **kwargs)
    dialog.run()

def show_warning(text, *, title=None, details=None, **kwargs):
    """Show warning message box.
    >>> show_warning("Warning", "NO-body expects the Spanish Inquisition!")
    """
    dialog = MessageBox(QtWidgets.QMessageBox.Warning, title, text, details, **kwargs)
    dialog.run()

def show_error(text, *, title=None, details=None, **kwargs):
    """Show warning message box.
    >>> show_error("Error", "NO-body expects the Spanish Inquisition!")
    """
    dialog = MessageBox(QtWidgets.QMessageBox.Critical, title, text, details, **kwargs)
    dialog.run()

def show_exception(exception, tb=None, **kwargs):
    """Show exception message box including exception stack trace.
    >>> try:
    ...     foo()
    ... except NameError as e:
    ...     show_exception(e)
    """
    if not tb:
        tb = traceback.format_exc() or None
    show_error(title="An exception occured", text=format(exception), details=tb, **kwargs)

def show_question(text, *, title=None, details=None, **kwargs):
    """Show question message box, returns True for yes and False for no.
    >>> show_question("Question", "Fancy a cup of Yorkshire Tea?")
    True
    """
    dialog = MessageBox(QtWidgets.QMessageBox.Question, title, text, details, **kwargs)
    dialog.qt.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    print(dialog.width)
    return dialog.run() == QtWidgets.QMessageBox.Yes

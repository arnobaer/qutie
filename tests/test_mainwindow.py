import unittest

from qutie import MainWindow
from . import QutieTestCase

class MainWindowTest(QutieTestCase):

    def testEmpty(self):
        context = MainWindow()
        self.assertEqual(context.menubar.qt, context.qt.menuBar())
        self.assertEqual(context.statusbar.qt, context.qt.statusBar())

    def testFull(self):
        context = MainWindow()
        self.assertEqual(context.menubar.qt, context.qt.menuBar())
        self.assertEqual(context.statusbar.qt, context.qt.statusBar())

    def testProperties(self):
        context = MainWindow()

    def testMethods(self):
        context = MainWindow()

if __name__ == '__main__':
    unittest.main()

import unittest

from qutie import Label
from qutie import Pixmap
from . import QutieTestCase

class LabelTest(QutieTestCase):

    def testEmpty(self):
        context = Label()
        self.assertEqual(context.text, '')
        self.assertEqual(context.margin, 0)
        self.assertEqual(context.indent, -1)
        self.assertEqual(context.pixmap, None)

    def testFull(self):
        context = Label(
            text='lorem',
            margin=16,
            indent=32,
            pixmap='yellow'
        )
        context.qt.setText('lorem')
        self.assertEqual(context.text, 'lorem')
        self.assertEqual(context.margin, 16)
        self.assertEqual(context.indent, 32)
        self.assertEqual(context.pixmap, None)

    def testFullPixmap(self):
        context = Label(
            text='lorem', # ignored
            pixmap='yellow'
        )
        self.assertEqual(context.text, '')
        self.assertEqual(type(context.pixmap), Pixmap)

    def testProperties(self):
        context = Label()
        context.text = 'lorem'
        self.assertEqual(context.text, 'lorem')
        context.margin = 32
        self.assertEqual(context.margin, 32)
        context.indent = 16
        self.assertEqual(context.indent, 16)

    def testMethods(self):
        context = Label('lorem')
        context.clear()
        self.assertEqual(context.text, '')
        self.assertEqual(context.pixmap, None)
        context.pixmap = 'yellow'
        context.clear()
        self.assertEqual(context.text, '')
        self.assertEqual(context.pixmap, None)

if __name__ == '__main__':
    unittest.main()

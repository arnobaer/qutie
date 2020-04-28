import unittest

from qutie import Application
from qutie import Widget

class WidgetTest(unittest.TestCase):

    def setUp(self):
        self.app = Application.instance()
        if not self.app:
            self.app = Application()

    def testEmpty(self):
        widget = Widget()
        self.assertEqual(widget.title, '')
        self.assertEqual(widget.tooltip, '')

    def testFull(self):
        widget = Widget(title='title', tooltip='tooltip')
        self.assertEqual(widget.title, 'title')
        self.assertEqual(widget.tooltip, 'tooltip')

if __name__ == '__main__':
    unittest.main()

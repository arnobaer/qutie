import unittest

from qutie import Row, Column
from qutie import Widget
from . import QutieTestCase

class ColumnTest(QutieTestCase):

    LayoutClass = Column

    def testEmpty(self):
        context = self.LayoutClass()
        self.assertEqual(len(context), 0)
        self.assertEqual(list(context), [])
        self.assertEqual(context.stretch, [])

    def tesFull(self):
        items = [Widget(), Widget(), Widget()]
        context = self.LayoutClass(*items, stretch=[2, 3, 1])
        self.assertEqual(len(context), 3)
        self.assertEqual(list(context), items)
        self.assertEqual(context.stretch, [2, 3, 1])

    def testProperties(self):
        items = [Widget(), Widget(), Widget(), Widget()]
        context = self.LayoutClass(*items)
        context.stretch = (1, 2)
        self.assertEqual(context.stretch, [1, 2, 0, 0])

    def testMethods(self):
        context = self.LayoutClass()

class RowTest(ColumnTest):

    LayoutClass = Row

if __name__ == '__main__':
    unittest.main()

import unittest

from qutie import Tab
from qutie import Tabs
from . import QutieTestCase

class TabTest(QutieTestCase):

    def testEmpty(self):
        context = Tab()
        self.assertEqual(context.title, '')

    def testFull(self):
        context = Tab(title='title')
        self.assertEqual(context.title, 'title')

    def testProperties(self):
        context = Tabs()
        context.title = 'title'
        self.assertEqual(context.title, 'title')

class TabsTest(QutieTestCase):

    def testEmpty(self):
        context = Tabs()

    def testFull(self):
        items = [Tab(), Tab(), Tab()]
        context = Tabs(*items)

    def testProperties(self):
        items = [Tab(), Tab(), Tab()]
        context = Tabs(*items)
        self.assertEqual(context.items, items)

    def testMethods(self):
        items = [Tab(), Tab(), Tab()]
        context = Tabs()
        context.append(items[1])
        context.append(items[2])
        context.insert(0, items[0])
        self.assertEqual(context.items, items)
        self.assertEqual(context.index(items[1]), 1)
        context.clear()
        self.assertEqual(context.items, [])

if __name__ == '__main__':
    unittest.main()

import unittest

from qutie import List
from . import QutieTestCase

class ListTest(QutieTestCase):

    def testEmpty(self):
        context = List()
        self.assertEqual(context.items, [])
        self.assertEqual(len(context), 0)
        self.assertEqual(context.view_mode, 'list')
        self.assertEqual(context.resize_mode, 'fixed')

    def testFull(self):
        context = List(
            [2, 4, 7],
            view_mode='icon',
            resize_mode='adjust'
        )
        self.assertEqual([item.value for item in context.items], [2, 4, 7])
        self.assertEqual(len(context), 3)
        self.assertEqual(context.view_mode, 'icon')
        self.assertEqual(context.resize_mode, 'adjust')

    def testProperties(self):
        context = List()
        context.items = [8, 16]
        self.assertEqual(context.items[0].value, 8)
        self.assertEqual([item.value for item in context.items], [8, 16])
        self.assertEqual(len(context), 2)
        context.view_mode = 'icon'
        self.assertEqual(context.view_mode, 'icon')
        context.resize_mode = 'adjust'
        self.assertEqual(context.resize_mode, 'adjust')

    def testMethods(self):
        context = List([16])
        item = context.append(32)
        self.assertEqual(len(context), 2)
        item.value = 4.2
        self.assertEqual(item.value, 4.2)
        item.color = 'red'
        self.assertEqual(item.color, '#ff0000')
        item.background = 'blue'
        self.assertEqual(item.background, '#0000ff')
        context.insert(0, 8)
        self.assertEqual(len(context), 3)
        self.assertEqual([item.value for item in context.items], [8, 16, 4.2])
        self.assertEqual(context.index(context.items[1]), 1)
        context.clear()
        self.assertEqual(len(context), 0)
        self.assertEqual(context.items, [])


if __name__ == '__main__':
    unittest.main()

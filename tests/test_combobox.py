import unittest

from qutie import ComboBox
from . import QutieTestCase

class ComboBoxTest(QutieTestCase):

    def testEmpty(self):
        context = ComboBox()
        self.assertEqual(context.items, [])

    def testFull(self):
        context = ComboBox(
            items=[1, 2, 3]
        )
        self.assertEqual(context.items, [1, 2, 3])

    def testProperties(self):
        context = ComboBox()
        context.items = [4, 5, 6]
        self.assertEqual(context.items, [4, 5, 6])

    def testMethods(self):
        context = ComboBox([3, 4, 5])
        self.assertEqual(context.items, [3, 4, 5])
        context.clear()
        self.assertEqual(context.items, [])


if __name__ == '__main__':
    unittest.main()

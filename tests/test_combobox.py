import unittest

from qutie import ComboBox
from . import QutieTestCase

class ComboBoxTest(QutieTestCase):

    def testEmpty(self):
        context = ComboBox()
        self.assertEqual(len(context), 0)
        self.assertEqual(list(context), [])

    def testFull(self):
        context = ComboBox([1, 2, 3])
        self.assertEqual(len(context), 3)
        self.assertEqual(list(context), [1, 2, 3])

    def testProperties(self):
        context = ComboBox()
        context.extend([4, 5, 6])
        self.assertEqual(len(context), 3)
        self.assertEqual(list(context), [4, 5, 6])
        context[0] = 7
        context[-1] = 8
        self.assertEqual(list(context), [7, 5, 8])

    def testMethods(self):
        context = ComboBox([3, 4, 5])
        self.assertEqual(len(context), 3)
        self.assertEqual(list(context), [3, 4, 5])
        context.clear()
        self.assertEqual(len(context), 0)
        self.assertEqual(list(context), [])
        context.append(22)
        context.insert(-1, 21)
        context.insert(2, 23)
        self.assertEqual(len(context), 3)
        self.assertEqual(list(context), [21, 22, 23])
        context.append(24)
        self.assertEqual(len(context), 4)
        self.assertEqual(list(context), [21, 22, 23, 24])


if __name__ == '__main__':
    unittest.main()

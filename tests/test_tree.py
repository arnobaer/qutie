import unittest

from qutie import Tree
from . import QutieTestCase

class TreeTest(QutieTestCase):

    def testEmpty(self):
        context = Tree()
        self.assertEqual(context.header, tuple())

    def testFull(self):
        context = Tree(header=["foo", "bar"])
        self.assertEqual(context.header, ("foo", "bar"))

    def testProperties(self):
        context = Tree()
        context.header = "foo", "bar"
        self.assertEqual(context.header, ("foo", "bar"))

    def testMethods(self):
        context = Tree()

if __name__ == '__main__':
    unittest.main()

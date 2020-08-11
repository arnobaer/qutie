import unittest

from qutie import Table
from . import QutieTestCase

class TableTest(QutieTestCase):

    def testEmpty(self):
        context = Table()
        self.assertEqual(context.header, tuple())

    def testFull(self):
        context = Table(header=["foo", "bar"])
        self.assertEqual(context.header, ("foo", "bar"))

    def testProperties(self):
        context = Table()
        context.header = "foo", "bar"
        self.assertEqual(context.header, ("foo", "bar"))

    def testMethods(self):
        context = Table()

if __name__ == '__main__':
    unittest.main()

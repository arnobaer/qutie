import unittest

from qutie import Object
from . import QutieTestCase

class ObjectTest(QutieTestCase):

    def testEmpty(self):
        context = Object()
        self.assertEqual(context.object_name, '')

    def testFull(self):
        context = Object(
            object_name='object_name'
        )
        self.assertEqual(context.object_name, 'object_name')

if __name__ == '__main__':
    unittest.main()

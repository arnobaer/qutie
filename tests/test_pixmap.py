import unittest

from qutie import Pixmap
from . import QutieTestCase

class PixmapTest(QutieTestCase):

    def testEmpty(self):
        context = Pixmap()
        self.assertEqual(context.width, 0)
        self.assertEqual(context.height, 0)

    def testCreate(self):
        context = Pixmap.create(16, 32, 'red')
        self.assertEqual(context.width, 16)
        self.assertEqual(context.height, 32)

if __name__ == '__main__':
    unittest.main()

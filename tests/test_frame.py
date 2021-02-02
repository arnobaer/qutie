import unittest

from qutie import Frame
from . import QutieTestCase

class FrameTest(QutieTestCase):

    def testEmpty(self):
        context = Frame()
        self.assertEqual(context.frame_width, 0)
        self.assertEqual(context.line_width, 1)
        self.assertEqual(context.mid_line_width, 0)

    def testFull(self):
        context = Frame(line_width=2, mid_line_width=3)
        self.assertEqual(context.frame_width, 0)
        self.assertEqual(context.line_width, 2)
        self.assertEqual(context.mid_line_width, 3)

    def testProperties(self):
        context = Frame()
        context.line_width = 4
        self.assertEqual(context.line_width, 4)
        context.mid_line_width = 5
        self.assertEqual(context.mid_line_width, 5)

    def testMethods(self):
        context = Frame()

if __name__ == '__main__':
    unittest.main()

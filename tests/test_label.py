import unittest

from qutie import Label
from . import QutieTestCase

class LabelTest(QutieTestCase):

    def testEmpty(self):
        context = Label()
        self.assertEqual(context.text, '')

    def testFull(self):
        context = Label(
            text='text'
        )
        self.assertEqual(context.text, 'text')

if __name__ == '__main__':
    unittest.main()

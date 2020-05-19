import unittest

from qutie import CheckBox
from . import QutieTestCase

class CheckBoxTest(QutieTestCase):

    def testEmpty(self):
        context = CheckBox()
        self.assertEqual(context.text, '')
        self.assertEqual(context.checked, False)

    def testFull(self):
        context = CheckBox(
            text='text',
            checked=True
        )
        self.assertEqual(context.text, 'text')
        self.assertEqual(context.checked, True)

    def testProperties(self):
        context = CheckBox()

    def testMethods(self):
        context = CheckBox()

if __name__ == '__main__':
    unittest.main()

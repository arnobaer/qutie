import unittest

from qutie import Button
from . import QutieTestCase

class ButtonTest(QutieTestCase):

    def testEmpty(self):
        context = Button()
        self.assertEqual(context.text, '')
        self.assertEqual(context.tool_tip, '')
        self.assertEqual(context.checkable, False)
        self.assertEqual(context.checked, False)

    def testFull(self):
        context = Button(
            text='text',
            tool_tip='tool tip',
            checkable=True,
            checked=True
        )
        self.assertEqual(context.text, 'text')
        self.assertEqual(context.tool_tip, 'tool tip')
        self.assertEqual(context.checkable, True)
        self.assertEqual(context.checked, True)

if __name__ == '__main__':
    unittest.main()

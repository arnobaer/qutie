import unittest

from qutie import Application
from qutie import Button

class ButtonTest(unittest.TestCase):

    def setUp(self):
        self.app = Application.instance() or Application(name='unittest')

    def testEmpty(self):
        button = Button()
        self.assertEqual(button.text, '')
        self.assertEqual(button.tooltip, '')
        self.assertEqual(button.checkable, False)
        self.assertEqual(button.checked, False)

    def testFull(self):
        button = Button(text='text', tooltip='tooltip', checkable=True, checked=True)
        self.assertEqual(button.text, 'text')
        self.assertEqual(button.tooltip, 'tooltip')
        self.assertEqual(button.checkable, True)
        self.assertEqual(button.checked, True)

if __name__ == '__main__':
    unittest.main()

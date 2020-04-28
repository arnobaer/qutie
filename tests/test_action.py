import unittest

from qutie import Application
from qutie import Action

class ActionTest(unittest.TestCase):

    def setUp(self):
        self.app = Application.instance()
        if not self.app:
            self.app = Application()

    def testEmpty(self):
        action = Action()
        self.assertEqual(action.text, '')
        self.assertEqual(action.tooltip, '')
        self.assertEqual(action.shortcut, None)
        self.assertEqual(action.triggered, None)
        self.assertEqual(action.toggled, None)

    def testFull(self):
        def triggered(): pass
        def toggled(checked): pass
        action = Action(text='text', tooltip='tooltip', shortcut='Ctrl+O',
                        triggered=triggered, toggled=toggled)
        self.assertEqual(action.text, 'text')
        self.assertEqual(action.tooltip, 'tooltip')
        self.assertEqual(action.shortcut, 'Ctrl+O')
        self.assertEqual(action.triggered, triggered)
        self.assertEqual(action.toggled, toggled)

if __name__ == '__main__':
    unittest.main()

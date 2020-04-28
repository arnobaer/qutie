import unittest

from qutie import Application
from qutie import Action

class ActionTest(unittest.TestCase):

    def setUp(self):
        self.app = Application.instance() or Application(name='unittest')

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

    def testCheckedState(self):
        action = Action()
        self.assertEqual(action.checkable, False)
        self.assertEqual(action.checked, False)
        action = Action(checked=True)
        self.assertEqual(action.checkable, False)
        self.assertEqual(action.checked, False)
        action = Action(checkable=True)
        self.assertEqual(action.checkable, True)
        self.assertEqual(action.checked, False)
        action.checkable = False
        action.checked = True
        self.assertEqual(action.checkable, False)
        self.assertEqual(action.checked, False)
        action.checkable = True
        action.checked = True
        self.assertEqual(action.checkable, True)
        self.assertEqual(action.checked, True)
        action.trigger()
        self.assertEqual(action.checkable, True)
        self.assertEqual(action.checked, False)
        action.toggle()
        self.assertEqual(action.checkable, True)
        self.assertEqual(action.checked, True)

if __name__ == '__main__':
    unittest.main()

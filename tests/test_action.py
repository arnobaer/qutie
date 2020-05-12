import unittest

from qutie import Action
from . import QutieTestCase

class ActionTest(QutieTestCase):

    def testEmpty(self):
        context = Action()
        self.assertEqual(context.text, '')
        self.assertEqual(context.tool_tip, '')
        self.assertEqual(context.status_tip, '')
        self.assertEqual(context.shortcut, None)
        self.assertEqual(context.triggered, None)
        self.assertEqual(context.toggled, None)

    def testFull(self):
        def triggered(): pass
        def toggled(checked): pass
        context = Action(
            text='text',
            tool_tip='tool tip',
            status_tip='status tip',
            shortcut='Ctrl+O',
            triggered=triggered,
            toggled=toggled
        )
        self.assertEqual(context.text, 'text')
        self.assertEqual(context.tool_tip, 'tool tip')
        self.assertEqual(context.status_tip, 'status tip')
        self.assertEqual(context.shortcut, 'Ctrl+O')
        self.assertEqual(context.triggered, triggered)
        self.assertEqual(context.toggled, toggled)

    def testCheckedState(self):
        context = Action()
        self.assertEqual(context.checkable, False)
        self.assertEqual(context.checked, False)
        context = Action(checked=True)
        self.assertEqual(context.checkable, False)
        self.assertEqual(context.checked, False)
        context = Action(checkable=True)
        self.assertEqual(context.checkable, True)
        self.assertEqual(context.checked, False)
        context.checkable = False
        context.checked = True
        self.assertEqual(context.checkable, False)
        self.assertEqual(context.checked, False)
        context.checkable = True
        context.checked = True
        self.assertEqual(context.checkable, True)
        self.assertEqual(context.checked, True)
        context.trigger()
        self.assertEqual(context.checkable, True)
        self.assertEqual(context.checked, False)
        context.toggle()
        self.assertEqual(context.checkable, True)
        self.assertEqual(context.checked, True)

if __name__ == '__main__':
    unittest.main()

import unittest

from qutie import GroupBox
from . import QutieTestCase

class GroupBoxTest(QutieTestCase):

    def testEmpty(self):
        context = GroupBox()
        self.assertEqual(context.title, '')
        self.assertEqual(context.checkable, False)
        self.assertEqual(context.checked, False)
        self.assertEqual(context.flat, False)
        self.assertEqual(context.clicked, None)
        self.assertEqual(context.toggled, None)

    def testFull(self):
        def on_clicked(): pass
        def on_toggled(state): pass
        context = GroupBox(
            title='title',
            checkable=True,
            checked=True,
            flat=True,
            clicked=on_clicked,
            toggled=on_toggled
        )
        self.assertEqual(context.title, 'title')
        self.assertEqual(context.checkable, True)
        self.assertEqual(context.checked, True)
        self.assertEqual(context.flat, True)
        self.assertEqual(context.clicked, on_clicked)
        self.assertEqual(context.toggled, on_toggled)

    def testProperties(self):
        context = GroupBox()
        context.checkable = True
        self.assertEqual(context.checkable, True)
        context.checked = True
        self.assertEqual(context.checked, True)
        context.flat = True
        self.assertEqual(context.flat, True)

    def testMethods(self):
        context = GroupBox()

if __name__ == '__main__':
    unittest.main()

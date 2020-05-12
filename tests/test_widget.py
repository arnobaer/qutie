import unittest

from qutie import Widget
from . import QutieTestCase

class WidgetTest(QutieTestCase):

    def testEmpty(self):
        context = Widget()
        self.assertEqual(context.title, '')
        self.assertEqual(context.enabled, True)
        self.assertEqual(context.visible, False)
        self.assertEqual(context.tool_tip, '')
        self.assertEqual(context.status_tip, '')

    def testFull(self):
        context = Widget(
            title='title',
            enabled=False,
            visible=True,
            width=320,
            height=240,
            tool_tip='tool tip',
            status_tip='status tip'
        )
        self.assertEqual(context.title, 'title')
        self.assertEqual(context.enabled, False)
        self.assertEqual(context.visible, True)
        self.assertEqual(context.width, 320)
        self.assertEqual(context.height, 240)
        self.assertEqual(context.tool_tip, 'tool tip')
        self.assertEqual(context.status_tip, 'status tip')

if __name__ == '__main__':
    unittest.main()

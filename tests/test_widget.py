import unittest

from qutie import Icon
from qutie import Widget
from . import QutieTestCase

class WidgetTest(QutieTestCase):

    def testEmpty(self):
        context = Widget()
        self.assertEqual(context.title, '')
        self.assertEqual(context.enabled, True)
        self.assertEqual(context.visible, False)
        self.assertEqual(context.status_tip, '')
        self.assertEqual(context.stylesheet, '')
        self.assertEqual(context.icon, None)
        self.assertEqual(context.tool_tip, '')
        self.assertEqual(context.tool_tip_duration, -0.001)
        self.assertEqual(context.modal, False)
        self.assertEqual(context.close_event, None)

    def testFull(self):
        def on_close(): pass
        context = Widget(
            title='title',
            enabled=False,
            visible=True,
            width=320,
            height=240,
            status_tip='status tip',
            stylesheet='color:green;',
            icon='yellow',
            tool_tip='tool tip',
            tool_tip_duration=7,
            modal=True,
            close_event=on_close
        )
        self.assertEqual(context.title, 'title')
        self.assertEqual(context.width, 320)
        self.assertEqual(context.height, 240)
        self.assertEqual(context.enabled, False)
        self.assertEqual(context.visible, True)
        self.assertEqual(context.status_tip, 'status tip')
        self.assertEqual(context.stylesheet, 'color:green;')
        self.assertEqual(type(context.icon), Icon)
        self.assertEqual(context.tool_tip, 'tool tip')
        self.assertEqual(context.tool_tip_duration, 7.0)
        self.assertEqual(context.modal, True)
        self.assertEqual(context.close_event, on_close)

    def testProperties(self):
        context = Widget()
        context.title = 'title'
        self.assertEqual(context.title, 'title')
        context.title = 'title'
        self.assertEqual(context.title, 'title')
        context.size = 32, 64
        self.assertEqual(context.width, 32)
        self.assertEqual(context.height, 64)
        self.assertEqual(context.size, (32, 64))
        context.width = 16
        context.height = 32
        self.assertEqual(context.width, 16)
        self.assertEqual(context.height, 32)
        self.assertEqual(context.size, (16, 32))
        context.modal = True
        self.assertEqual(context.modal, True)
        context.modal = False
        self.assertEqual(context.modal, False)

    def testMethods(self):
        context = Widget()
        context.show()
        self.assertEqual(context.visible, True)
        context.hide()
        self.assertEqual(context.visible, False)
        context.move(16, 32)
        self.assertEqual(context.position, (16, 32))
        context.resize(32, 64)
        self.assertEqual(context.size, (32, 64))

if __name__ == '__main__':
    unittest.main()

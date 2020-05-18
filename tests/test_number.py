import unittest

from qutie import Number
from . import QutieTestCase

class NumberTest(QutieTestCase):

    def testEmpty(self):
        context = Number()
        self.assertEqual(context.value, 0)
        self.assertEqual(context.minimum, float('-inf'))
        self.assertEqual(context.maximum, float('+inf'))
        self.assertEqual(context.step, 1.0)
        self.assertEqual(context.decimals, 0.0)
        self.assertEqual(context.prefix, '')
        self.assertEqual(context.suffix, '')
        self.assertEqual(context.readonly, False)
        self.assertEqual(context.special_value, '')
        self.assertEqual(context.adaptive, False)
        self.assertEqual(context.changed, None)
        self.assertEqual(context.editing_finished, None)

    def testFull(self):
        def on_changed(value): pass
        def on_edited(): pass
        context = Number(
            value=42,
            minimum=16,
            maximum=42,
            step=4,
            decimals=8,
            prefix='pre',
            suffix='suf',
            readonly=True,
            special_value='special',
            adaptive=True,
            changed=on_changed,
            editing_finished=on_edited
        )
        self.assertEqual(context.value, 42)
        self.assertEqual(context.minimum, 16)
        self.assertEqual(context.maximum, 42)
        self.assertEqual(context.step, 4)
        self.assertEqual(context.decimals, 8)
        self.assertEqual(context.prefix, 'pre')
        self.assertEqual(context.suffix, 'suf')
        self.assertEqual(context.readonly, True)
        self.assertEqual(context.special_value, 'special')
        self.assertEqual(context.adaptive, True)
        self.assertEqual(context.changed, on_changed)
        self.assertEqual(context.editing_finished, on_edited)

    def testProperties(self):
        def on_changed(value): pass
        def on_edited(): pass
        context = Number()
        context.value = 42
        self.assertEqual(context.value, 42)
        context.minimum = 16
        self.assertEqual(context.minimum, 16)
        context.maximum = 42
        self.assertEqual(context.maximum, 42)
        context.step = 4
        self.assertEqual(context.step, 4)
        context.decimals = 8
        self.assertEqual(context.decimals, 8)
        context.prefix = 'pre'
        self.assertEqual(context.prefix, 'pre')
        context.suffix = 'suf'
        self.assertEqual(context.suffix, 'suf')
        context.readonly = True
        self.assertEqual(context.readonly, True)
        context.special_value = 'special'
        self.assertEqual(context.special_value, 'special')
        context.adaptive = True
        self.assertEqual(context.adaptive, True)
        context.changed = on_changed
        self.assertEqual(context.changed, on_changed)
        context.editing_finished = on_edited
        self.assertEqual(context.editing_finished, on_edited)

    def testMethods(self):
        context = Number()

if __name__ == '__main__':
    unittest.main()

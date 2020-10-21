import unittest

from qutie import Object
from . import QutieTestCase

class ObjectTest(QutieTestCase):

    def testEmpty(self):
        context = Object()
        self.assertEqual(context.object_name, '')
        self.assertEqual(context.destroyed, None)
        self.assertEqual(context.object_name_changed, None)

    def testFull(self):
        def on_destroyed(): pass
        def on_name_changed(): pass
        context = Object(
            object_name='object name',
            destroyed=on_destroyed,
            object_name_changed=on_name_changed
        )
        self.assertEqual(context.object_name, 'object name')
        self.assertEqual(context.destroyed, on_destroyed)
        self.assertEqual(context.object_name_changed, on_name_changed)

    def testProperties(self):
        def on_destroyed(): pass
        def on_name_changed(): pass
        context = Object()
        context.object_name = 'object name'
        self.assertEqual(context.object_name, 'object name')
        context.destroyed = on_destroyed
        self.assertEqual(context.destroyed, on_destroyed)
        context.object_name_changed = on_name_changed
        self.assertEqual(context.object_name_changed, on_name_changed)

if __name__ == '__main__':
    unittest.main()

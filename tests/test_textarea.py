import os
import unittest

from qutie import TextArea
from . import QutieTestCase

class TextAreaTest(QutieTestCase):

    def testEmpty(self):
        context = TextArea()
        self.assertEqual(context.readonly, False)
        self.assertEqual(context.richtext, False)
        self.assertEqual(context.value, '')

    def testFull(self):
        context = TextArea(
            readonly=True,
            richtext=True,
            value='lorem ipsum'
        )
        self.assertEqual(context.readonly, True)
        self.assertEqual(context.richtext, True)
        self.assertEqual(context.value, 'lorem ipsum')

    def testProperties(self):
        context = TextArea()
        context.readonly = True
        self.assertEqual(context.readonly, True)
        context.readonly = False
        self.assertEqual(context.readonly, False)
        context.richtext = True
        self.assertEqual(context.richtext, True)
        context.richtext = False
        self.assertEqual(context.richtext, False)
        context.value = 'lorem'
        self.assertEqual(context.value, 'lorem')

    def testMethods(self):
        context = TextArea()
        context.append('lorem')
        self.assertEqual(context.value, 'lorem')
        context.append('ipsum')
        self.assertEqual(context.value, os.linesep.join(('lorem', 'ipsum')))
        context.insert(' et dolor') # insert at cursor
        self.assertEqual(context.value, os.linesep.join(('lorem', 'ipsum et dolor')))
        context.clear()
        self.assertEqual(context.value, '')
        context.select_all()
        context.undo()
        context.redo()

if __name__ == '__main__':
    unittest.main()

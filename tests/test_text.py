import unittest

from qutie import Text
from . import QutieTestCase

class TextTest(QutieTestCase):

    def testEmpty(self):
        context = Text()
        self.assertEqual(context.readonly, False)
        self.assertEqual(context.clearable, False)
        self.assertEqual(context.value, '')

    def testFull(self):
        context = Text(
            readonly=True,
            clearable=True,
            value='lorem ipsum'
        )
        self.assertEqual(context.readonly, True)
        self.assertEqual(context.clearable, True)
        self.assertEqual(context.value, 'lorem ipsum')

    def testProperties(self):
        context = Text()
        context.readonly = True
        self.assertEqual(context.readonly, True)
        context.readonly = False
        self.assertEqual(context.readonly, False)
        context.clearable = True
        self.assertEqual(context.clearable, True)
        context.clearable = False
        self.assertEqual(context.clearable, False)
        context.value = 'lorem'
        self.assertEqual(context.value, 'lorem')

    def testMethods(self):
        context = Text()
        context.append('lorem')
        self.assertEqual(context.value, 'lorem')
        context.clear()
        self.assertEqual(context.value, '')

if __name__ == '__main__':
    unittest.main()

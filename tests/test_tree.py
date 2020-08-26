import unittest

from qutie import Tree
from . import QutieTestCase

class TreeTest(QutieTestCase):

    def testEmpty(self):
        context = Tree()
        self.assertEqual(context.expands_on_double_click, True)
        self.assertEqual(context.header, tuple())
        self.assertEqual(context.sortable, False)
        # self.assertEqual(context.indentation, 20)
        self.assertEqual(context.root_is_decorated, True)
        self.assertEqual(context.word_wrap, False)

    def testFull(self):
        context = Tree(
            expands_on_double_click=False,
            header=["foo", "bar"],
            sortable=True,
            indentation=42,
            root_is_decorated=False,
            word_wrap=True
        )
        self.assertEqual(context.expands_on_double_click, False)
        self.assertEqual(context.header, ("foo", "bar"))
        self.assertEqual(context.sortable, True)
        self.assertEqual(context.indentation, 42)
        self.assertEqual(context.root_is_decorated, False)
        self.assertEqual(context.word_wrap, True)

    def testProperties(self):
        context = Tree()
        context.header = "foo", "bar"
        context.expands_on_double_click = False
        context.sortable = True
        context.indentation = 4
        context.root_is_decorated = False
        context.word_wrap = True
        self.assertEqual(context.header, ("foo", "bar"))
        self.assertEqual(context.expands_on_double_click, False)
        self.assertEqual(context.sortable, True)
        self.assertEqual(context.indentation, 4)
        self.assertEqual(context.root_is_decorated, False)
        self.assertEqual(context.word_wrap, True)

    def testMethods(self):
        context = Tree()

if __name__ == '__main__':
    unittest.main()

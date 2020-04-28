import unittest

from qutie import Application
from qutie import Label

class LabelTest(unittest.TestCase):

    def setUp(self):
        self.app = Application.instance() or Application(name='unittest')

    def testEmpty(self):
        button = Label()
        self.assertEqual(button.text, '')

    def testFull(self):
        button = Label(text='text')
        self.assertEqual(button.text, 'text')

if __name__ == '__main__':
    unittest.main()

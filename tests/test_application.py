import unittest

from qutie import Application

class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.app = Application.instance() or Application(name='unittest')

    def testEmpty(self):
        self.assertEqual(self.app.name, 'unittest')
        self.assertEqual(self.app.version, '')
        self.assertEqual(self.app.organization, '')
        self.assertEqual(self.app.domain, '')

if __name__ == '__main__':
    unittest.main()

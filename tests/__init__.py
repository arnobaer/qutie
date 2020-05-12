import unittest

from qutie import Application

class QutieTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Application.instance() or Application(name='unittest')

    def tearDown(self):
        pass

import unittest

from qutie import Application
from . import QutieTestCase

class ApplicationTest(QutieTestCase):

    def testAttr(self):
        context = Application.instance()
        self.assertEqual(context.name, 'unittest')
        self.app.version = '1.2.3'
        self.assertEqual(context.version, '1.2.3')
        self.app.organization = 'HEPHY'
        self.assertEqual(context.organization, 'HEPHY')
        self.app.domain = 'hephy.at'
        self.assertEqual(context.domain, 'hephy.at')

if __name__ == '__main__':
    unittest.main()

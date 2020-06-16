import unittest
import os

from qutie import Settings
from . import QutieTestCase

class SettingsTest(QutieTestCase):

    def testFilename(self):
        context = Settings(persistent=False)
        filename = os.path.basename(context.filename)
        self.assertEqual(filename, 'unittest.qutie')

if __name__ == '__main__':
    unittest.main()

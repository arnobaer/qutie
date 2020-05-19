import unittest

from qutie import Settings
from . import QutieTestCase

class SettingsTest(QutieTestCase):

    def testEmpty(self):
        context = Settings(persistent=False)


if __name__ == '__main__':
    unittest.main()

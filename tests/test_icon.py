import unittest

from qutie import Icon
from . import QutieTestCase

class IconTest(QutieTestCase):

    def testEmpty(self):
        context = Icon()

    def testColor1(self):
        context = Icon('red')

    def testColor2(self):
        context = Icon('#00ffaa')

if __name__ == '__main__':
    unittest.main()

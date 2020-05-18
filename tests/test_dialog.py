import unittest

from qutie import Dialog
from qutie import DialogButtonBox
from qutie import filename_open
from qutie import filenames_open
from qutie import directory_open
from qutie import filename_save
from qutie import get_number
from qutie import get_text
from qutie import get_item

from . import QutieTestCase

class DialogTest(QutieTestCase):

    def testEmpty(self):
        context = Dialog()

    def testFull(self):
        context = Dialog()

    def testProperties(self):
        context = Dialog()

    def testMethods(self):
        context = Dialog()

class DialogButtonBoxTest(QutieTestCase):

    def testEmpty(self):
        context = DialogButtonBox()

    def testFull(self):
        context = DialogButtonBox()

    def testProperties(self):
        context = DialogButtonBox()

    def testMethods(self):
        context = DialogButtonBox()

if __name__ == '__main__':
    unittest.main()

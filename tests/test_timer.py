import threading
import time
import unittest

from qutie import Timer, single_shot
from . import QutieTestCase

class TimerTest(QutieTestCase):

    def testEmpty(self):
        context = Timer()
        self.assertEqual(context.interval, 0.0)
        self.assertEqual(context.single_shot, False)
        self.assertEqual(context.timer_type, 'coarse')
        self.assertEqual(context.timeout, None)

    def testFull(self):
        def timeout_event():
            pass
        context = Timer(
            interval=1.23,
            single_shot=True,
            timer_type='precise',
            timeout=timeout_event
        )
        self.assertEqual(context.interval, 1.23)
        self.assertEqual(context.single_shot, True)
        self.assertEqual(context.timer_type, 'precise')
        self.assertEqual(context.timeout, timeout_event)

    def testStart(self):
        timeout_event = threading.Event()
        context = Timer(interval=0.025, timeout=timeout_event.set)
        self.assertFalse(timeout_event.is_set())
        context.start()
        time.sleep(0.030)
        self.app.qt.processEvents()
        self.assertTrue(timeout_event.is_set())

    def testSingleShot(self):
        timeout_event = threading.Event()
        self.assertFalse(timeout_event.is_set())
        single_shot(0.025, timeout_event.set)
        time.sleep(0.030)
        self.app.qt.processEvents()
        self.assertTrue(timeout_event.is_set())

if __name__ == '__main__':
    unittest.main()

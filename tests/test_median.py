import unittest

from insight_challenge.median import RunningMedian


class TestRunningMedian(unittest.TestCase):

    def test_no_elements(self):
        rm = RunningMedian()
        self.assertRaises(IndexError, rm.get_median)

    def test_single_element(self):
        rm = RunningMedian()
        rm.add(0)
        self.assertEqual(rm.get_median(), 0)

    def test_two_different_elements(self):
        rm = RunningMedian()
        rm.add(1)
        rm.add(2)
        self.assertEqual(rm.get_median(), 1.5)

    def test_two_equal_elements(self):
        rm = RunningMedian()
        rm.add(1)
        rm.add(1)
        self.assertEqual(rm.get_median(), 1)

    def test_task_example(self):
        rm = RunningMedian()
        rm.add(5)
        self.assertEqual(rm.get_median(), 5.0)
        rm.add(4)
        self.assertEqual(rm.get_median(), 4.5)
        rm.add(4)
        self.assertEqual(rm.get_median(), 4)
        rm.add(5)
        self.assertEqual(rm.get_median(), 4.5)

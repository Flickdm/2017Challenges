import unittest

from ranges import get_ranges

class TestRanges(unittest.TestCase):
    def test_case0(self):
        self.assertEqual(get_ranges([1,2,3,4,8,9,10,12,13,14]), ["1->4", "8->10", "12->14"])

    def test_case1(self):
        self.assertEqual(get_ranges([1,2,3,4,9,10,15]), ["1->4","9->10"])

    def test_case2(self):
        self.assertEqual(get_ranges([1, 2]), ["1->2"])

    def test_case3(self):
        self.assertEqual(get_ranges([1,2,3,4,5,8,9,10]), ["1->5", "8->10"])

    def test_case4(self):
        self.assertEqual(get_ranges([5,6,7,10,15,18,20,21,22]), ['5->7', '20->22'])

    def test_case5(self):
        self.assertEqual(get_ranges([5,6,9,10,12,13,15,16,18,19,25,30]), ['5->6', '9->10', '12->13', '15->16', '18->19'])

    def test_case6(self):
        self.assertEqual(get_ranges([1]), [])

    def test_case7(self):
        self.assertEqual(get_ranges([1]), [])

if __name__ == '__main__':
    unittest.main()

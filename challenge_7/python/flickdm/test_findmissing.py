import unittest

from findmissing import find_missing

class TestFindMissing(unittest.TestCase):
    def test_pattern(self):
        pattern_0 = [0, 1, 2, 4]
        pattern_1 = [1, 2, 3, 4]

        self.assertEqual(find_missing(pattern_0), 3)
        self.assertEqual(find_missing(pattern_1), 0)

if __name__ == '__main__':
    unittest.main()

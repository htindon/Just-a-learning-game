import unittest

from just_a_deck import checkForDuplicates

class TestCheckForDuplicates(unittest.TestCase):
    def test_checkForDuplicates(self):
        '''
        Test that this function can detect duplicates in lists of ints or strs.
        '''
        self.assertFalse(checkForDuplicates([2, 1, 2]))
        self.assertFalse(checkForDuplicates(["miaou", "miaou"]))
        self.assertFalse(checkForDuplicates(['A', 'A']))
        self.assertTrue(checkForDuplicates(["mi", "ia", "ou"]))
        self.assertTrue(checkForDuplicates(['A', 'B']))
        self.assertTrue(checkForDuplicates([1, 2, 3]))

if __name__ == "__main__":
    unittest.main()

import unittest

from just_a_deck import checkForDuplicates, checkForLength

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

class TestCheckForLength(unittest.TestCase):
    def test_checkForLength(self):
        '''
        Test that this function can invalidate list that have a length not equal to 30.
        '''
        data = list(range(30))
        res = checkForLength(data)
        self.assertTrue(res)
        
        data = list(range(29))
        res = checkForLength(data)
        self.assertFalse(res)
        
        data = list(range(31))
        res = checkForLength(data)
        self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()

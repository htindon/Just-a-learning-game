import unittest
import random
import string

from just_a_deck import checkForDuplicates, checkForLength, validateList

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

class TestValidateList(unittest.TestCase):
    def test_validateList(self):
        '''
        Test that this function can invalidate list that have either:
        - a length not equal to 30
        - at least one duplicate item
        '''
        data = list(range(30))
        res = validateList(data)
        self.assertTrue(res)
        
        data = string.ascii_letters
        res = validateList(data)
        self.assertFalse(res)
        
        data = list(string.ascii_letters)
        del data[30:]
        res = validateList(data)
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()

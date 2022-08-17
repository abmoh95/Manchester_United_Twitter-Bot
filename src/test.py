# https://realpython.com/python-testing/
# https://docs.python.org/3/library/unittest.html

import unittest

import football_UTD_logic
import football_UTD_twitter

class Test_UTD_Bot(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    # Testing methods from football_UTD_logic

    # def test_check_Games_Today(self):
    #     self.assertEqual(football_UTD_logic.check_Games_Today(), False)
    
    def test_teamLineUp(self):
        self.assertEqual(football_UTD_logic.teamLineUp(234234234), [])
    
    # def test_splitLineup(self):
    #     self.assertEqual(football_UTD_logic.split_lineup(234234234), False)

    


if __name__ == '__main__':
    unittest.main()
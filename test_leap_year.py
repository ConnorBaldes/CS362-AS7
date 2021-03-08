import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    
    def test_leap_year(self):
    
        year1 = 4
        self.assertEqual(leap_year.leap_year(year1), str(year1) + " is a leap year. ")



if __name__ == '__main__':

    unittest.main(verbosity=2)
import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    
    def test_leap_year(self):
    
       
        self.assertEqual(leap_year.leap_year(),0)



if __name__ == '__main__':

    unittest.main(verbosity=2)
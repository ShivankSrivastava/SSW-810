"""
Name: Shivank Srivastava
CWID: 20006832
Date: 11th Oct 2021
"""

import unittest 
from HW05_Shivank_Srivastava import Strings


class StringTest(unittest.TestCase):
    
    
    def test_reverse(self) -> None:
        
        test: Strings = Strings("Shivank")
        self.assertEqual(test.s, "Shivank") 
        self.assertEqual(test.reverse(test.s), "knavihS")
        
        test1: Strings = Strings("abcdcba")
        self.assertEqual(test1.reverse(test1.s), "abcdcba")
        
        test2: Strings = Strings("x")
        self.assertEqual(test2.reverse(test2.s), "x")
        
        test3: Strings = Strings("abc")
        self.assertNotEqual(test3.reverse(test3.s), "abc")
        
        test4: Strings = Strings(" ")
        self.assertEqual(test4.reverse(test4.s), " ")

        with self.assertRaises(ValueError, msg="Input should be string"):
            test5: Strings = Strings(55)

    def test_substring(self) -> None:
        
        test: Strings = Strings("Shivank")
        self.assertEqual(test.substring("Shi", test.s), 0)
        self.assertEqual(test.substring("an", test.s), 4)
        self.assertEqual(test.substring("nk", test.s), 5)
        self.assertEqual(test.substring("i", ""), -1)


    def test_find_second(self) -> None:
        
        test: Strings = Strings("abcdcba")
        self.assertEqual(test.find_second("a", test.s), 6)
        test1: Strings = Strings("Mississippi")
        self.assertEqual(test1.find_second("iss", test1.s), 4)
        self.assertEqual(test1.find_second("xyz", test1.s), -1)

    """def test_get_lines(self) -> None:
        
        List = []
        test: Strings = Strings("")
        file_name: str = 'C:/Users/Shivank Srivastava/Desktop/SSW810/HW05/test.txt'
        expect: List[str] = ['<line0>', '<line1>', '<line2>','<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        result: List[str] = list(test.get_lines(file_name))
        self.assertEqual(result, expect)

       
        file_name_2: str = 'C:/Users/Shivank Srivastava/Desktop/SSW810/HW05/test.txt'
        expect1: List[str] = []
        result1: List[str] = list(test.get_lines(file_name_2))
        self.assertEqual(result1, expect1)
"""

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

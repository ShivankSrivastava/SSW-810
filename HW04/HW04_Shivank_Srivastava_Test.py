"""
Name: Shivank Srivastava    
CWID: 20006832
Date: 03 Oct 2021
"""
import unittest
from HW04_Shivank_Srivastava import count_vowels, last_occurrence, my_enumerate


class CountVowelTest(unittest.TestCase):
    def test1_count_vowels(self) -> None:
        
        self.assertEqual(count_vowels("Sneakers"), 3)
        self.assertEqual(count_vowels("Doritos"), 3)
        self.assertEqual(count_vowels("Gym"), 0)
        self.assertNotEqual(count_vowels("Hello"), 5)


class FindLastTest(unittest.TestCase):
    def test2_last_occurrence(self) -> None:
       
        self.assertEqual(last_occurrence("k", "Sneakers"), 4)
        self.assertEqual(last_occurrence("1", "Doritos"), None)
        self.assertEqual(last_occurrence(
            "Rabbit", ["Dog", "Cat", "Rat", "Rabbit", "Rabbit"]), 4)
        self.assertEqual(last_occurrence(
            "s", "Gym"), None)
        self.assertEqual(last_occurrence("n", "Banana"), 4)
        self.assertNotEqual(last_occurrence("l", "World"), 5)
        self.assertEqual(last_occurrence(
            "Hello", "l"), None)


class EnumerateTest(unittest.TestCase):
    def test3_enumerate(self) -> None:
        
        str1: str = list(my_enumerate("Shivank"))
        str2: str = list(enumerate("Shivank"))
        self.assertEqual(str1, str2)
        str3: str = list(my_enumerate("Shivank"))
        str4: str = list(enumerate("Shivank Srivastava"))
        self.assertNotEqual(str3, str4)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

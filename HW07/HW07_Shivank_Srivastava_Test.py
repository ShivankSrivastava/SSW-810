"""
Name: Shivank Srivastava
CWID: 20006832
Date: 25 Oct 2021
"""
from typing import List, Tuple
import unittest
from HW07_Shivank_Srivastava import Containers


class ContainersTest(unittest.TestCase):
    def test_anagrams_list(self) -> None:
       
        test: Containers = Containers()
        self.assertEquals(test.anagrams_lst("Dirtyroom", "Dormitory"), True)
        self.assertEquals(test.anagrams_lst("Cinema", "Iceman"), True)
        self.assertEquals(test.anagrams_lst("Study", "Dusty"), True)
        self.assertEquals(test.anagrams_lst("Shivank", "Srivastava"), False)
        self.assertEquals(test.anagrams_lst("", ""), True)
        self.assertEquals(test.anagrams_lst("123", "321"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of string type"):
            test.anagrams_lst(9, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of string type"):
            test.anagrams_lst("Dormitory", 9)

    def test_anagrams_defaultdict(self) -> None:
       
        test: Containers = Containers()
        self.assertEquals(test.anagrams_dd("Dirtyroom", "Dormitory"), True)
        self.assertEquals(test.anagrams_dd("Cinema", "Iceman"), True)
        self.assertEquals(test.anagrams_dd("Study", "Dusty"), True)
        self.assertEquals(test.anagrams_dd("Shivank", "Srivastava"), False)
        self.assertEquals(test.anagrams_dd("", ""), True)
        self.assertEquals(test.anagrams_dd("123", "321"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of string type"):
            test.anagrams_dd(9, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of string type"):
            test.anagrams_dd("Dormitory", 9)

    def test_anagrams_cntr(self) -> None:
        
        test: Containers = Containers()
        self.assertEquals(test.anagrams_cntr("Dirtyroom", "Dormitory"), True)
        self.assertEquals(test.anagrams_cntr("Cinema", "Iceman"), True)
        self.assertEquals(test.anagrams_cntr("Study", "Dusty"), True)
        self.assertEquals(test.anagrams_cntr("Shivank", "Srivastava"), False)
        self.assertEquals(test.anagrams_cntr("", ""), True)
        self.assertEquals(test.anagrams_cntr("123", "321"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of string type"):
            test.anagrams_cntr(9, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of string type"):
            test.anagrams_cntr("Dormitory", 9)

    def test_covers_alphabet(self) -> None:
        
        test: Containers = Containers()
        self.assertEquals(test.covers_alphabet(
            "qwertyuiopasdfghjklzxcvbnm"), True)
        self.assertEquals(test.covers_alphabet(
            "We promptly judged antique ivory buckles for the next prize"), True)
        self.assertEquals(test.covers_alphabet("xyz"), False)
        with self.assertRaises(ValueError, msg="Input sentence must be of string type"):
            test.covers_alphabet(9)

    def test_web_analyzer(self) -> None:
        
        test: Containers = Containers()
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(test.web_analyzer(weblogs), summary)
        with self.assertRaises(ValueError, msg="Input weblogs must be of List type"):
            test.web_analyzer(9)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

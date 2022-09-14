"""
Name: Shivank Srivastava
CWID: 20006832
Date: 17 Oct 2021
"""
import unittest
from HW06_Shivank_Srivastava import HomeWork06, DonutQueue


class HomeWork06Test(unittest.TestCase):
    def test_list_copy(self) -> None:
        
        test: HomeWork06 = HomeWork06()
        self.assertEqual(test.list_copy(list([4, 5, 6])), list([4, 5, 6]))
        self.assertNotEqual(test.list_copy(list([4, 5, 6])), list([1, 2, 3]))
        self.assertEqual(test.list_copy([]), [])
        self.assertEqual(test.list_copy(
            [1, "Shivank", "hello"]), [1, "Shivank", "hello"])
        with self.assertRaises(ValueError, msg="Input l must be of type List"):
            test.list_copy(9)

    def test_list_intersect(self) -> None:
        
        test: HomeWork06 = HomeWork06()
        self.assertEqual(test.list_intersect(
            list([1, 2, 3]), list([1, 4, 5])), [1])
        self.assertEqual(test.list_intersect(
            list([1, 2, 3]), list([7, 8, 9])), [])
        self.assertEqual(test.list_intersect(
            [1, 2, "Shivank"], ["Shivank", 6, 7]), ["Shivank"])
        with self.assertRaises(ValueError, msg="Input l1 must be of type List"):
            test.list_intersect(9, list([1, 2, 3]))
        with self.assertRaises(ValueError, msg="Input l2 must be of type List"):
            test.list_intersect(list([1, 2, 3]), 9)

    def test_list_difference(self) -> None:
        
        test: HomeWork06 = HomeWork06()
        self.assertEqual(test.list_difference([1, 2, 5], [1, 2, 4]), [5])
        self.assertEqual(test.list_difference([7, 8, 9], [4, 5, 6]), [7, 8, 9])
        self.assertEqual(test.list_difference([10, 12, 13], [10, 12, 13]), [])
        with self.assertRaises(ValueError, msg="Input l1 must be of type List"):
            test.list_intersect(9, list([1, 2, 3]))
        with self.assertRaises(ValueError, msg="Input l2 must be of type List"):
            test.list_intersect(list([1, 2, 3]), 9)

    def test_remove_vowels(self) -> None:
        
        test: HomeWork06 = HomeWork06()
        self.assertEqual(test.remove_vowels(
            "Amy is my favorite daughter"), "my favorite daughter")
        self.assertEqual(test.remove_vowels(
            "Jan is my best friend"), "Jan my best friend")
        self.assertEqual(test.remove_vowels(""), "")
        with self.assertRaises(ValueError, msg="Input string must be of type str"):
            test.remove_vowels(9)

    def test_check_pwd(self) -> None:
        
        test: HomeWork06 = HomeWork06()
        self.assertEqual(test.check_pwd("9SHivank"), True)
        self.assertEqual(test.check_pwd("9Shivank"), False)
        self.assertEqual(test.check_pwd("Shivank"), False)
        self.assertEqual(test.check_pwd("007SHiv"), True)
        self.assertEqual(test.check_pwd("007"), False)
        self.assertEqual(test.check_pwd(""), False)
        self.assertEqual(test.check_pwd("9SHIVANK"), False)
        with self.assertRaises(ValueError, msg="Input password must be of type str"):
            test.check_pwd(9)

    def test_DonoutQueue(self) -> None:
        
        dq: DonutQueue = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

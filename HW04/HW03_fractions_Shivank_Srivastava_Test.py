"""
Author: Shivank Srivastava
CWID: 20006832
Date: 28th Sept 2021
"""

import unittest
from HW03_fractions_Shivank_Srivastava import Fraction


class TestFraction(unittest.TestCase):
    """
    In this we will test all the possible cases.
    """

    def test_init(self) -> None:
    
        f: "Fraction" = Fraction(1, 4)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 4)

    def test_init_exception(self) -> None:
        
        with self.assertRaises(ValueError, msg="The fraction cannot be zero"):

            f10: "Fraction" = Fraction(1, 0)

    def test_add(self) -> None:
        
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(f12 + f13, Fraction(5, 6))
        self.assertNotEqual(f12 + f13, Fraction(77, 102))

    def test_multiple_operands(self) -> None:
        
        f12: "Fraction" = Fraction(1, 2)
        f32: "Fraction" = Fraction(3, 2)
        f68: "Fraction" = Fraction(6, 8)
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(f12 + f12 + f12, Fraction(12, 8))
        self.assertEqual(f13 + f13 + f13, Fraction(3, 3))
        self.assertEqual(f12 + f32 * f68, Fraction(52, 32))

    def test_sub(self) -> None:
       
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(f12 - f13, Fraction(1, 6))
        self.assertNotEqual(f12 - f34 - f13, Fraction(34, 54))

    def test_mul(self) -> None:
       
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f34: "Fraction" = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))
        self.assertEqual(f12 * f13, Fraction(1, 6))
        self.assertEqual(f12 * f34 * f13, Fraction(3, 24))

    def test_truediv(self) -> None:
       
        f12: "Fraction" = Fraction(1, 2)
        f68: "Fraction" = Fraction(6, 8)
        self.assertEqual(f12 / f68, Fraction(8, 12))
        self.assertNotEqual(f12 / f68, Fraction(-1, 2))

    def test_equal(self) -> None:
        """
        Equal function
        """
        f12: "Fraction" = Fraction(1, 2)
        f24: "Fraction" = Fraction(2, 4)
        f34: "Fraction" = Fraction(3, 4)
        f68: "Fraction" = Fraction(6, 8)
        self.assertTrue(f12 == f24)
        self.assertFalse(f12 == f34)
        self.assertFalse(f12 == f68)

    def test_notequal(self) -> None:
        
        f12: "Fraction" = Fraction(1, 2)
        f24: "Fraction" = Fraction(2, 4)
        f48: "Fraction" = Fraction(4, 8)
        f34: "Fraction" = Fraction(3, 4)
        self.assertFalse(f12 != f24)
        self.assertFalse(f12 != f48)
        self.assertTrue(f12 != f34)

    def test_lessthan(self) -> None:
        
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f14: "Fraction" = Fraction(1, 4)
        f34: "Fraction" = Fraction(3, 4)
        self.assertLess(f12, f34)
        self.assertEqual(f12.__lt__(f13), False)
        self.assertEqual(f12.__lt__(f14), False)

    def test_lessthanequal(self) -> None:
        
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        f13: "Fraction" = Fraction(1, 3)
        f14: "Fraction" = Fraction(1, 4)
        self.assertLessEqual(f12, f34)
        self.assertLessEqual(f12, f12)
        self.assertEqual(f34.__le__(f12), False)
        self.assertEqual(f12.__le__(f13), False)
        self.assertEqual(f12.__le__(f14), False)

    def test_greaterthan(self) -> None:
        
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f34: "Fraction" = Fraction(3, 4)
        f24: "Fraction" = Fraction(2, 4)
        self.assertGreater(f12, f13)
        self.assertGreater(f34, f12)
        self.assertEqual(f12.__gt__(f12), False)
        self.assertEqual(f12.__gt__(f24), False)

    def test_greaterthanequal(self) -> None:
        
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f24: "Fraction" = Fraction(2, 4)
        f34: "Fraction" = Fraction(3, 4)
        self.assertGreaterEqual(f12, f24)
        self.assertGreaterEqual(f34, f12)
        self.assertGreaterEqual(f34, f13)
        self.assertEqual(f12.__ge__(f34), False)

    def test_str(self) -> None:
        
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(str(f13), "1/3")
    
    def test_simplify(self) -> None:
        
        str1 = Fraction(1, 3).__simplify__().__str__()
        str2 = Fraction(4, 12).__simplify__().__str__()
        str3 = Fraction(6, 2).__simplify__().__str__()
        str4 = Fraction(18, 6).__simplify__().__str__()
        str5 = Fraction(2, 1).__simplify__().__str__()
        self.assertEqual(str1, str2)
        self.assertEqual(str3, str4)
        self.assertNotEqual(str2, str3)
        self.assertNotEqual(str1, str5)



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

"""
Name: Shivank Srivastava
CWID: 20006832
Date: 09/20/2021
"""


class Fraction:
    """
    We will use Add, Subtract, Multiply, Divide and Compare two fraction
    """

    def __init__(self, numerator: float,  denominator: float) -> None:
        
        self.numerator: float = numerator
        if denominator == 0:
            raise ValueError("The denominatoe cannot be Zero" )
        self.denominator: float = denominator
    
    def add(self, other: "Fraction") -> "Fraction":
        opt_num: float = (self.numerator * other.denominator) + \
            (self.denominator * other.numerator)
        opt_den: float = self.denominator * other.denominator
        return Fraction(opt_num, opt_den)
    
    def subtract(self, other: "Fraction") -> "Fraction":
        
        opt_num: float = (self.numerator * other.denominator) - \
            (self.denominator * other.numerator)
        opt_den: float = self.denominator * other.denominator
        return Fraction(opt_num, opt_den)

    def multiply(self, other: "Fraction") -> "Fraction":
        
        opt_num: float = self.numerator * other.numerator
        opt_den: float = self.denominator * other.denominator
        return Fraction(opt_num, opt_den)

    def divide(self, other: "Fraction") -> "Fraction":
        
        opt_num: float = self.numerator * other.denominator
        opt_den: float = self.denominator * other.numerator
        return Fraction(opt_num, opt_den)

    def compare(self, other: "Fraction") -> bool:
        
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __str__(self) -> str:
        
        return str(self.numerator) + "/" + str(self.denominator)

def inp_number(prompt: str) -> float:
    loop: bool = True
    while loop:
        try:
            inp: str = input(prompt)
            return float(inp)
        except ValueError as e:
            print("Enter number only")
            continue


def inp_fraction() -> "Fraction":

    Numerator: float = float(inp_number("Enter the Numerator:"))
    while True:
        Denominator: float = float(inp_number("Enter the Denominator:"))
        try:
            Fraction(Numerator, Denominator)
        except ValueError:
            print("The denominator cannot be ZERO")
        except BaseException:
            print(f"Something went wrong: {BaseException}")
        else:
            return Fraction(Numerator, Denominator)


def compute(f1: "Fraction", operator: str, other: "Fraction") -> None:
    
    if operator == "+":
        print(f'{f1.numerator} / {f1.denominator} + {other.numerator} / {other.denominator} = {str(f1.add(other))}')
    elif operator == "-":
        print(f'{f1.numerator} / {f1.denominator} - {other.numerator} / {other.denominator} = {str(f1.subtract(other))}')
    elif operator == "*":
        print(f'{f1.numerator} / {f1.denominator} * {other.numerator} / {other.denominator} = {str(f1.multiply(other))}')
    elif operator == "/":
        print(f'{f1.numerator} / {f1.denominator} / {other.numerator} / {other.denominator} = {str(f1.divide(other))}')
    elif operator == "==":
        print(f'{f1.numerator} / {f1.denominator} == {other.numerator} / {other.denominator} = {str(f1.compare(other))}')


def check_operator(operator: str) -> bool:
    
    opp = ["+", "-", "*", "/", "=="]
    if(operator not in opp):
        return True
    else:
        return False


def main() -> None:
    
    print("Fraction calculator!")
    print("Fraction 1")
    f1: Fraction = inp_fraction()
    opp = input("Operation (+, -, *, /, ==):")
    loop: bool = check_operator(opp)
    while loop:
        if loop:
            print("Invalid input for operator, Try again!")
            opp = input("Operation (+, -, *, /, ==):")
            loop: bool = check_operator(opp)
        else:
            pass
    print("Fraction 2")
    other: Fraction = inp_fraction()
    compute(f1, opp, other)


def test_case() -> None:

    print("TEST CASES")
    f12: Fraction = Fraction(1, 2)
    f44: Fraction = Fraction(4, 4)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)

    print(f"{f12} + {f12} = {f12.add(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.subtract(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.add(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.compare(f32)} [True]")

    """
    Test cases that were asked in the assignment
    """

if __name__ == '__main__':
    main()
    test_case()


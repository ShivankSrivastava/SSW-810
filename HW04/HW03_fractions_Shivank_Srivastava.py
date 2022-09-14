"""
Name: Shivank Srivastava
CWID: 20006832
Date: 29th Sept 2021
"""


class Fraction:
    """
    We will use Add, Subtract, Multiply, Divide and __eq__ two fraction
    """

    def __init__(self, numerator: float,  denominator: float) -> None:
        
        self.numerator: float = numerator
        if denominator == 0:
            raise ValueError("The denominatoe cannot be Zero" )
        self.denominator: float = denominator
    
    def __add__(self, other: "Fraction") -> "Fraction":
        opt_num: float = (self.numerator * other.denominator) + \
            (self.denominator * other.numerator)
        opt_den: float = self.denominator * other.denominator
        return Fraction(opt_num, opt_den)
    
    def __sub__(self, other: "Fraction") -> "Fraction":
        
        opt_num: float = (self.numerator * other.denominator) - \
            (self.denominator * other.numerator)
        opt_den: float = self.denominator * other.denominator
        return Fraction(opt_num, opt_den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        
        opt_num: float = self.numerator * other.numerator
        opt_den: float = self.denominator * other.denominator
        return Fraction(opt_num, opt_den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        
        opt_num: float = self.numerator * other.denominator
        opt_den: float = self.denominator * other.numerator
        return Fraction(opt_num, opt_den)

    def __eq__(self, other: "Fraction") -> bool:
        
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __str__(self) -> str:
        
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __ne__(self, other: "Fraction") -> bool:
        
        return self.numerator * other.denominator != self.denominator * other.numerator
    
    def __lt__(self, other: "Fraction") -> bool:
       
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other: "Fraction") -> bool:
       
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other: "Fraction") -> bool:
        
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other: "Fraction") -> bool:
        
        return self.numerator * other.denominator >= self.denominator * other.numerator
    
    def __gcd__(self, numerator: int, denominator: int) -> int:

        while(denominator):
            numerator, denominator = denominator, numerator % denominator
        return numerator

    def __simplify__(self) -> "Fraction":
        
        if((self.numerator > 0) and (self.denominator < 0)):
            x = self.__gcd__(abs(self.numerator), abs(self.denominator))
            numerator1: float = -(self.numerator/x)
            denominator1: float = -(self.denominator/x)
            return Fraction(numerator1, denominator1)
        elif((self.numerator < 0) and (self.denominator < 0)):
            x = self.__gcd__(abs(self.numerator), abs(self.denominator))
            numerator1: float = -(self.numerator/x)
            denominator1: float = -(self.denominator/x)
            return Fraction(numerator1, denominator1)
        else:
            x = self.__gcd__(abs(self.numerator), abs(self.denominator))
            numerator1: float = self.numerator/x
            denominator1: float = self.denominator/x
            return Fraction(numerator1, denominator1)

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
        print(f'{f1.numerator} / {f1.denominator} + {other.numerator} / {other.denominator} = {str(f1.__add__(other))}')
    elif operator == "-":
        print(f'{f1.numerator} / {f1.denominator} - {other.numerator} / {other.denominator} = {str(f1.__sub__(other))}')
    elif operator == "*":
        print(f'{f1.numerator} / {f1.denominator} * {other.numerator} / {other.denominator} = {str(f1.__mul__(other))}')
    elif operator == "/":
        print(f'{f1.numerator} / {f1.denominator} / {other.numerator} / {other.denominator} = {str(f1.__truediv__(other))}')
    elif operator == "==":
        print(f'{f1.numerator} / {f1.denominator} == {other.numerator} / {other.denominator} = {str(f1.__eq__(other))}')
    elif operator == '!=':
        result = f1 != other
    elif operator == '>':
        result = f1 > other
    elif operator == '>=':
        result = f1 >= other
    elif operator == '<':
        result = f1 < other
    elif operator == '<=':
        result = f1 <= other
    


def check_operator(operator: str) -> bool:
    
    opp = ["+", "-", "*", "/", "==", "!=", "<", "<=", ">", ">="]
    if(operator not in opp):
        return True
    else:
        return False


def main() -> None:
    
    print("Fraction calculator!")
    print("Fraction 1")
    f1: Fraction = inp_fraction()
    opp = input("Operation (+, -, *, /, ==, !=, <, <=, >, >=):")
    loop: bool = check_operator(opp)
    while loop:
        if loop:
            print("Invalid input for operator, Try again!")
            opp = input("Operation (+, -, *, /, ==, !=, <, <=, >, >=):")
            loop: bool = check_operator(opp)
        else:
            pass
    print("Fraction 2")
    other: Fraction = inp_fraction()
    compute(f1, opp, other)

"""
def test_case() -> None:

    print("TEST CASES")
    f12: Fraction = Fraction(1, 2)
    f44: Fraction = Fraction(4, 4)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)

    print(f"{f12} + {f12} = {f12.__add__(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.__sub__(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.__add__(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.__eq__(f32)} [True]")
"""


if __name__ == '__main__':
    main()
    


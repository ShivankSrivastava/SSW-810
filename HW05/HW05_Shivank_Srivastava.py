"""
Name: Shivank Srivastava
CWID: 20006832
Date: 11th Oct 2021
"""


from typing import Iterator

class Strings:

    def reverse(self, s: str) -> str:

        str = ""
        for i in s:
            str = i + str
        return str 
       
    def substring(self, target: str, s: str) -> int:

        if not isinstance(target, str):
            raise ValueError("Invalid input!! Input should be string")
        if len(target) < 1:
            return 0
        if len(s) < 1:
            return -1
        for i in range(len(s)):
            if(s[i:i+len(target)] == target):
                return i
        return -1

    def find_second(self, target: str, string: str) -> int:
        
        a: int = self.substring(target, string)
        b: int = string.find(target, a+1)
        return b

    def get_lines(self, path: str) -> Iterator[str]:
        
        try:
            filePath = open(path, 'r')
        except FileNotFoundError:
            print(f"Cant open {path}")
        else:
            with filePath:
                for line in filePath:
                    line = line.rstrip('\n')
                    while line.endswith('\\'):
                        slashpointer: int = line.find('\\')
                        line = line[:slashpointer]+" "
                        line = line[:-1] + filePath.readline().strip('\n')

                    line = line.split('#', 1)[0].strip('\n')
                    if line:
                        yield line
                    else:
                        continue

    def __init__(self, s: str)-> None:
        if not isinstance(s, str): 
            raise ValueError("Invalid input!! Input should be string")
        self.s: str = s


def main() -> None:
    file_name = 'C:/Users/Shivank Srivastava/Desktop/SSW810/HW05/test1.txt'
    test: Strings = Strings("")
    for line in test.get_lines(file_name):
        print(line)

if __name__ == '__main__':
    main()
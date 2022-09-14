"""
Name: Shivank Srivastava
CWID: 20006832
Date: 17 Oct 2021
"""
from typing import Any, Optional, List


class HomeWork06:

    def __init__(self) -> None:
        return None

    def list_copy(self, l: List[Any]) -> List[Any]:
        
        if not isinstance(l, List):  
            raise ValueError("Input l must be of type List")
        return [i for i in l]

    def list_intersect(self, l1: List[Any], l2: List[Any]) -> List[Any]:
        
        if not isinstance(l1, List):  
            raise ValueError("Input l1 must be of type List")
        if not isinstance(l2, List):  
            raise ValueError("Input l2 must be of type List")
        return [i for i in l1 if i in l2]

    def list_difference(self, l1: List[Any], l2: List[Any]) -> List[Any]:
        
        if not isinstance(l1, List):  
            raise ValueError("Input l1 must be of type List")
        if not isinstance(l2, List):  
            raise ValueError("Input l2 must be of type List")
        return [i for i in l1 if i not in l2]

    def remove_vowels(self, string: str) -> str:
        
        if not isinstance(string, str):  
            raise ValueError("Input string must be of type str")
        return " ".join([words for words in string.split() if words[0] not in "aeiouAEIOU"])

    def check_pwd(self, password: str) -> bool:
        
        if not isinstance(password, str):  
            raise ValueError("Input password must be of type str")
        return len(password) >= 4 \
            and password[0].isdigit() \
            and len([c for c in password if c.isupper()]) >= 2 \
            and len([c for c in password if c.islower()]) >= 1


class DonutQueue:
    
    queue: List

    def __init__(self) -> None:
        self.queue: List = []

    def arrive(self, name: str, vip: bool) -> None:
        
        if len(self.queue) > 0:
            if vip:
                for index, person in enumerate(self.queue):
                    if not person[1]:
                        self.queue.insert(index, [name, vip])
                        break
            else:
                self.queue.append([name, vip])
        else:
            self.queue.append([name, vip])

    def next_customer(self) -> Optional[str]:
        
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)[0]

    def waiting(self) -> Optional[str]:
        
        result: str = ""
        for i in self.queue:
            result += i[0]+", "
        return result[:-2]

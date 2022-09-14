"""
Name: Shivank Srivastava
CWID: 20006832
Date: 25 Oct 2021
"""

from typing import List, DefaultDict, Tuple
from collections import Counter, defaultdict
import string


class Containers:
    
    def __init__(self) -> None:
        return None

    def anagrams_lst(self, str1: str, str2: str) -> bool:
        
        if not isinstance(str1, str): 
            raise ValueError("Input str1 must be of string type")
        if not isinstance(str2, str): 
            raise ValueError("Input str2 must be of string type")
        return sorted(list(str1.lower())) == sorted(list(str2.lower()))

    def anagrams_dd(self, str1: str, str2: str) -> bool:
        
        if not isinstance(str1, str): 
            raise ValueError("Input str1 must be of string type")
        if not isinstance(str2, str): 
            raise ValueError("Input str2 must be of string type")
        dd: defaultdict[str, int] = defaultdict(int)
        for i in str1.lower():
            dd[i] += 1
        for i in str2.lower():
            dd[i] -= 1
        return not any(dd.values())

    def anagrams_cntr(self, str1: str, str2: str) -> bool:
        
        if not isinstance(str1, str): 
            raise ValueError("Input str1 must be of string type")
        if not isinstance(str2, str): 
            raise ValueError("Input str2 must be of string type")
        return Counter(str1.lower()) == Counter(str2.lower())

    def covers_alphabet(self, sentence: str) -> bool:
        
        if not isinstance(sentence, str): 
            raise ValueError("Input must be of string type")
        return set(string.ascii_lowercase) <= set(sentence.lower())

    def web_analyzer(self, weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
        
        if not isinstance(weblogs, List): 
            raise ValueError("Input weblogs must be of type List")
        dd: DefaultDict[str, set[str]] = defaultdict(set)
        for names, webpage in weblogs:
            dd[webpage].add(names)
        return [(website, sorted(name)) for website, name in sorted(dd.items())]
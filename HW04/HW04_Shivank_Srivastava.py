"""
Name: Shivank Srivastava
CWID: 20006832
Date: 03 Oct 2021
"""
from typing import Optional, Any, Iterator, Sequence


def count_vowels(s: str) -> int:
    
    count: int = 0
    s1: str = s.lower()
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    for i in s1:
        if i in vowels:
            count += 1
    return count


def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
    
    ans: Optional[int] = None
    for offset, i in enumerate(sequence):
        if i == target:
            ans = int(offset)
    return ans


def my_enumerate(seq) -> Iterator[Any]:
    
       for offset in range(len(seq)):
        yield offset, seq[offset]

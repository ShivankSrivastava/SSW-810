"""
Name: Shivank Srivastava
CWID: 20006832
Date: 1st Nov 2021
"""

from typing import Tuple, Iterator, List, IO, Dict
from datetime import timedelta, datetime
from prettytable import PrettyTable
import os


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    
    three_days_after_02272020: datetime = datetime(
        2020, 2, 27) + timedelta(days=3)
    three_days_after_02272019: datetime = datetime(
        2019, 2, 27) + timedelta(days=3)
    days_passed_02012019_09302019: int = (
        datetime(2019, 9, 30) - datetime(2019, 2, 1)).days

    return (three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019)


def file_reader(path: str, fields: int, sep: str = ',', header: bool = False) -> Iterator[List[str]]:
    
    try:
        fp: IO = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot open file at {path} ")
    else:
        line_number: int = 0
        for line in fp:
            row: List[str] = line.strip().split(sep)
            line_number += 1
            if len(row) != fields:
                fp.close()
                raise ValueError(
                    f"File {path} at line {line_number} has  {len(row)} items, whereas the \
                    expected items where {fields} ")
            if header is False:
                yield row
            else:
                header = False


class FileAnalyzer:
   

    def __init__(self, directory: str) -> None:
        
        self.directory: str = directory  
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()  
    def analyze_files(self) -> None:
        
        path: str = self.directory
        direct: List[str] = os.listdir(path)
        for f in direct:
            if f.endswith('.py'):
                try:
                    fp = open(os.path.join(path, f), 'r')
                except FileNotFoundError:
                    raise FileNotFoundError(f"File {f} cannot be openend")
                else:
                    with fp:
                        character_count: int = 0
                        class_count: int = 0
                        function_count: int = 0
                        line_count: int = 0

                        for line in fp:
                            character_count += len(line)
                            line_count += 1

                            if line.strip().startswith('def '):
                                function_count += 1
                            if line.startswith('class '):
                                class_count += 1

                        self.files_summary[f] = {
                            'classes': class_count,
                            'functions': function_count,
                            'lines': line_count,
                            'characters': character_count
                        }

    def pretty_print(self) -> None:
        
        output: PrettyTable = PrettyTable()
        output.field_names = ['File Name', 'Classes',
                              'Functions', 'Lines', 'Characters']

        for i, j in self.files_summary.items():
            output.add_row([i, j['classes'], j['functions'],
                            j['lines'], j['characters']])

        print("\nSummary for ", self.directory)
        print(output)

"""
Name: Shivank Srivastava
CWID: 20006832
Date: 1st Nov 2021
"""

import unittest
from HW08_Shivank_Srivastava import date_arithmetic, file_reader, FileAnalyzer
from datetime import datetime
from prettytable import PrettyTable


class HW08Test(unittest.TestCase):
   

    def test_date_arithmatic(self):
       
        self.assertEqual(date_arithmetic(), (datetime(
            2021, 3, 1), datetime(2020, 3, 2), 241))
        self.assertNotEqual(date_arithmetic(), (datetime(
            2021, 3, 1), datetime(2020, 3, 2), 41))

    def test_file_reader(self) -> None:
        
        result = [['123', 'Jin He', 'Computer Science'],
                  ['234', 'Nanda Koka', 'Software Engineering'],
                  ['345', 'Benji Cai', 'Software Engineering']]
        self.assertEqual(
            list(file_reader('./student_majors.txt', 3, '|', True)), result)
        self.assertNotEqual(
            list(file_reader('./student_majors.txt', 3, '|')), result)
        with self.assertRaises(ValueError):
            list(file_reader('./student_majors.txt', 4, '|', True))
        with self.assertRaises(FileNotFoundError):
            list(file_reader('abc.txt', 3, '|', True))

    def test_analyze_files(self) -> None:
       
        test = FileAnalyzer('./HW08_Test')
        expected = {'HW08_Shivank_Srivastava.py':
                    {'classes': 1,
                     'functions': 5, 'lines': 100, 'characters': 3399}}
        self.assertNotEqual(test.files_summary, expected)
        with self.assertRaises(FileNotFoundError):
            FileAnalyzer(' ')

    def test_pretty_print(self) -> None:
        test2 = FileAnalyzer('./HW08_Test/')
        test2.pretty_print()


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

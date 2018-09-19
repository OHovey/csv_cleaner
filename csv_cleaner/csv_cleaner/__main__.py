"""A module for quickly removing empty rows from csv files

Args:
    path (optional): path where the target file(s) is located.
    if no argument is given, the current working directory will be used.

    filename (optional): the csv file to be modified and copied.
                         If no argument is given, all files with the '.csv'
                         or '.xlsx' suffix will be used.

Returns:
    ...

"""

from csv_cleaner import CsvClean
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 2:
        c = CsvClean()
    elif len(sys.argv) < 3 and '.csv' not in sys.argv[1] or 'xlsx' not in sys.argv[1]:
        c = CsvClean(sys.argv[1])
    elif len(sys.argv) < 3 and '.csv' in sys.argv[1] or '.xlsx' in sys.argv[1]:
        c = CsvClean(file = sys.argv[1])
    else:
        c = CsvClean(sys.argv[1], sys.argv[2])
    
    c.clean()

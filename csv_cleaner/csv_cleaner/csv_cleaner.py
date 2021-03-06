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

import pandas as pd 
import os

class CsvClean:
    def __init__(self, path=None, file=None):
        if path is not None:
            self.path = path
        else:
            self.path = os.getcwd()
        self.path += '/'
        if file is not None:
            self.file = file
            self.new_filename = 'new_' + self.file
        else:
            self.files = [c for c in os.listdir(path) if '.csv' in str(c) or '.xlsx' in str(c)]
            self.file = False


    def file_writer(self, file):
        try:
            full_path = "{}{}".format(self.path, file)
        except NotADirectoryError:
            raise NotADirectoryError('could not locate file: {} at {}\n Full path at: {}'.format(self.file, self.path, full_path))
            
        if '.xlsx' in str(full_path):
            df = pd.read_excel(full_path)
            df = df.dropna(how='all')
            df.to_csv(file.replace('.xlsx', '.csv'), encoding='utf-8', index=False)
            return 

        df = pd.read_csv(full_path)
        df = df.dropna(how='all')
        df.to_csv(self.new_filename)
        
    
    def clean(self):

        if self.file:
            self.file_writer(self.file)
        else:
            for file in self.files:
                self.new_filename = '{}{}'.format('new_', file)
                self.file_writer(file)
            

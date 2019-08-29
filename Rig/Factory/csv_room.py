import psv
import sys
from importlib import import_module

import_module(name='unicode_checker' ,package='..Engine')
import_module(name='FSGate' ,package='..Hold')


def useless_column(api, column_name):
    "Checks if the CSV column has a set length of 0."
    if (len(set(api[column_name])) == 0):
        return 'empty'


def check_all_useless(api):
    "Checks if the CSV has useless fields."
    for each_column in api.columns:
        column_val = useless_column(api, each_column)
        if (column_val != None):
            yield (each_column, column_val)


def list_of_CSV_fields(api):
    "Returns the entire CSV file as a dict of lists."
    for useless in check_all_useless(api):
        api.delcolumn(useless)
    csv = dict()
    for column in api.columns():
        csv[column] = list()
        for case in column:
            csv[column].append(case)
    return(csv)

def parse_CSV(csv_file):
    "Parses a CSV."
    api = psv.load(csv_file, encoding='utf_8')
    if unicode_checker.check_unicode(swallow_file(csv_file), csv_file) != 'utf-8' : return
    list_of_CSV_fields(api)

if __name__ == '__main__':
    parse_CSV('testvictim_U.csv')
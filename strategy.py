__author__ = 'Michyo'

import process_data

file_name = "20131128.csv"
file_date = process_data.filenameIntoDate(file_name)
print file_date
files = process_data.findLastNDaysFilename(file_date, 20)
print files
print process_data.computeOneBollinger(files, 2)



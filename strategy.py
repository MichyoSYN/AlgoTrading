__author__ = 'Michyo'

import csv
import process_data
import os
import datetime

''' LOG OUTPUT
log_name = "out.log"
log_file = open(log_name, "a")
sys.stdout = log_file
'''

write_in_file = "RSI_band.csv"

print ""
print "* --- * --- * --- * --- * --- * --- *"
print ""
print "--- NAME: RSI LINES ---"
print datetime.datetime.now()
print "--- START ---"

'''
for f in os.listdir(process_data.folder):
    file_name_type_separate = os.path.splitext(f)
    if file_name_type_separate[1] == ".csv":
        print "file = " + f
        print process_data.computeOneBollinger(f, -20, 2)

for f in os.listdir(process_data.folder):
    file_name_type_separate = os.path.splitext(f)
    if file_name_type_separate[1] == ".csv":
        print "file = " + f
        print "RSI = " + str(process_data.computeOneRSI(f, 14))
'''

'''
# Output into .csv
with open(write_in_file, "ab+") as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    file_id = 0
    for f in os.listdir(process_data.folder):
        file_name_type_separate = os.path.splitext(f)
        if file_name_type_separate[1] == ".csv":
            print "file = " + f
            bollinger = process_data.computeOneBollinger(f, -20, 2)
            print bollinger
            csv_writer.writerow([str(file_id), f, str(bollinger[0]), str(bollinger[1]), str(bollinger[2]), str(bollinger[3])])
            RSI = process_data.computeOneRSI(f, 14)
            print RSI
            csv_writer.writerow([str(file_id), f, str(RSI)])

        file_id += 1
'''


print datetime.datetime.now()
print "--- END ---"
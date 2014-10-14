__author__ = 'Michyo'

import sys
import process_data
import os
import datetime

log_name = "out.log"
log_file = open(log_name, "a")
sys.stdout = log_file

print "* --- * --- * --- * --- * --- * --- *"
print datetime.datetime.now()
print "--- START ---"

folder = "data/"
files = ["20140130.csv", "20140204.csv", "20140205.csv", "20140206.csv", "20140207.csv", "20140210.csv",
          "20140211.csv", "20140212.csv", "20140213.csv", "20140214.csv", "20140217.csv", "20140218.csv",
           "20140219.csv", "20140220.csv", "20140221.csv", "20140224.csv", "20140225.csv", "20140226.csv",
            "20140227.csv",  "20140228.csv",]

for f in os.listdir(folder):
    file_name_type_separate = os.path.splitext(f)
    if file_name_type_separate[1] == ".csv":
        print "file = " + f
        file_date = process_data.filenameIntoDate(f)
        print " - date = " + file_date.strftime("%Y-%m-%d")
        files = process_data.findLastNDaysFilename(file_date, 20)
        print process_data.computeOneBollinger(files, 2)

print "--- END ---"
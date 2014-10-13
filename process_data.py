__author__ = 'Michyo'

import os
import time
import datetime

separate_symbol = os.sep
folder = "data"
file_name = "20131130.csv"

def filenameIntoDate(file_name):
    file_name_separate = os.path.split(file_name)
    # print file_name_separate[0], file_name_separate[1]
    file_name_type_separate = os.path.splitext(file_name_separate[1])
    if file_name_type_separate[1] == ".csv":
        # print file_name_type_separate[0]
        # file_date = time.strptime(file_name_type_separate[0], "%Y%m%d")
        file_date =  datetime.datetime.fromtimestamp(time.mktime(time.strptime(file_name_type_separate[0],"%Y%m%d")))
        # print date
        return file_date
    else:
        return datetime.datetime.now()

def getNDaysFromDate(date, n):
    if n < 0:
        n = abs(n)
        return date - datetime.timedelta(days = n)
    else:
        return date + datetime.timedelta(days = n)

def dateIntoFilename(date):
    return time.strftime("%Y%m%d", date)

def findLastNDaysFilename(date, n):
    # past_date =  getNDaysFromDate(date, n)
    file_names = []
    global folder
    for f in os.listdir(folder):
        file_date = filenameIntoDate(f)
        print file_date
        if (date - file_date).days in range(1, n):
             file_names.append(f)
    return file_names

first = filenameIntoDate("20131104.csv")
last = filenameIntoDate("20131107.csv")
print (first - last).days

date = filenameIntoDate(file_name)
print findLastNDaysFilename(date, 20)
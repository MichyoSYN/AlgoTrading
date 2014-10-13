__author__ = 'Michyo'

import os
import time
import datetime

separate_symbol = os.sep
folder = "data"

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
    return time.strftime("%Y%m%d", date) + ".csv"

def findLastNDaysFilename(date, n):
    # past_date =  getNDaysFromDate(date, n)
    file_names = []
    global folder
    for f in os.listdir(folder):
        file_date = filenameIntoDate(f)
        if (date - file_date).days in range(1, n):
             file_names.append(f)
    return file_names

''' PASSED TEST CODE
first = filenameIntoDate("20131104.csv")
last = filenameIntoDate("20131107.csv")
print (first - last).days

file_name = "20131130.csv"
date = filenameIntoDate(file_name)
print findLastNDaysFilename(date, 20)
'''

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ----

def getProductCode(file_name):
    date = filenameIntoDate(file_name)
    HSIX3_initial_date = filenameIntoDate("20131101.csv")
    if (date - HSIX3_initial_date).days in range(0, 28):
        return "HSIX3"
    HSIZ3_initial_date = filenameIntoDate("20131130.csv")
    if (date - HSIZ3_initial_date).days in range(0, 30):
        return "HSIZ3"
    HSIF4_initial_date = filenameIntoDate("20131231.csv")
    if (date - HSIF4_initial_date).days in range(0, 30):
        return "HSIF4"
    HSIG4_initial_date = filenameIntoDate("20140131.csv")
    if (date - HSIG4_initial_date).days in range(0, 28):
        return "HSIG4"
    HSIH4_initial_date = filenameIntoDate("20130228.csv")
    if (date - HSIH4_initial_date).days in range(0, 30):
        return "HSIH4"

def combineFolderWithFilename(file_name):
    global folder, separate_symbol
    return folder + separate_symbol + file_name

def getClosePriceForPeriod(files):
    # return close price from start to end period in an array
    prices = []
    for f in files:
        for line in open(combineFolderWithFilename(f)):
            data_line = line.split(",")
            product_code = getProductCode(f)
            if data_line[1] == product_code and data_line[2] != "999999":
                prices.append(float(data_line[2]))
    return prices

# Calculate simple moving average.
def calcSMA(prices):
    avg = 0.0
    if len(prices) == 0:
        return avg
    for p in prices:
        avg += p
    return avg / len(prices)

# Calculate standard deviation.
def calcSD(avg, prices):
    if len(prices) == 0:
        return 0.0
    dev = 0.0
    for data in prices:
        dev += (data - avg) ** 2
    return (dev / len(prices)) ** 0.5

def computeOneBollinger(files, bollinger_band_multiplier):
    prices = getClosePriceForPeriod(files)
    # print prices
    middle_bollinger = calcSMA(prices)
    sd = calcSD(middle_bollinger, prices)
    print "SD = " + str(sd) # test
    upper_bollinger = middle_bollinger + bollinger_band_multiplier * sd
    lower_bollinger = middle_bollinger - bollinger_band_multiplier * sd
    return [middle_bollinger, upper_bollinger, lower_bollinger]

'''
def computeBollingerBands(files, N, bollinger_band_multiplier)
    for i in range(start + N, end):
        closePrices = getClosePriceForPeriod(files)
        middleband[i] = calcSMA(closePrices)
        sd[i] = calcSD(middleband[i], closePrices)
        upperband[i] = middleband[i] + bollinger_band_multiplier * sd[i]
        lowerband[i] = middleband[i] - bollinger_band_multiplier * sd[i]
    return (middleband, upperband, lowerband)
'''

''' PASSED TEST CODE
file_group = ['data/20131231.csv', 'data/20131105.csv', 'data/20131106.csv']
print computeOneBollinger(file_group, 2)
'''

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ----


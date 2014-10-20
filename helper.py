__author__ = 'Michyo'

import os
import time
import datetime

separate_symbol = os.sep
folder = "data"

def stringIntoTime(s):
    return datetime.datetime.fromtimestamp(time.mktime(time.strptime(s,"%Y%m%d %H%M%S")))

def combineFolderWithFilename(file_name):
    global folder, separate_symbol
    return folder + separate_symbol + file_name

def filenameIntoDate(file_name):
    file_name_separate = os.path.split(file_name)
    file_name_type_separate = os.path.splitext(file_name_separate[1])
    if file_name_type_separate[1] == ".csv":
        file_date =  datetime.datetime.fromtimestamp(time.mktime(time.strptime(file_name_type_separate[0],"%Y%m%d")))
        return file_date
    else:
        return datetime.datetime.now()

def getProductCode(file_name):
    date = filenameIntoDate(file_name)
    HSIX3_initial_date = filenameIntoDate("20131101.csv")
    if (date - HSIX3_initial_date).days in range(0, 28):
        return "HSIX3"
    HSIZ3_initial_date = filenameIntoDate("20131129.csv")
    if (date - HSIZ3_initial_date).days in range(0, 32):
        return "HSIZ3"
    HSIF4_initial_date = filenameIntoDate("20131231.csv")
    if (date - HSIF4_initial_date).days in range(0, 30):
        return "HSIF4"
    HSIG4_initial_date = filenameIntoDate("20140130.csv")
    if (date - HSIG4_initial_date).days in range(0, 30):
        return "HSIG4"
    HSIH4_initial_date = filenameIntoDate("20130228.csv")
    if (date - HSIH4_initial_date).days in range(0, 31):
        return "HSIH4"

def getOneDayPrices(file_name):
    prices = []
    for line in open(combineFolderWithFilename(file_name)):
        data_line = line.split(",")
        product_code = getProductCode(file_name)
        if data_line[1] == product_code and data_line[2] != "999999":
            prices.append(float(data_line[2]))
    return  prices

def isCSV(file_name):
    file_name_type_separate = os.path.splitext(file_name)
    if file_name_type_separate[1] == ".csv":
        return True
    else:
        return False

def findFilesInFolder(start, end=100):
    count = 0
    files = []
    for f in os.listdir(folder):
        if isCSV(f):
            if count >= start and count < end:
                files.append(f)
            count += 1
            if count >= end:
                return files
    return files

def getOneDayData(file):
    time_and_prices = []
    for line in open(combineFolderWithFilename(file)):
        data_line = line.split(",")
        product_code = getProductCode(file)
        if data_line[1] == product_code and data_line[2] != "999999":
            bids = data_line[5:14:2]
            asks = data_line[16:25:2]
            couples = [stringIntoTime(file[:8] + " " + data_line[0]), float(data_line[2]), max(bids), min(asks)]
            time_and_prices.append(couples)
    return  time_and_prices

def getClosePrices(prices):
    closePrices = []
    for i in prices:
        closePrices.append(i[-1])
    return closePrices

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ----

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

def calcBollinger(prices, bollinger_band_multiplier):
    middle_bollinger = calcSMA(prices)
    sd = calcSD(middle_bollinger, prices)
    upper_bollinger = middle_bollinger + bollinger_band_multiplier * sd
    lower_bollinger = middle_bollinger - bollinger_band_multiplier * sd
    return [middle_bollinger, upper_bollinger, lower_bollinger]
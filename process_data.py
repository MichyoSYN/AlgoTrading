__author__ = 'Michyo'

import os
import time
import datetime

'''
Help functions to the whole project.
'''

separate_symbol = os.sep
folder = "data"

def filenameIntoDate(file_name):
    file_name_separate = os.path.split(file_name)
    file_name_type_separate = os.path.splitext(file_name_separate[1])
    if file_name_type_separate[1] == ".csv":
        file_date =  datetime.datetime.fromtimestamp(time.mktime(time.strptime(file_name_type_separate[0],"%Y%m%d")))
        return file_date
    else:
        return datetime.datetime.now()

def getNDaysFromDate(date, n):
    if n < 0:
        n = abs(n)
        return date - datetime.timedelta(days = n)
    else:
        return date + datetime.timedelta(days = n)

def timeIntoString(date):
    return time.strftime("%Y%m%d", date)

def findNDaysFromFilename(date, n):
    # past_date =  getNDaysFromDate(date, n)
    files = []
    global folder
    for f in os.listdir(folder):
        file_date = filenameIntoDate(f)
        if n < 0:
            if (file_date - date).days in range(n, 0):
                files.append(f)
        else:
            if (file_date - date).days in range(1, n+1):
                files.append(f)
    return files

''' PASSED TEST CODE
first = filenameIntoDate("20131104.csv")
last = filenameIntoDate("20131107.csv")
print (first - last).days

file_name = "20131130.csv"
date = filenameIntoDate(file_name)
print findNDaysFromFilename(date, 20)
'''

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ----
'''
Culculate the Bolliger band.
'''

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

def combineFolderWithFilename(file_name):
    global folder, separate_symbol
    return folder + separate_symbol + file_name

def getTodayPrices(file_name):
    prices = []
    for line in open(combineFolderWithFilename(file_name)):
        data_line = line.split(",")
        product_code = getProductCode(file_name)
        if data_line[1] == product_code and data_line[2] != "999999":
            prices.append(float(data_line[2]))
    return prices


def getOneClosePrice(p):
    return p[len(p) - 1]

def getPriceForDays(files):
    # return close price from start to end period in an array
    prices = []
    for f in files:
        single_day_price = []
        for line in open(combineFolderWithFilename(f)):
            data_line = line.split(",")
            product_code = getProductCode(f)
            if data_line[1] == product_code and data_line[2] != "999999":
                single_day_price.append(float(data_line[2]))
        prices.append(single_day_price)
    return prices

def getClosePriceForDays(prices):
    closePrices = []
    for single_day_prices in prices:
        closePrices.append(getOneClosePrice(single_day_prices))
    return closePrices

def addOneDayPrice(prices, file_name):
    del prices[0];
    single_day_price = getTodayPrices(file_name)
    prices.append(single_day_price)

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
    return [middle_bollinger, upper_bollinger, lower_bollinger, sd]

def computeOneBollinger(file_name, n,  bollinger_band_multiplier):
    files = findNDaysFromFilename(filenameIntoDate(file_name), n)
    print files
    prices = getClosePriceForDays(files)
    return calcBollinger(prices, bollinger_band_multiplier)

'''
def computeBollingerBands(files, N, bollinger_band_multiplier):
    for i in range(start + N, end):
        closePrices = getClosePriceForDays(files)
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

'''
Calculate the RSI.
'''

def calcRSI(today_avg, prices):
    gain, loss = [0.0] * 2
    for p in prices:
        if p > today_avg:
            gain += p - today_avg
            print "GAIN: " + str(p-today_avg) # test
        if p < today_avg:
            loss += today_avg - p
            print "LOSS: " + str(today_avg-p) # test
    if loss == 0:
        return 100
    RS = gain / loss
    print "gain = " + str(gain) # test
    print "loss = " + str(loss) # test
    print "RS = " + str(RS) # test
    return 100 - 100 / (1 + RS)

def computeOneRSI(today_file, n):
    avg = calcSMA(getTodayPrices(today_file))
    files = findNDaysFromFilename(filenameIntoDate(today_file), n)
    days_avg = []
    for f in files:
        days_avg.append(calcSMA(getTodayPrices(f)))
    RSI = calcRSI(avg, days_avg)
    return RSI

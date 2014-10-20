__author__ = 'Michyo'

import process_data
import datetime
import time

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ----

def stringIntoTime(s):
    return datetime.datetime.fromtimestamp(time.mktime(time.strptime(s,"%Y%m%d %H%M%S")))

def getOneDayTimeAndPrice(file):
    time_and_prices = []
    for line in open(process_data.combineFolderWithFilename(file)):
        data_line = line.split(",")
        product_code = process_data.getProductCode(file)
        if data_line[1] == product_code and data_line[2] != "999999":
            couples = [stringIntoTime(file[:8] + " " + data_line[0]), float(data_line[2])]
            time_and_prices.append(couples)
    return  time_and_prices

def calcGapInSeconds(time_initial, time_end):
    return (time_end - time_initial).seconds

def getClosePriceForPeriod(data, time_end, seconds):
    prices = []
    for single_couple in data:
        gap_in_seconds = calcGapInSeconds(single_couple[0], time_end)
        # print gap_in_seconds
        if gap_in_seconds == 0:
            return prices
        if gap_in_seconds in range(1, seconds+1):
            prices.append(single_couple[1])
    return prices

def computeOneBollinger_inOneDay(file, seconds,  bollinger_band_multiplier):
    data = getOneDayTimeAndPrice(file)
    # print len(data)
    time_and_bollinger = []
    for single_couple in data:
        time_now = single_couple[0]
        print time_now
        close_prices = getClosePriceForPeriod(data, time_now, seconds)
        # print close_prices
        bollingers = process_data.calcBollinger(close_prices, bollinger_band_multiplier)
        print bollingers
        time_and_bollinger.append([time_now, bollingers])
    return time_and_bollinger

print computeOneBollinger_inOneDay("20131104.csv", 10, 2)
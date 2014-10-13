__author__ = 'Michyo'

import csv
import os

separate_symbol = os.sep
data_folder = "processed"
data_file = "processed_data.csv"
file_name = data_folder + separate_symbol + data_file


def getClosePriceForPeriod():
    # return close price from start to end period in an array
    global file_name
    prices = []
    for line in open(file_name):
        data_line = line.split(",")
        if len(data_line) > 3:
            prices.append(data_line[2])
    return prices


# Calculate simple moving average.
def calcSMA(closePrices):
    avg = 0.0
    if len(closePrices) == 0:
        return avg
    for p in closePrices:
        avg += p
    return avg / len(closePrices)

# Calculate standard deviation.
def calcSD(avg, closePrices):
    if len(closePrices) == 0:
        return 0.0
    dev = 0.0
    for data in closePrices:
        dev += (data - avg) ** 2
    return (dev / len(closePrices)) ** 0.5

'''
def computeBollingerBands(start, end, N, bollinger_band_multiplier)
    for i in range(start + N, end):
        closePrices = getClosePriceForPeriod(i - N, i)
        middleband[i] = calcSMA(closePrices)
        sd[i] = calcSD(middleband[i], closePrices)
        upperband[i] = middleband[i] + bollinger_band_multiplier * sd[i]
        lowerband[i] = middleband[i] - bollinger_band_multiplier * sd[i]
    return (middleband, upperband, lowerband)
'''
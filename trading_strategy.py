__author__ = 'Michyo'

import helper
import datetime

print ""
print "* --- * --- * --- * --- * --- * --- *"
print ""
print "--- NAME: RSI LINES ---"
print datetime.datetime.now()
print "--- START ---"

all_files = helper.findFilesInFolder(0)
first_20_files = all_files[0:20]
one_day_data = helper.getOneDayData(all_files[20])

first_20_prices = []
for f in first_20_files:
    prices_of_a_day = helper.getOneDayPrices(f)
    first_20_prices.append(prices_of_a_day)
first_20_close_prices = helper.getClosePrices(first_20_prices)
bollinger_the_21 = helper.calcBollinger(first_20_close_prices, 2)

print datetime.datetime.now(),
print " Bollinger Finished."

total_earn = 0
total_pay = 0
for i in range(0, len(one_day_data)):
    '''
    print i,
    print " sell ? ",
    print one_day_data[i][1],
    print " ",
    print bollinger_the_21[1],
    print " ",
    print bollinger_the_21[2]
    '''
    if one_day_data[i][1] > bollinger_the_21[1]:
        if i == len(one_day_data) - 1:
            earn = one_day_data[i][2]
        else:
            earn = one_day_data[i+1][2]
        print "SELL: ",
        print earn
        total_earn += earn
    if one_day_data[i][1] < bollinger_the_21[2]:
        if i == len(one_day_data) - 1:
            pay = one_day_data[i][3]
        else:
            pay = one_day_data[i+1][3]
        print "BUY: ",
        print pay
        total_pay += pay
PnL = total_earn - total_pay
print "PnL = ",
print PnL


print datetime.datetime.now()
print "--- END ---"
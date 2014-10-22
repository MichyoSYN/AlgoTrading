__author__ = 'Michyo'

import helper
import datetime
import sys

log_name = "logs/onestock_RSI_3.log"
log_file = open(log_name, "a")
sys.stdout = log_file

print ""
print "* --- * --- * --- * --- * --- * --- *"
print ""
print "--- NAME: Strategy 1 ---"
print "duration = 9, change bounds[25, 75]"
print datetime.datetime.now()
print "--- START ---"

all_files = helper.findFilesInFolder(0)
duration = 9

first_9_files = all_files[0:duration]
close_prices = []
for f in first_9_files:
    prices_of_a_day = helper.getOneDayPrices(f)
    close_prices.append(prices_of_a_day[-1])

files = all_files[duration:]
print "Files = ",
print files
total_earn, total_pay, total_buy_times, total_sell_times, win_days = [0]*5

for f in files:
    today_data = helper.getOneDayData(f)
    RSI = helper.calcRSI(today_data[-1][1], close_prices)
    print "File = ",
    print f,
    print " RSI = ",
    print RSI
    today_earn, today_pay, today_sell_times, today_buy_times, stock_amount = [0]*5
    for i in range(0, len(today_data)-1):
        if RSI > 75 and stock_amount == 1:
            earn = today_data[i+1][2] * stock_amount
            print today_data[i][0],
            print ": SELL at ",
            print earn
            today_earn += earn * stock_amount
            today_sell_times += stock_amount
            stock_amount = 0
        if RSI < 25 and stock_amount == 0:
            pay = today_data[i+1][3]
            print today_data[i][0],
            print ": BUY at ",
            print pay
            today_pay += pay
            today_buy_times += 1
            stock_amount += 1
    if stock_amount > 0:
        today_earn += today_data[-1][1] * stock_amount
        today_sell_times += stock_amount
        print "SELL all remain ",
        print stock_amount,
        print " stocks at ",
        print today_data[-1][1]

    total_buy_times += today_buy_times
    total_sell_times += today_sell_times
    total_earn += today_earn
    total_pay += today_pay
    print "Buy times = ",
    print today_buy_times
    print "Sell times = ",
    print today_sell_times
    print "Today earn = ",
    print today_earn - today_pay

    if today_earn - today_pay > 0:
        win_days += 1

    del close_prices[0]
    close_prices.append(today_data[-1][1])

total_trade_times = total_buy_times + total_sell_times
total_point_earned = total_earn - total_pay
print "Total trade times = ",
print total_trade_times
print "Total point earned = ",
print total_point_earned
print "Win days = ",
print win_days

print ""
print datetime.datetime.now()
print "--- END ---"
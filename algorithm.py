__author__ = 'Michyo'

import helper
import datetime
import sys

def log_head(test_name, log_name):
    log_file = open(log_name, "a")
    sys.stdout = log_file

    print ""
    print "* --- * --- * --- * --- * --- * --- *"
    print ""
    print "--- " + test_name + " ---"
    print datetime.datetime.now()
    print "--- START ---"

def log_tail():
    print ""
    print datetime.datetime.now()
    print "--- END ---"

def Bollinger_day_duration_slippage1(test_name, log_name, duration, bollinger_multiplier):
    log_head(test_name, log_name)
    print " >> Apply Bollinger strategy."
    print "duration = " + str(duration) + ";" \
            " multipier = " + str(bollinger_multiplier)

    all_files = helper.findFilesInFolder(0)

    first_20_files = all_files[0:duration]
    # close_prices = []
    avg_prices = []
    for f in first_20_files:
        prices_of_a_day = helper.getOneDayPrices(f)
        # close_prices.append(prices_of_a_day[-1])
        avg_prices.append(helper.calcSMA(prices_of_a_day))

    files = all_files[duration:]
    print "Files = ",
    print files
    total_earn, total_pay, total_buy_times, total_sell_times, win_days = [0]*5

    for f in files:
        # bollinger = helper.calcBollinger(close_prices, bollinger_multiplier)
        bollinger = helper.calcBollinger(avg_prices, bollinger_multiplier)
        print "File = ",
        print f,
        print " Bollinger = ",
        print bollinger
        today_data = helper.getOneDayData(f)
        today_earn, today_pay, today_sell_times, today_buy_times, stock_amount = [0]*5
        today_prices = [] # avg_version
        for i in range(0, len(today_data)-1):
            today_prices.append(today_data[i][1]) # avg_version
            if today_data[i][1] > bollinger[1] and stock_amount == 1:
                earn = today_data[i+1][2] * stock_amount
                print today_data[i][0],
                print ": SELL at ",
                print earn
                today_earn += earn * stock_amount
                today_sell_times += stock_amount
                stock_amount = 0
            if today_data[i][1] < bollinger[2] and stock_amount == 0:
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

        # del close_prices[0]
        # close_prices.append(today_data[-1][1])
        today_prices.append(today_data[-1][1])
        today_avg = helper.calcSMA(today_prices)
        del avg_prices[0]
        avg_prices.append(today_avg)

    total_trade_times = total_buy_times + total_sell_times
    total_point_earned = total_earn - total_pay
    print "Total trade times = ",
    print total_trade_times
    print "Total point earned = ",
    print total_point_earned
    print "Win days = ",
    print win_days

    log_tail()



def RSI_day_duration_slippage1(test_name, log_name, duration, lower_bound, upper_bound):
    log_head(test_name, log_name)
    print " >> Apply RSI strategy."
    print "duration = " + str(duration) + "; " \
            "change bounds[" + str(lower_bound) + ", " + str(upper_bound) + "]"

    all_files = helper.findFilesInFolder(0)

    first_9_files = all_files[0:duration]
    # close_prices = []
    avg_prices = []
    for f in first_9_files:
        prices_of_a_day = helper.getOneDayPrices(f)
        # close_prices.append(prices_of_a_day[-1])
        avg_prices.append(helper.calcSMA(prices_of_a_day))

    files = all_files[duration:]
    print "Files = ",
    print files
    total_earn, total_pay, total_buy_times, total_sell_times, win_days = [0]*5

    for f in files:
        today_data = helper.getOneDayData(f)
        # RSI = helper.calcRSI(today_data[-1][1], close_prices)
        RSI = helper.calcRSI(today_data[-1][1], avg_prices)
        print "File = ",
        print f,
        print " RSI = ",
        print RSI
        today_earn, today_pay, today_sell_times, today_buy_times, stock_amount = [0]*5
        today_prices = [] # avg_version
        for i in range(0, len(today_data)-1):
            today_prices.append(today_data[i][1]) # avg_version
            if RSI > upper_bound and stock_amount == 1:
                earn = today_data[i+1][2] * stock_amount
                print today_data[i][0],
                print ": SELL at ",
                print earn
                today_earn += earn * stock_amount
                today_sell_times += stock_amount
                stock_amount = 0
            if RSI < lower_bound and stock_amount == 0:
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

        # del close_prices[0]
        # close_prices.append(today_data[-1][1])
        today_prices.append(today_data[-1][1])
        today_avg = helper.calcSMA(today_prices)
        del avg_prices[0]
        avg_prices.append(today_avg)

    total_trade_times = total_buy_times + total_sell_times
    total_point_earned = total_earn - total_pay
    print "Total trade times = ",
    print total_trade_times
    print "Total point earned = ",
    print total_point_earned
    print "Win days = ",
    print win_days

    log_tail()


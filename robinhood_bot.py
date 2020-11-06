# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:28:52 2020

@author: micha
"""

import robin_stocks as robin
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#import username and password from file
from robin_user import username
from robin_user import password

#login to robinhood
robin.login(username, password)

my_positions = robin.build_holdings()

dataf = pd.DataFrame(my_positions)
dataf = dataf.T
dataf['ticker'] = dataf.index
dataf = dataf.reset_index(drop=True)

#historical data for specific stocks
#example Tesla

tsla_data = robin.stocks.get_stock_historicals("TSLA",span='month',bounds='regular')
tsla = pd.DataFrame(tsla_data)

#switching numbers to float to allow pyplot to read them
column_list = ['close_price','high_price','low_price','open_price']
for i in column_list:
    tsla[i] = tsla[i].astype(float)
    
tsla['close_price'].plot(legend=True,figsize=(12,5))


spy_data = robin.options.find_tradable_options('SPY', optionType='call')

pd.DataFrame(spy_data)




#calculate expiration date that is 30 to 45 days from today
# YYYY/MM/DD correct formatting for profitability function
today = datetime.date.today()

#date = today.strftime("%Y-%m-%d")
#print("d1 =", d1)

#30 days ahead
thirty_days_out = datetime.timedelta(days=30)
#print(today + delta)

spy_data0 = robin.options.find_tradable_options('SPY', expirationDate=thirty_days_out, optionType='call')

pd.DataFrame(spy_data0)

#31 days ahead
thirty1_days_out = datetime.timedelta(days=31)
#print(today + delta)

spy_data1 = robin.options.find_tradable_options('SPY', expirationDate=thirty1_days_out, optionType='call')

pd.DataFrame(spy_data1)

#30 days ahead
thirty2_days_out = datetime.timedelta(days=32)
#print(today + delta)

spy_data2 = robin.options.find_tradable_options('SPY', expirationDate=thirty2_days_out, optionType='call')

pd.DataFrame(spy_data2)


# "Returns a list of option market data for several stock tickers that match a range of profitability."
#spy_thirty_long_data = robin.options.find_options_by_specific_profitability('SPY', expirationDate=thirty_days_out, strikePrice=None, optionType=None, typeProfit='chance_of_profit_long', profitFloor=0.0, profitCeiling=1.0)
#pd.DataFrame(spy_thirty_long_data)

#switching numbers to float to allow pyplot to read them
#column_list = ['inputSymbols','expirationDate','strikePrice','optionType', 'typeProfit']
#for i in column_list:
#    spy_thirty_long[i] = spy_thirty_long[i].astype(float)

#spy_thirty_long['close_price'].plot(legend=True,figsize=(12,5))
#30-45 day out iron condor on SPY
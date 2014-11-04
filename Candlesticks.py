# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:02:07 2014

@author: francescocorea
"""

# Candlesticks indicator and representation

from matplotlib.dates import DateFormatter as df, WeekdayLocator as wl, HourLocator as hl, DayLocator as dl, MONDAY
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo as yahoo, candlestick as cs, candlestick2 as cs2, plot_day_summary as pds
import numpy as np
from matplotlib import rc, rcParams

begdate=(2014, 9, 27)
enddate=(2014, 10, 27)

ticker='AAPL'

stock_price=yahoo(ticker,begdate,enddate)
if len(stock_price)==0:
    raise SystemExit 

rcParams['xtick.major.pad']='15'

figure,ax=plt.subplots()

ax.xaxis.set_major_locator(wl(MONDAY))
ax.xaxis.set_major_formatter(df("%b %d"))
ax.xaxis.set_minor_locator(dl())
ax.xaxis.set_minor_formatter(df("%d"))
pds(ax,stock_price,ticksize=1)
cs(ax,stock_price,width=0.5)
rc('xtick', labelsize=8)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=80,horizontalalignment='right')

plt.figtext(0.2,0.25, "Black if Open > Close")
plt.figtext(0.2,0.2, "White if Close > Open")
plt.title("Apple stock prices candlestick representation")
plt.ylabel("Days of trading")
plt.xlabel("Price")
plt.show()

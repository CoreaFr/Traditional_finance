# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 10:05:15 2014

@author: francescocorea
"""

# This file shows how several trading strategies works

from matplotlib.pyplot import *
import numpy as np
import bs_option

"Parmaters"
stock_price_t=15
stock_cost=10
exercise_price=15
call_price=2
put_price=1
sigma=0.3
r=0.05
T1=0.5
T2=1

strike_price_butterfly_1=50
strike_price_butterfly_3=60
strike_price_butterfly_2=(strike_price_butterfly_1+strike_price_butterfly_3)/2

call_butterfly_1=10
call_butterfly_2=7
call_butterfly_3=5

stock_market_price=np.arange(0,80,5)

# Covered Call (long position on a stock and short position on a call)

"Stock long position"

sy=stock_market_price-stock_cost

"Long position on a call"

cy=(abs(stock_market_price-exercise_price)+stock_market_price-exercise_price)/2-call_price

"Covered Call"

cc=sy-cy

plot(stock_market_price,sy,'b-.')
plot(stock_market_price,cy,'g-.')
plot(stock_market_price,cc,'r')
plot(stock_market_price,np.zeros(len(stock_market_price)), 'k--')

figtext(0.15,0.75,"Blue for stock, green for call, red for covered call")
title("Covered call payoff structure")
xlabel("Stock price")
ylabel("Payoff")

show()

# Stradlle (long on both call and put with same exercise price)

straddle=(abs(stock_market_price-exercise_price)+stock_market_price-exercise_price)/2-call_price + (abs(exercise_price-stock_market_price)+exercise_price-stock_market_price)/2-put_price

plot(stock_market_price,straddle)
plot(stock_market_price,np.zeros(len(stock_market_price)), 'k--')

title("Straddle payoff")
xlabel("Stock price")
ylabel("Payoff")

show()

# Calendar spread (Sell a call with maturity T1 and buy a call with maturity T2, where T2 > T1)

call_T1=bs_option.bs_call(stock_price_t,exercise_price,T1,r,sigma)
call_T2=bs_option.bs_call(stock_price_t,exercise_price,T2,r,sigma)

calendar_spread=-(abs(stock_market_price-exercise_price)+(stock_market_price-exercise_price)/2-bs_option.bs_call(stock_market_price,exercise_price,(T2-T1),r,sigma)) + (abs(stock_market_price-exercise_price)+(stock_market_price-exercise_price)/2-call_T2) - (abs(stock_market_price-exercise_price)+(stock_market_price-exercise_price)/2-call_T1)

ylim(-20,5)

plot(stock_market_price,calendar_spread)
plot(stock_market_price,np.zeros(len(stock_market_price)), 'k--')

title("Calendar Spread payoff")
xlabel("Stock price at time t")
ylabel("Payoff")

show()

# Butterfly strategy (long position on two calls with exercise price x1 < x3 and selling two calls with x2=(x1+x3)/2)

butterfly=((abs(stock_market_price-strike_price_butterfly_1)+stock_market_price-strike_price_butterfly_1)/2-call_butterfly_1) + ((abs(stock_market_price-strike_price_butterfly_3)+stock_market_price-strike_price_butterfly_3)/2-call_butterfly_3) - 2*((abs(stock_market_price-strike_price_butterfly_2)+stock_market_price-strike_price_butterfly_2)/2-call_butterfly_2)

ylim(-10,30)
xlim(0,75)

plot(stock_market_price,butterfly)
plot(stock_market_price,np.zeros(len(stock_market_price)), 'k--')

title("Butterfly payoff")
xlabel("Stock price at time t")
ylabel("Payoff")

show()
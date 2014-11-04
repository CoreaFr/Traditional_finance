# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 14:27:45 2014

@author: francescocorea
"""

# Monte Carlo simulation
import matplotlib.pyplot as plt
import scipy as sp
import time
start=time.clock()

stock_price_time_0=50
maturity=1.
steps=100
mu=0.15 # expected annual return
sigma=0.2

sp.random.seed(1)

number_simulations=10

Stock_price=sp.zeros(steps,dtype=float)

Stock_price[0]=stock_price_time_0

final_prices=[]

for j in range(0, number_simulations):
    for i in range(0,steps-1):
        epsilon=sp.random.standard_normal()
        Stock_price[i+1]=Stock_price[i]+Stock_price[i]*((mu-0.5*sigma**2)*maturity/steps + sigma*epsilon*sp.sqrt(maturity/steps))
    
    plt.plot(range(0,steps),Stock_price)
    final_prices.append(Stock_price[steps-1])
    
average_price=sp.mean(final_prices)
print "Stock price: " + str(average_price)
    
efficiency=time.clock()-start
print "Efficiency: " + str(efficiency)
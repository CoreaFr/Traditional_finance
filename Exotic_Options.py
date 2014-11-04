# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 09:41:26 2014

@author: francescocorea
"""

# How to price exotic options (since for most of them there is not any closed formula to price them correctly, we are going to use Monte Carlo Simulation for pricing them)

import scipy as sp
import bs_option as bs

"Asian Option (Average option)"

def Asian_call(S,K,T,r,sigma,n_simulation,n_steps):
    call=sp.zeros(n_simulation,dtype=float)
    stock_price_t=S
    total=0
    for i in range(0,n_simulation):
        for j in range(0,n_steps):
            sp.random.seed(1)
            epsilon=sp.random.standard_normal()
            stock_price_t*=sp.exp((r-0.5*sp.power(sigma,2))*T/n_steps + sigma*epsilon*sp.sqrt(T/n_steps))
            total+=stock_price_t
    call[i]=max(total/n_steps-K,0)
    
    print "The call price is" +str(sp.mean(call)*sp.exp(-r*T))

def Asian_put(S,K,T,r,sigma,n_simulation,n_steps):
    put=sp.zeros(n_simulation,dtype=float)
    stock_price_t=S
    total=0
    for i in range(0,n_simulation):
        for j in range(0,n_steps):
            sp.random.seed(2)
            epsilon=sp.random.standard_normal()
            stock_price_t*=sp.exp((r-0.5*sp.power(sigma,2))*T/n_steps + sigma*epsilon*sp.sqrt(T/n_steps))
            total+=stock_price_t
    put[i]=max(K-total/n_steps,0)
    
    print "The put price is" +str(sp.mean(put)*sp.exp(-r*T))
    
    
"Lookback Option (path-dependent option)"

def lookback_floating_strike(S,K,T,r,sigma,n_simulation,n_steps):
    minimum_price=100000
    stock_price_t=S    
    total=0
    for i in range(0, n_simulation):
        for j in range(0, n_steps):
            sp.random.seed(5)
            epsilon=sp.random.standard_normal()
            stock_price_t*=sp.exp((r-0.5*sp.power(sigma,2))*T/n_steps + sigma*epsilon*sp.sqrt(T/n_steps))
        if stock_price_t < minimum_price:
            minimum_price=stock_price_t
            total+=bs.bs_call(S,minimum_price,T,r,sigma)
    print "The lookback price is" + str(total/n_simulation)
                
    
"Barrier Option"

def Barrier_down_in_put(S,K,T,r,sigma,n_simulation,n_steps,barrier):
    stock_price_t=S
    in_barrier=False
    total=0
    for i in range(0,n_simulation):
        for j in range(0, n_steps):
            sp.random.seed(3)
            epsilon=sp.random.standard_normal()
            stock_price_t*=sp.exp((r-0.5*sp.power(sigma,2))*T/n_steps + sigma*epsilon*sp.sqrt(T/n_steps))
            if stock_price_t<barrier:
                in_barrier=True
        if in_barrier==True:
            total+=bs.bs_put(S,K,T,r,sigma)
    print "The down-and-in put value is" + str(total/n_simulation)
    
def Barrier_up_out_call(S,K,T,r,sigma,n_simulation,n_steps,barrier):
    stock_price_t=S
    out=False
    total=0
    for i in range(0,n_simulation):
        for j in range(0, n_steps):
            sp.random.seed(4)
            epsilon=sp.random.standard_normal()
            stock_price_t*=sp.exp((r-0.5*sp.power(sigma,2))*T/n_steps + sigma*epsilon*sp.sqrt(T/n_steps))
            if stock_price_t>barrier:
                out=True
        if out==False:
            total+=bs.bs_call(S,K,T,r,sigma)
    print "The up-and-out call value is" + str(total/n_simulation)
    

            
    

    
            
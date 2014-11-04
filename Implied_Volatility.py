# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:07:28 2014

@author: francescocorea
"""

# How to estimate implied volatility

import bs_option
import time

start=time.clock()

def implied_volatility(S,K,T,r,call_price,put_price):
    
        i=1; j=1 
        difference_with_call=1
        difference_with_put=1
        
        while abs(difference_with_call)>0.01:
            sigma_call=0.005*(i+1)
            difference_with_call=call_price-bs_option.bs_call(S,K,T,r,sigma_call)
            i+=1    
        print (i,sigma_call, difference_with_call) 

        while abs(difference_with_put)>0.01:
            sigma_put=0.005*(j+1)
            difference_with_put=put_price-bs_option.bs_put(S,K,T,r,sigma_put)
            j+=1    
        print (j,sigma_put, difference_with_put) 

efficiency=(time.clock()-start)   
print efficiency 

""" With for loop you get similar results, but it is a bit less efficient in the sense that you have to specify the max_iterations you want to go through:

def implied_volatility(S,K,T,r,call_price,put_price,max_iterations):
        for i in range(max_iterations):
            sigma_call=0.005*(i+1)
            if abs(call_price-bs_option.bs_call(S,K,T,r,sigma_call))<=0.01:
                print (i,sigma_call, call_price-bs_option.bs_call(S,K,T,r,sigma_call)) 

        for j in range(max_iterations):
            sigma_put=0.005*(j+1)
            if abs(put_price-bs_option.bs_put(S,K,T,r,sigma_put))<=0.01:
                print (i,sigma_put, put_price-bs_option.bs_put(S,K,T,r,sigma_put)) 

"""

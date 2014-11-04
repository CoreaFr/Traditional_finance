# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:32:32 2014

@author: francescocorea
"""

# 3 - Discounted Payback Period 
  
def Discounted_Payback_Period(cashflows,rate,critical_value):
    cumulative_value_discounted=0.0
    initial_value=cashflows[0]
    n=1
    while (cumulative_value_discounted<abs(initial_value)):
        cumulative_value_discounted+=cashflows[n]/(1+rate)**n 
        n+=1
    else:
        dpayback = (n-1 + (abs(initial_value)-cumulative_value_discounted)/(cashflows[n-1]/(1+rate)**(n-1)))
        return dpayback
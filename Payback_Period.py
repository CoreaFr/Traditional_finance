# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:32:32 2014

@author: francescocorea
"""

# 2 - Payback Period

def Payback_Period(cashflows,critical_value):
    cumulative_value=0.0
    initial_value=cashflows[0]
    n=1
    while (cumulative_value<abs(initial_value)):
        cumulative_value+=cashflows[n]
        n+=1
    else:
        payback = (n-1 + (abs(initial_value)-cumulative_value)/cashflows[n-1])
        return payback
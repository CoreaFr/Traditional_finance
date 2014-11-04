# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:43:01 2014

@author: francescocorea
"""

# 5 - Internal Rate of Return
from Net_Present_Value import Net_Present_Value as npv

def Interal_Rate_Return(cashflows, required_rate, interactions=1000):
    rate=1.0
    for i in range(1,interactions+1):
        rate*=(1-npv(cashflows, rate)/cashflows[0])
    return rate

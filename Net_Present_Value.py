# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:32:31 2014

@author: francescocorea
"""

# 1 - Net Present Value

def Net_Present_Value(cashflows, rate):
    total_value=0.0
    for n, cashflow in enumerate(cashflows):
        total_value+= cashflow/(1+rate)**n
    return total_value

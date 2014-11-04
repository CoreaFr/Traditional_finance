# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:32:33 2014

@author: francescocorea
"""

# 4 - Profitability Index   
    
def Profitability_Index(cashflows, rate):
    total_value=0.0
    for n, cashflow in enumerate(cashflows):
        total_value+= cashflow/(1+rate)**n
    p_index=1+total_value/abs(cashflows[0])
    return p_index
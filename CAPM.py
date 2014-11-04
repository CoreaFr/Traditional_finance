# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 15:09:45 2014

@author: francescocorea
"""

# Capital Asset Pricing Model
from scipy import stats 

stock_return=[]
market_return=[]

beta,alpha,r_value,p_value,std_err=stats.linregress(stock_return,market_return)

print "Alpha=", alpha
print "Beta=", beta
print "R-squared=", r_value**2
print "P-value=", p_value
print "Standard_error=", std_err
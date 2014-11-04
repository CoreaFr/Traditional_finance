# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 12:10:19 2014

@author: francescocorea
"""

from scipy import stats,log,exp,sqrt

# How to price a European Call Option through Black-Scholes formula

def bs_call(S,K,T,rf,sigma):
    d1=(log(S/float(K))+(rf+sigma**2/2.)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-K*exp(-rf*T)*stats.norm.cdf(d2)

# How to price a European Put Option through Black-Scholes formula

def bs_put(S,K,T,rf,sigma):
    d1=(log(S/float(K))+(rf+sigma**2/2.)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return K*exp(-rf*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1)

# How to compute the delta of the Call

def delta_call(S,K,T,rf,sigma):
    d1=(log(S/float(K))+(rf+sigma**2/2.)*T)/(sigma*sqrt(T))
    return d1

#How to compute the delta of the Put

def delta_put(S,K,T,rf,sigma):
    delta_call(S,K,T,rf,sigma)
    return delta_call(S,K,T,rf,sigma)-1


# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 12:13:26 2014

@author: francescocorea
"""
# This file presents several project selection methods
from Payback_Period import Payback_Period as pbp
from Discounted_Payback_Period import Discounted_Payback_Period as dpbp
from Profitability_Index import Profitability_Index as pindex
from Interal_Rate_Return import Interal_Rate_Return as IRR
from Net_Present_Value import Net_Present_Value as npv

# The following input are given as examples, but they can be modified.

cashflows=[-10,2,2,2,2,2,2,2,2,2,2]
rate= 0.1
required_rate=0.1
time_deadline=10

npv(cashflows,rate)
pbp(cashflows,time_deadline)
dpbp(cashflows,rate, time_deadline)
pindex(cashflows, rate)
IRR(cashflows, required_rate, interactions=1000)

if npv(cashflows, rate)>0:
    print "The NPV is %s, accept the project!" % npv(cashflows, rate)
else:
    print "The NPV is negative, reject the project."
    

if pbp(cashflows,time_deadline)<time_deadline:
    print "The project recovers the initial investment in {0}, that is less than the {1} years time required. Accept the project!".format(pbp(cashflows,time_deadline), time_deadline )
else:
    print "The project does not recover the investment on time. Reject it."        
    

if dpbp(cashflows,rate, time_deadline)<time_deadline:
    print "The project recovers the initial investment in {0}, that is less than the {1} years time required. Accept the project!".format(dpbp(cashflows,rate,time_deadline), time_deadline )
else:
    print "The project does not recover the investment on time. Reject it."        
    
    
if pindex(cashflows, rate)>1:
    print "The Profitability Index is %s and it is greater than 1, so accept the project!" % pindex(cashflows, rate)
else:
    print "The Profitability Index is less than 1, reject the project."


if IRR(cashflows, required_rate, interactions=1000)>required_rate:
    print "The IRR is {0}, and it is greater than {1} required rate, so accept the project!".format(IRR(cashflows, required_rate, interactions=1000), required_rate)
else:
    print "The IRR is less than the required rate, you should not accept the project."
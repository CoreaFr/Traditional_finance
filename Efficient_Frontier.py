# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:51:11 2014

@author: francescocorea (This file is based on Yan's book)
"""

# Efficient Frontier for two correlated stocks

import matplotlib.pyplot as plt 
import numpy as np
from scipy.optimize import minimize as mnm
import scipy as sp
import pandas as pd
from datetime import datetime as dt

"Parameters"
mean_vector=(0.15, 0.25)
std_vector=(0.1, 0.2)
correlation=0.2
number_simulation=1000
number_stock=len(mean_vector)

sp.random.seed(1)
x1_uncorrelated=sp.random.normal(loc=mean_vector[0],scale=std_vector[0],size=number_simulation) # data input for DataFrame function
x2_uncorrelated=sp.random.normal(loc=mean_vector[1],scale=std_vector[1],size=number_simulation)

x1_correlated=pd.DataFrame(x1_uncorrelated,index=pd.date_range(start=dt(2001,9,11),periods=number_simulation,freq='D'))
x2_correlated=pd.DataFrame(x1_uncorrelated*correlation+np.sqrt((1-correlation**2))*x2_uncorrelated,index=pd.date_range(start=dt(2001,9,11),periods=number_simulation,freq='D'))

return_matrix=np.array(pd.merge(x1_correlated,x2_correlated,left_index=True,right_index=True))

def ObjectiveFunction(weight,return_matrix,target_return):
    portfolio_mean=np.dot(weight,sp.mean(return_matrix,axis=0))
    portfolio_std=np.sqrt(np.dot(np.dot(weight,np.cov(return_matrix.T)),weight.T))
    
    penalty_to_minimize=2000*abs(portfolio_mean-target_return)
    return portfolio_std + penalty_to_minimize
    
"Procedure to estimate the optimal portfolio"

optimal_mean, optimal_std, optimal_weight=[],[],[]

for r_target in np.linspace(np.min(np.mean(return_matrix,axis=0)),np.max(np.mean(return_matrix,axis=0)),num=100):
    weight=np.ones([number_stock])/number_stock
    bound=[(0,1) for i in range(number_stock)]
    constraint=({'type':'eq', 'fun': lambda weight: sum(weight)-1.})
    result=mnm(ObjectiveFunction,weight,(return_matrix,r_target),method='SLSQP',constraints=constraint,bounds=bound) 
    if not result.success:
        raise BaseException(result.message)
    optimal_mean.append(r_target)
    optimal_std.append(np.std(np.sum(return_matrix*result.x,axis=1)))
    optimal_weight.append(result.x)
    
plt.title("Efficient Frontier given two correlated stocks")
plt.xlabel("Standard deviations")
plt.ylabel("Stock returns")
plt.plot(np.array(std_vector),np.array(np.mean(return_matrix,axis=0)),'o')
plt.plot(optimal_std,optimal_mean,'--')


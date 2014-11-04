# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 11:55:42 2014

@author: francescocorea
"""

# How to interpolate a set of values

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x=np.linspace(0,20,30, endpoint=True)
y=np.exp(-x**2/3)

f1=interp1d(x,y)
f2=interp1d(x,y,kind='slinear')
f3=interp1d(x,y,kind='cubic')

plt.plot(x,y,'o',x,f1(x),'r-',x,f2(x),'bs',x, f3(x),'g^')
plt.legend(['data','linear','spline first-order','cubic'],loc='best')
plt.xlabel("x-axis")
plt.ylabel("y-axis:-x^2/3")
plt.title("Interpolation")
plt.show()
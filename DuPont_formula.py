# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 15:58:15 2014

@author: francescocorea
"""

# DuPont formula for ROE

import numpy as np
import matplotlib.pyplot as plt

ROE=[0.134, 0.24]
tax_burden=[0.667,0.60]
interest_burden=[0.857,1]
ebit_margin=[0.07,0.111]
asset_turnover=[2,3]
financial_leverage=[1.67,1.2]

ind=np.arange(2)
width=0.5   

plot_tax_burden=plt.bar(ind,tax_burden,width,color='b')
plot_asset_turnover=plt.bar(ind,asset_turnover,width, color='k', bottom=tax_burden)
plot_financial_leverage=plt.bar(ind,financial_leverage,width,color='y',bottom=[asset_turnover[j]+tax_burden[j] for j in range(2)])
plot_interest_burden=plt.bar(ind,interest_burden,width,color='r',bottom=[financial_leverage[j]+asset_turnover[j]+tax_burden[j] for j in range(2)])
plot_ebit_margin=plt.bar(ind,ebit_margin,width,color='g',bottom=[interest_burden[j]+financial_leverage[j]+asset_turnover[j]+tax_burden[j] for j in range(2)])

plt.figtext(0.18,0.83,"ROE=0.134")
plt.figtext(0.67, 0.83, "ROE=0.24")

plt.title("DuPont extended decomposition")
plt.xlabel("Companies")
plt.ylabel("Tax burden, Interest burden, EBIT margin, Asset turnover, Financial leverage")
plt.show()
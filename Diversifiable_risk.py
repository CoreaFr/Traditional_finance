# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 09:57:49 2014

@author: francescocorea
"""

# How to understand diversifiable and non-diversifiable risk. The market does not compensate for a risk you can reduce diversifying!

# All the data and analysis are based on Statman's paper (1987).
from matplotlib.pyplot import *

n=[1,2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,75,100,200,300,400,500,600,700,800,900,1000]
sigma_portfolio=[0.49236,0.37358,0.29687,0.26643,0.24983,0.23932,0.23204, 0.22670,0.22261,0.21939,0.21677,0.21196,0.20870,0.20634,0.20456,0.20316,0.20203,0.19860,0.19686,0.19432,0.19336,0.19292,0.19265,0.19347,0.19233,0.19224,0.19217,0.19211,]


table_image=cbook.get_sample_data('Statman')
image=imread(table_image)
imshow(image)
axis('off')



xlim(0,100)
ylim(0,0.5)
hlines(0.19217, 0, 100,  colors='r', linestyles='dashed')

figtext(0.10,0.45,"Diversifiable risk")
annotate('',xy=(5, 0.19), xycoords = 'data',xytext = (5, 0.28),textcoords = 'data',arrowprops = {'arrowstyle':'<->'})

figtext(0.6,0.3,"Systematic risk")
annotate('', xy=(60, 0.19), xycoords = 'data',xytext = (60, 0.01),textcoords = 'data',arrowprops = {'arrowstyle':'<->'})

annotate('Total portfolio risk', xy=(5,0.3),xytext=(25,0.35),arrowprops=dict(facecolor='black',shrink=0.02))

plot(n,sigma_portfolio)

title("Diversifiable VS Systematic risk")
xlabel("Number of stocks into the portfolio")
ylabel("Risks")
show()
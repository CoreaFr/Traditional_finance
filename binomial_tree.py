# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 12:43:55 2014

@author: francescocorea
"""

# How to price options through binomial tree

import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt,exp

"Binomial tree pricing model"

def call_pricing(S,K,T,r,sigma,q,steps):
    
    u=exp(sigma*sqrt((float(T)/12)/steps)) # What it is inside the sqrt brackets is the time duration of a single step in annual terms
    d=1./u
    a=exp((r-q)*((float(T)/12)/steps))
    p=(a-d)/(u-d)
    value=[[0.0 for j in xrange(i+1)] for i in xrange(steps+1)]
    # Terminal value
    for j in xrange(i+1):
        value[steps][j]=max(S*u**j*d**(steps-j)-K,0.0)
    # Discounting process through risk neutral probability p
    for i in xrange(steps-1,-1,-1):
        for j in xrange(i+1):
            value[i][j]=(p*value[i+1][j+1]+(1.0-p)*value[i+1][j])*exp(-r*(float(T)/12)/steps)
    return value[0][0] # Present Value

def put_pricing(S,K,T,r,sigma,q,steps):
    
    u=exp(sigma*sqrt((float(T)/12)/steps)) # What it is inside the sqrt brackets is the time duration of a single step in annual terms
    d=1./u
    a=exp((r-q)*((float(T)/12)/steps))
    p=(a-d)/(u-d)
    value=[[0.0 for j in xrange(i+1)] for i in xrange(steps+1)]
    # Terminal value
    for j in xrange(i+1):
        value[steps][j]=max(K-S*u**j*d**(steps-j),0.0)
    # Discounting process through risk neutral probability p
    for i in xrange(steps-1,-1,-1):
        for j in xrange(i+1):
            value[i][j]=(p*value[i+1][j+1]+(1.0-p)*value[i+1][j])*exp(-r*(float(T)/12)/steps)
    return value[0][0] # Present Value

def acall_pricing(S,K,T,r,sigma,q,steps):
    
    u=exp(sigma*sqrt((float(T)/12)/steps)) # What it is inside the sqrt brackets is the time duration of a single step in annual terms
    d=1./u
    a=exp((r-q)*((float(T)/12)/steps))
    p=(a-d)/(u-d)
    value=[[0.0 for j in xrange(i+1)] for i in xrange(steps+1)]
    # Terminal value
    for j in xrange(i+1):
        value[steps][j]=max(S*u**j*d**(steps-j)-K,0.0)
    # Discounting process through risk neutral probability p
    for i in xrange(steps-1,-1,-1):
        for j in xrange(i+1):
            value_late_exercise=(p*value[i+1][j+1]+(1.0-p)*value[i+1][j])*exp(-r*(float(T)/12)/steps)
            value_early_exercise=max(S-K,0.0)
            value[i][j]=max(value_late_exercise,value_early_exercise)
    return value[0][0] # Present Value

def aput_pricing(S,K,T,r,sigma,q,steps):
    
    u=exp(sigma*sqrt((float(T)/12)/steps)) # What it is inside the sqrt brackets is the time duration of a single step in annual terms
    d=1./u
    a=exp((r-q)*((float(T)/12)/steps))
    p=(a-d)/(u-d)
    value=[[0.0 for j in xrange(i+1)] for i in xrange(steps+1)]
    # Terminal value
    for j in xrange(i+1):
        value[steps][j]=max(K-S*u**j*d**(steps-j),0.0)
    # Discounting process through risk neutral probability p
    for i in xrange(steps-1,-1,-1):
        for j in xrange(i+1):
            value_late_exercise=(p*value[i+1][j+1]+(1.0-p)*value[i+1][j])*exp(-r*(float(T)/12)/steps)
            value_early_exercise=max(K-S,0.0)
            value[i][j]=max(value_late_exercise,value_early_exercise)
    return value[0][0] # Present Value
    
"Creating the tree"

def binomial_tree(steps):
    G=nx.Graph()
    for i in range(0,steps+1):
        for j in range(1,i+2):
            if i<steps:
                G.add_edge((i,j),(i+1,j))
                G.add_edge((i,j),(i+1,j+1))
    position={}
    for node in G.nodes():
        position[node]=(node[0],steps+2+node[0]-2*node[1])
    nx.draw(G,pos=position)

"CRR visualized model "

def CRR_model(S,K,T,r,sigma,q,steps):
    
    print "The European call value is $ " + str(call_pricing(S,K,T,r,sigma,q,steps)) 
    print "The European put value is $ " + str(put_pricing(S,K,T,r,sigma,q,steps))
    print "The American call value is $ " + str(acall_pricing(S,K,T,r,sigma,q,steps))
    print "The American put value is $ " + str(aput_pricing(S,K,T,r,sigma,q,steps))
    
    plt.show(binomial_tree(steps))

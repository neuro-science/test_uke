#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:15:16 2020

@author: peng_wang
"""

### 1. a general function test
### There is 1 rich landlord in a 1000 population village.
### If the landload produce R0 male landloads every generation,
### other 30% extinct, 40% 1 male descendant,
### 25% 2 male descenedants, 5% 3 male descendants.
### what is the proportion of landlords after n generation?

def loop_pop_function(n, X, N):
   R0 = 3
   Rn = 0.4+0.25*2+0.05*3
   for k in range(n):
      X = X * R0
      N = N * Rn
   y = X / (X + N)
   print('After {0:d} generations, there are {1:d} male landlords and {2:d} male peasants, which yield {3:5.2f}% of noblity.'.format(n, int(X), int(N), 100*y))
   return y

#X = 1
#N = 1000/2 - 1
#n = 7
#y = loop_pop_function(n, X, N)
y = loop_pop_function(10, 5, 6e7)   #Across ~250 years of Ming Dynasty, Royal family grows from 5 males to ~0.3M



### 2.


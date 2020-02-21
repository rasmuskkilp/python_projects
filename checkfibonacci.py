#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:44:01 2020

@author: rasmuskaarelkilp
"""

#This is fibonacci check
import math

def isperfectsquare(x):
        s = int(math.sqrt(x))
        return s*s == x
def isfibonacci(n):
     # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square
    return isperfectsquare(5*n*n + 4) or isperfectsquare(5*n*n - 4)
for i in range(1,50):
    if isfibonacci(i) == True:
        print(i," is a fibonacci number")
    else:
        print(i," is not a fibonacci number")
        
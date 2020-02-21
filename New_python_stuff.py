#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:10:34 2020

@author: rasmuskaarelkilp
"""
#Input: num1 = 5, num2 = 3
#Output: 8

#Input: num1 = 13, num2 = 6
#Output: 19
input1 = float(input("first number:"))
input2 = float(input("second number:"))
summation = float(input1) + float(input2)
#print ("this is the sum of {input1} and {input2}: {summation} ".format(input1, input2, summation))
print(f"{summation} this is the sum of  {input1} and {input2}" )
print( "{} is the sum of {} plus {}".format(summation,input1,input2))
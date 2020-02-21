#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:52:36 2020

@author: rasmuskaarelkilp
"""

#Find the largest element in an array
#Input : arr[] = {10, 20, 4}
#Output : 20

#Input : arr[] = {20, 10, 20, 4, 100}
#Output : 100
#array1 = {50,12,52,152,56}
#array2 = {3,215,21,22,54}
#arr = [array1,array2]
array1 = {50,12,52,152,56}
array2 = {3,215,21,22,54}
arr = [array1,array2]
n = len(arr)
def largest(arr,n):
    max = 0
    for j in arr:
        print(j)
        for i in j:
            print(i)
            if i > max:
                max = i
    return max
ans = largest(arr,n)

print("this is the largest value:", ans)
    
    
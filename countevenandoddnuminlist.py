#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:10:32 2020

@author: rasmuskaarelkilp
"""

#Input: list1 = [2, 7, 5, 64, 14]
#Output: Even = 3, odd = 2
list1 = [2, 7, 5, 64, 14]
#Input: list2 = [12, 14, 95, 3]
#Output: Even = 2, odd = 2
list2 = [12, 14, 95, 3]
ultlist = [list1,list2]
even_count, odd_count = 0, 0
for i in ultlist:
    for j in i:
        if j % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
print(f"the number of odds in the lists: {odd_count} and even numbers in list {even_count}")
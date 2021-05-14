# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:48:03 2021

@author: Atul Mishra
"""

'''
Picking Numbers

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1. 
'''

def pickingNumbers(a):
    # Write your code here
    # count = 0
    # for i in range(len(a)-1):
    #      if abs(a[i] - a[i+1]) <=1:
    #          count +=1
    #      else:
    #          pass
    # return count + 1.
    l = a
    maximum=0
    for i in l:
        # print('i',i)
        c=l.count(i)
        d=l.count(i-1)
        # print('c',c,'d',d)
        c=c+d
        # print('c',c)
        if c > maximum:
            maximum=c
            # print('max',maximum)
    return maximum

print(pickingNumbers([4,6,5,5,3,1]))
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:58:18 2021

@author: Atul Mishra
"""

'''
BINARY GAP

Find the longest subsequence of zeros in binary respresentation of an integer.

'''

def binary_gap(N):
    
    cnt = 0
    result = 0
    found_one = False
    
    i = N
    while i:
        if i & 1 == 1:
            
            if(found_one == False):
                found_one = True
            else:
                result = max(result,cnt)
            cnt = 0
        else:
            cnt +=1
        i >>=1
    
    return result

print(binary_gap(10))
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:09:51 2021

@author: Atul Mishra
"""

'''
SUBARRAY DIVISION

Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

    The length of the segment matches Ron's birth month, and,
    The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.

Example

s = [2,2,1,3,2]
d = 4
m =2

Lily wants to find segments summing to Ron's birth day,d=4 with a length equalling his birth month,m=2 . In this case, there are two segments meeting her criteria:[2,2] and [1,3].
'''

def subarray_div(s,d,m):
    count = 0
    
    # We need to have number/slicing_index which will create sliding window of lists for those many number of chocolate slices
    for sliding_index in range(len(s)-m+1): # sliding_index -> 5-2+1 = 4 -> range(0,4)
        if sum(s[sliding_index:sliding_index+m]) == d: # s[0:2],s[1:3],s[2,4] -> continous two pieces
            count +=1
    
    return count

print(subarray_div([2,2,1,3,2],4,2))
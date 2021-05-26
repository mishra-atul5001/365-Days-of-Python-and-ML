# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:07:16 2021

@author: Atul Mishra
"""

'''
TapeEquilibrium

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7 
        
        the function should return 1,
'''

def TapeEquilibrium(A):
    '''
    So, we will first build the basic case where P = 1. Will compute the LEFT and RIGHT sum and then their ABSOLUTE DIFFERENCES.
    Then we will loop from 2 to len(A) and for each index, we will add the LIST element to LEFT and subtract the same from RIGHT.
    
    Then minimum at every iteration to get the minimum distance
    '''
    
    P = 1
    n = len(A)
    LEFT = sum(A[:P])
    RIGHT = sum(A[P:])
    
    min_diff = abs(LEFT - RIGHT)
    
    for i in range(2,n):
        current_element = A[P-1]
        # print('current element is ',current_element)
        LEFT += current_element
        # print('LEFT sum has become:',LEFT)
        RIGHT -=current_element
        # print('RIGHT sum has become:',RIGHT)
        min_diff = min(min_diff,abs(LEFT - RIGHT))
        # print('Updated Minimum is:',min_diff)
    return min_diff

print(TapeEquilibrium([3,1,2,4,3]))

























# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:37:18 2021

@author: Atul Mishra
"""

'''
CyclicRotation

Short Problem Definition:
Rotate an array to the right by a given number of steps.

'''

def CyclicRotation(A, K):
    
    for e in range(K):
        A = [A[i-1] for i in range(len(A))]
        
    return A

print(CyclicRotation([3,8,9,5],2))


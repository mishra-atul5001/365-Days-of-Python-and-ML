# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:01:43 2021

@author: Atul Mishra
"""

'''
Circular Array Rotation

John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

Example: 
a = [3,4,5]
k = 2
queries = [1,2]

[3,4,5] -> [5,3,4] -> [4,5,3]
'''

def circularArrayRotation(a, k, queries):

    indices =[] 
    '''
    (k)%len(a) -> Gives us the exact element count we need and subtracting it from every int from index queries, we can fetch the circulating
    elements.
    '''
    for i in queries: 
        print(i,a[i-(k)%len(a)])
        indices.append(a[i-(k)%len(a)]) 
        
    return indices

print(circularArrayRotation([3,4,5], 2, [1,2]))

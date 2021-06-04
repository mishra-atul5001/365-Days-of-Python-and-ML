# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:22:23 2021

@author: Atul Mishra
"""

'''
MaxProductOfThree

A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.
'''
def MaxProductOfThree(list_to_check):
    
    '''
    This problem is more easy if we just use some MATHS.
    Step 1: Sort the LIST
    Step 2: Max product can only be achieved if the FIRST 2 negatives are multiplied with the LARGEST element and LAST 3 elements are multiplied.
    In this manner only, we can get the LARGEST PRODUCT.
    
    Ex: [-3,-2,2,1,4,5] -> If we sort if then [-3,-2,1,2,4,5] -> So two products will be MAX((-3*-2*5),(2*4*5)) -> (2*4*5) -> 40 
    '''
    list_to_check.sort()
    
    count = max(list_to_check[0]*list_to_check[1]*list_to_check[-1] , list_to_check[-1]*list_to_check[-2]*list_to_check[-3])
    return count

print(MaxProductOfThree([-3,-2,2,1,4,5]))

print(MaxProductOfThree([-3,1,2,-2,5,6]))

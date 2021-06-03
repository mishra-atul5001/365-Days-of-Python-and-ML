# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:22:10 2021

@author: Atul Mishra
"""

'''
Min Avg Two Slice

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.
'''




def MinAvgTwoSlice(A):
    min_indx = 0
    min_val = 10001
    
    for idx in range(0,len(A)-1):
        if (A[idx] + A[idx+1])/2.0 < min_val:
            min_indx = idx
            min_val = (A[idx] + A[idx+1])/2.0
        elif idx < len(A)-2 and (A[idx] + A[idx+1] + A[idx+2])/3.0 < min_val:
            min_indx = idx
            min_val = (A[idx] + A[idx+1] + A[idx+2])/3.0
    
    return min_indx

print(MinAvgTwoSlice([4,2,2,5,1,5,8]))






































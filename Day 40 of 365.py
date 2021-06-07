# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:36:19 2021

@author: Atul Mishra
"""

'''

TRIANGLE

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.
'''

def triangle(A):
    '''
    One quckest solution is to SORT the LIST and then JUST Iterate to check the SUM
    '''
    if 3 > len(A):
        return 0
    A.sort()
    for idx in range(len(A)-2):
        if A[idx] + A[idx + 1] > A[idx + 2]:
            return 1
    return 0

print(triangle([10,2,5,1,8,20]))
print(triangle([10,50,5,1]))
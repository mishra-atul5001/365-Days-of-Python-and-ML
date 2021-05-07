# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:41:37 2021

@author: Atul Mishra
"""

'''
Remove all consecutive duplicates from the string

Input  : aaaaabbbbbb
Output : ab

Input : geeksforgeeks
Output : geksforgeks

Input : aabccba
Output : abcba

'''

s = 'geeksforgeeks'

def func(s):
    j = 0
    S1 = s
    S1 = list(S1.rstrip())
    print(S1)
    for i in range(len(S1)):
        if S1[j] != S1[i]:
            j+=1
            S1[j] = S1[i]
    
    j +=1
    S1 = S1[:j]
    print(*S1, sep = "")
    
func(s)
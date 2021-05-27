# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:59:38 2021

@author: Atul Mishra
"""

'''
Problem Link: https://www.hackerrank.com/challenges/permutation-equation/problem
'''

def permutationEquation(p):
    
    '''
    This was tricky as INDEXES were supposed to be treated as VALUES in step 1 and then those VALUES are treated as INDEXES in step 2. Quite Interesting!
    So, we just loop in the LEN of LIST and for each INDEX NUMBER, we increament 1 as we have to fetch that number. Now we get an index and we have to increament that index, treat it as value in next step and then again find the increamented index.
    
    '''    
    total_len = len(p)
    for i in range(0,total_len):
        my_val = p.index(i+1) + 1
        # print(i,my_val)
        final_val = p.index(my_val)
        print(final_val + 1)
        
permutationEquation([2,3,1])
print()
permutationEquation([4 ,3 ,5 ,1 ,2])
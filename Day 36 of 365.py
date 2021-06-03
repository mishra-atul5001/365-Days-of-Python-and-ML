# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:34:16 2021

@author: Atul Mishra
"""

'''
Extra Long Factorials

Calculate and print the factorial of a given integer. 
'''

def Extra_Long_Factorials(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod*i
    return prod

print(Extra_Long_Factorials(25),'\n')
print(Extra_Long_Factorials(12),'\n')
print(Extra_Long_Factorials(111),'\n')
print(Extra_Long_Factorials(650),'\n')
print(Extra_Long_Factorials(9))
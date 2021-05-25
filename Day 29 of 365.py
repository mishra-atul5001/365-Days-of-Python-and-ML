# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:43:13 2021

@author: Atul Mishra
"""

'''

PermMissingElem

Find the missing element in a given permutation. 
'''

def permMissingElem(list_to_look):
    
    # Well this seems stright forward as we can get the number of elements that should be present by adding 1 to the exisitng list
    # Then we will apply the sum formula and subtract the sume of the list to find the missing value
    n = len(list_to_look) + 1
    real_sum = (n*(n+1))//2
    num_sum = sum(list_to_look)
    
    diff = real_sum - num_sum
    
    return diff

print(permMissingElem([2,3,1,5]))
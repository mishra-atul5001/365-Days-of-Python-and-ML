# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:56:34 2021

@author: Atul Mishra
"""

"""
Append List to Sum Target

You are given a list of integers nums and integers k and target. Consider an operation where we choose an integer -k ≤ e ≤ k and append it to nums.
Return the minimum number of operations required such that the sum of nums equals to target.

Constraints
    n ≤ 100,000 where n is the length of nums
    1 ≤ k < 2 ** 31

Example 1

Input
nums = [2, 1]
k = 3
target = 10
Output
3

Explanation
We can append [3, 3, 1] to get [2, 1, 3, 3, 1] for a total sum of 10.
"""

def append_num(nums,k,target):
    sum_nums = sum(nums)
    diff = abs(target - sum_nums)
    
    '''
    In the following code, firstly i find out the sum of list , then I found difference b/w the sum_nums and the target & 
    then divide it with k , if the division is completely being done , than I just returned the answer that I got from the 
    division BUT If the division isn't complete that means we have to add one more number in the list , 
    in that case return answer + 1
    '''
    
    count = diff//k
    
    if diff % k != 0:
        return count + 1
    
    return count

print(append_num([2,1],3,10))


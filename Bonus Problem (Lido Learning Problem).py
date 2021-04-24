# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:24:38 2021

@author: Atul Mishra
"""

"""
Lido Learnings - Phone Screen
Question 1: Given an array arr[], find the maximum j - i such that arr[j] > arr[i]
Expected: O(nlogn) or O(n) 

Example: [2,3,4,9]

"""
arr = [2,3,9,4,8,11,1]
index = 0
max_num = 1

        
while index < len(arr):
    # print('index',index)
    for j in range(1,len(arr)):
        # print('j',j)
        if arr[j] > arr[index]:
            current_max = j - index
            if max_num != 0 and max_num > current_max:
                pass
            else:
                max_num = current_max
            
    index +=1
        

print('max',max_num)
        

"""
List Min Replacement

Given a list of integers nums, replace every nums[i] with the smallest integer left of i. Replace nums[0] with 0.

Constraints
    1 ≤ n ≤ 100,000 where n is the length of nums

Input: nums = [10, 5, 7, 9]
Ouput: [0, 10, 5, 5]

Explanation:
    
    nums[0] = 0 by definition
    nums[1] = min(10)
    nums[2] = min(5, 10)
    nums[3] = min(7, 5, 10)

"""

def list_min_replacement(nums):
    nums_min = nums [0]
  
    nums[0] = 0
    for i in range(1,len(nums)):
        if nums_min < nums[i]:
            nums[i] = nums_min
        elif nums_min >= nums[i]:
            nums[i],nums_min = nums_min,nums[i]
    return nums

print(list_min_replacement([10, 5, 7, 9]))

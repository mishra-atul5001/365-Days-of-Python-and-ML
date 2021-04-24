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
        

        
    


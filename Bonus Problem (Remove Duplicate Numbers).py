# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:34:20 2021

@author: Atul Mishra
"""

"""
Remove Duplicate Numbers

Given a list of integers nums, remove numbers that appear multiple times in the list, while maintaining order of the appearance in the original list.
It should use O(k) space where k is the number of unique integers.

Constraints
    n ≤ 100,000 where n is the length of nums

Example 1

Input
nums = [1, 3, 5, 0, 3, 5, 8]

Output
[1, 0, 8]

Explanation
Only [1, 0, 8] are unique in the list and that's the order they appear in.
"""

from collections import Counter
def remove_duplicate_nums(nums):
    my_dict = {}
    
    # We use a hashmap and remove the elements where value is not 1, which results in removing duplicates!
    for num in nums:
        my_dict[num] = nums.count(num)
    
    # print(my_dict)
    count = []
    key_list=list(my_dict.keys())
    val_list=list(my_dict.values())
    for val in range(len(val_list)):
        if val_list[val] == 1:
            count.append(key_list[val])
    print('Cleaned List looks like!',count)

    return count

remove_duplicate_nums([1,3,5,0,3,5,8])

'''
Unfortunately, above solution exceeds time limit for huge test cases!. So we need to settle this in one go!
'''
def remove_duplicate_nums_m2(nums):
    freq = Counter(nums)
    # print(freq)
    n=len(nums)
    count = []
    '''
    Well, i thought, why don't we just remove the lement where we see it more than 1 time right!?'
    '''
    for i in range(n):

        # Print the element which appear
        # more than or equal to k times.
        if (freq[nums[i]] <= 1):
            # print(nums[i])
            count.append(nums[i])
                
    return count

print(remove_duplicate_nums_m2([1,3,5,0,3,5,8]))

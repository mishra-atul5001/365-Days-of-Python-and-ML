# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 10:37:15 2021

@author: Atul Mishra
"""

"""
Longest Consecutive Duplicate String

Given a lowercase alphabet string s, return the length of the longest substring with same characters.
Constraints
    0 ≤ n ≤ 100,000 where n is the length of s

Example 1

Input
s = "abbbba"

Output
4

Explanation
The longest substring is "bbbb".
"""

def find_longest_substring_length(string_to_look):
    
    # Final count variable
    count = 0
    
    # Count variable associated with each element
    current_elem_count = 1
    
    # We loop in the string and avoid the last element as it will be compared in second if condition
    for ix in range(len(string_to_look)):
        if ix < len(string_to_look) - 1 and string_to_look[ix] == string_to_look[ix+1]:
            
            # We update the current element/char count
            current_elem_count +=1
            
            # Now if we have consumed that char in a sequence, we update the count
        elif current_elem_count > count:
            count = current_elem_count
            
            # Else, we just start again from 1
            current_elem_count = 1
    
    return count

print(find_longest_substring_length('abbbba'))









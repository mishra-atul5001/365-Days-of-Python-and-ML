# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:34:18 2021

@author: Atul Mishra
"""

"""
NOISY PALINDROME

You are given a string s containing lowercase and uppercase alphabet characters as well as digits from "0" to "9". Return whether s is a palindrome if we only consider the lowercase alphabet characters.

Constraints
    0 ≤ n ≤ 100,000 where n is the length of s

Example 1

Input
s = "a92bcbXa"

Output
True

Explanation
If we only consider the lowercase characters, then s is "abcba" which is a palindrome.

Example 2

Input
s = "abZ"

Output
False
"""
import re
def noisy_palindrome(noisy_str):
    
    """
    Step 1: Remove Capital Letters, which we can do from regex.
    Step 2: Remove number from the cleaned STR
    Step 3: Just match it backwards.
    """
    
    regex = "[A-Z]"
    lower = re.sub(regex,"",noisy_str)
    regex = "[0-9]"
    good_str = re.sub(regex,"",lower)
    
    if good_str == good_str[::-1]:
        return True
    else:
        return False
    
    return


print(noisy_palindrome("a92bcbXa")) # True
print(noisy_palindrome("abZ")) # False
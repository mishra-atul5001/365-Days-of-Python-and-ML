# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:17:29 2021

@author: Atul Mishra
"""

"""
PALINDROMIC INTEGER

Example: 121
True

0
True

43
False
"""


def check_palindrome(num):
    yes_no = False
    
    # Fetch the numbers in a dictionary
    digits_list = [digit for digit in str(num)]
    
    # Combine the items in a reverse manner
    rev_num = ''
    for x in digits_list[::-1]:
        rev_num = rev_num + str(x)
        
    # Print the original and reversed nums
    print('original_num', num)
    print('reversed_num', int(rev_num))    
    
    # Compare if the reversed items are same or not!
    if digits_list == digits_list[::-1]:
        yes_no = True
    else:
        yes_no = False
    
    return yes_no

print('Palindrome? ->',check_palindrome(121),'\n')
print('Palindrome? ->',check_palindrome(0),'\n')
print('Palindrome? ->',check_palindrome(4774),'\n')
print('Palindrome? ->',check_palindrome(34),'\n')

"""
original_num 121
reversed_num 121
Palindrome? -> True 

original_num 0
reversed_num 0
Palindrome? -> True 

original_num 4774
reversed_num 4774
Palindrome? -> True 

original_num 34
reversed_num 43
Palindrome? -> False 
"""
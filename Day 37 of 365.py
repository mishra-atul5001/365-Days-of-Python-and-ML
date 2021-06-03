# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:21:46 2021

@author: Atul Mishra
"""

'''
Append and Delete

You have two strings of lowercase English letters. You can perform two types of operations on the first string:

    1. Append a lowercase English letter to the end of the string.
    2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.

Given an integer,k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No.
'''


def Append_and_Delete(s,t,k):
    my_s = [str(char) for char in s]
    my_t = [str(char) for char in t]
    
    my_instersections = set(my_t).intersection(my_s)
    print(my_instersections)
    print(len(my_instersections))
    
    if len(my_instersections) > k:
        print('No')
    elif len(my_t) - len(my_instersections) - 1 <= k:
        print('Yes')
    else:
        print('Yes')
        
Append_and_Delete('hackerhappy','hackerrank',9)
Append_and_Delete('ashley','ash',2)
Append_and_Delete('zzzzz','zzzzzzz',4)
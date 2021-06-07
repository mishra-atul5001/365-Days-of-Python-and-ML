# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:45:44 2021

@author: Atul Mishra
"""

'''
Brackets

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
'''

def brackets(left,right):
    if left == '[' and right ==']':
        return True
    elif left == '(' and right ==')':
        return True
    elif left == '{' and right =='}':
        return True
    return False

def solution(A):
    
    x = []
    for symbol in A:
        if symbol == '[' or symbol == '(' or symbol =='{':
            x.append(symbol)
        else:
            if len(x) == 0:
                return 0
            y = x.pop()
            if not brackets(symbol,y):
                return 0
            
    if len(x) != 0:
        return 0
    return 1

print(solution('{[()()]}'))
print(solution('([)()]'))
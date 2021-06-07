# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:45:57 2021

@author: Atul Mishra
"""

'''

Nesting

A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.
'''

def solution(S):
    x = []
    for symbol in S:
        if symbol == '(':
            x.append(symbol)
        else:
            if len(x) == 0:
                return 0
            y = x.pop()
            if symbol == '(' and y ==')':
                return 1
    if len(x)!=0:
        return 0
    return 1

print(solution('(()(())())'))
print(solution('())'))
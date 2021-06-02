# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:34:05 2021

@author: Atul Mishra
"""

'''
Find Digits

https://www.hackerrank.com/challenges/find-digits/problem
'''

n = 124
my_list = [int(x) for x in str(n)]
count = 0

for num in my_list:
    if num == 0:
        pass
    elif n%num == 0:
        count +=1

print(count)
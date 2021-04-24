# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:21:51 2021

@author: Atul Mishra
"""

"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

    - Print the three most common characters along with their occurrence count.
    - Sort in descending order of occurrence count.
    - If the occurrence count is the same, sort the characters in alphabetical order.

"""
x = {'a': 2, 'b':3, 'c': 2, 'd': 1, 'e':1}


from collections import Counter

chars = Counter(x).items()

for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)


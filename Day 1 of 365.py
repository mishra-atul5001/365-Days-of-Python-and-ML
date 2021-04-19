# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:23:37 2021

@author: Atul Mishra
"""

'''
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example

'aabbcdddde',2 -> Letters repeating 2 times are: #  a b
'aabbcdddde',4 -> Letters repeating 4 times are: #  d
'Indivisibilities',2 -> Letters repeating 2 times are: #  s

'''

def count_duplicates(input_str,input_val):
    my_dup_str = '# '
    split_list = list(input_str)
    
    # Let's count the duplicates and store them in dictionary.
    split_dict = {}
    for str_item in split_list:
        split_dict[str_item] = split_list.count(str_item)
        
    # Let's print the charactes having exact number of duplicates based on the input

    print('The Dictionary of words looks like:',split_dict)
    my_list = []
    for key,val in split_dict.items():
        if val == input_val:
            my_list.append(key)
            my_dup_str += ' ' + str(key)
    
    print('Letters repeating {} times are:'.format(input_val))
    
    return my_dup_str + '\n'

'''
Algorithm:
    1. Let's first split the String "input_str" into a List.
    2. Let's count the duplicated elements into a dictionary.
    3. Return the elements which have duplicated values greater than "input_val"
'''

print(count_duplicates('aabbcdddde',2))
print(count_duplicates('aabbcdddde',4))
print(count_duplicates('Indivisibilities',2))

'''
The Dictionary of words looks like: {'a': 2, 'b': 2, 'c': 1, 'd': 4, 'e': 1}
Letters repeating 2 times are:
#  a b

The Dictionary of words looks like: {'a': 2, 'b': 2, 'c': 1, 'd': 4, 'e': 1}
Letters repeating 4 times are:
#  d

The Dictionary of words looks like: {'I': 1, 'n': 1, 'd': 1, 'i': 6, 'v': 1, 's': 2, 'b': 1, 'l': 1, 't': 1, 'e': 1}
Letters repeating 2 times are:
#  s
'''





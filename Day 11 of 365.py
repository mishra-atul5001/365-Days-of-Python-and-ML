# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:12:27 2021

@author: Atul Mishra
"""

"""
No Idea!

There is an array of n integers. There are also 2 disjoint sets,A and B, each containing integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if ,i belongs A you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
param_input = input()
a = input()
main_list = list(map(int,a.split()))
A = input()
A_list = set(list(map(int,A.split())))
B = input()
B_list = set(list(map(int,B.split())))
happiness_score = 0

'''
Step 1: Fetch the input/main list as LIST and not set, otherwise you will loose the duplicates and that will affect your happiness score.
Step 2: Just loop in the main array and keep checking that element in the SET which should contain the number in a unique manner.
Step 3: Increament/Decreament 1 as per the number occurence.
'''

for i in main_list:
    if i in A_list:
        happiness_score +=1
    elif i in B_list:
        happiness_score -=1
    else:
        pass

print('My Happiness Score is:',happiness_score)


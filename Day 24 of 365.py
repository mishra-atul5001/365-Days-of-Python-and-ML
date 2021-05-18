# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:48:05 2021

@author: Atul Mishra
"""

'''

Utopian Tree

The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter. A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

'''

def utopianTree(n):

    '''
    Well, this one is easy, we just have to see if the SEASON is EVEN or ODD, coz if even, then it is SUMMER and if odd, then the season is     SPRING.
    The main thing to notice is that we need to loop from 1 to n instead of from 0 to n-1. This will exactly perform the TREE LEN addition and multiplication.
    '''
    tree_len = 1
    for i in range(1,n+1):
        if i%2 == 0:
            tree_len +=1
        elif i%2!=0:
            tree_len *=2
    return tree_len

n = [0,1,4]

for param in n:
    print(utopianTree(param))
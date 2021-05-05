# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:57:08 2021

@author: Atul Mishra
"""

'''
Save the Prisoner!

A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

Example

n = 4
m = 6
s = 2

There are 4 prisoners,6 pieces of candy and distribution starts at chair 2. The prisoners arrange themselves in seats numbered 1 to 4. Prisoners receive candy at positions 2,3,4,1,2,3. The prisoner to be warned sits in chair number 3. 
'''

def saveThePrisoner(n, m, s):
    """
    There are m sweets and n prisoners. since these n prisoners are sitting in a circular table, and the m sweetes being distributed starting from seat 's' , they are going to repeate after every (m+s-1), so its very simple to just take mod with n to get to remainder which gives you the last sweets position. Now suppose the remainder turns out to be 0, this means that the sweets with end at the very last prisoner which is sitting at position 'n' (because 'n' is the total number of prisoners), just do Dry Run by taking different value of m, n, 
    """

    # n is the number of prisoners
    # m is the number of sweets we have
    # s is the number of prisoner from which sweet distribution will happen.
    
    if((m + s -1)%n == 0):
        return(n)
    else:
        return ((m+s-1)%n) 
    
    
print(saveThePrisoner(4,6,2))
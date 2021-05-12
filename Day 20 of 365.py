# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:41:31 2021

@author: Atul Mishra
"""

'''

The Stolen Breakfast Drone 

Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.

Each breakfast delivery is assigned a unique ID, a positive integer. When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations. When the drone comes back and lands, the ID is again added to the same list.

After breakfast this morning there were only 99 drones on the tarmac. One of the drones never made it back from a delivery. We suspect a secret agent from Amazon placed an order and stole one of our patented drones. To track them down, we need to find their delivery ID.

Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer. 

'''


from collections import Counter

def find_stolen_drone(delivery_id_confirmations):
    
    '''
    Well, it is almost opposite of duplicate elements problem.
    We will just fetch the LIST in a DICTIONARY and look for VAL == 1. Once found, fetch that key!
    '''
    my_dict = Counter(delivery_id_confirmations)
    my_key = []
    for key,val in my_dict.items():
        if val == 1:
            my_key.append(key)
    
    return my_key

print(*find_stolen_drone([1,1,2,2,3,4])) # I use the asterisk to get the integers, instead of getting a LIST


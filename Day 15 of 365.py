# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:20:25 2021

@author: Atul Mishra
"""

'''
Electronics Shop

A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.


'''

def getMoneySpent(keyboards, drives, b):

    bill = []
    '''
    Step 1: Let's loop for each KEYBOARD PRICE
    Step 2: Fetch one price and add the next price from DRIVE PRICE for loop
    Step 3: Adding the prices and if the price is less than the BUDGET b, save it in the LIST
    Step 4: Check if the final list contains any element. If yes, return the MAX of the LIST, else -1
    '''
    
    for key_board in keyboards:
        for drive in drives:
            if key_board + drive <= b:
                bill.append(key_board + drive)
    
    if len(bill) == 0:
        return -1
    else:
        return max(bill)
    
print('Maximum Cost to buy them:',getMoneySpent([40,50,60], [5,8,12], 60),'Rs.')
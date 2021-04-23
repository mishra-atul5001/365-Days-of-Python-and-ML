# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:21:51 2021

@author: Atul Mishra
"""

"""
Given a list of integers prices representing prices of cars for sale, and a budget k, return the maximum number of cars you can buy.
Constraints
    n ≤ 200,000 where n is the length of prices

Example 

Input
prices = [90, 30, 20, 40, 90]
k = 95

Output
3

Explanation
We can buy the cars with prices 30, 20, and 40.

"""

def number_of_cars_to_buy(prices,k):
    car_count = 0
    prices.sort()
    remaining_money = k
    for price in range(len(prices)):

        if prices[price] <= remaining_money:

            car_count +=1
            remaining_money = remaining_money - prices[price]
        else:
            break
            
    return car_count



prices = [90, 30, 20, 40, 90]
k = 95

print(number_of_cars_to_buy(prices, k))

prices = [42,64,155]
k = 261

print(number_of_cars_to_buy(prices, k))
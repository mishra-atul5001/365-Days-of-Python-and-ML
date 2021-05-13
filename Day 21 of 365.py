# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:18:29 2021

@author: Atul Mishra
"""
'''
Beautiful Days at the Movies

Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days [i.....j], and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where |i - reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range.
'''

def beautifulDays(i, j, k):
    # Write your code here
    # beautiful_day = []
    count = 0
    '''
    Well, it's easy, now in order to reverse an integer also, normal type casting can help. Just convert INT to STR, reverse it and typecaste is back to INT. Voila, we have reverse value. Then take the sum/perform the mathematical operatin and return the count, whenever that operation is TRUE!'
    '''
    for m in range(i,j+1):
        temp_sum = abs(m - int(str(m)[::-1]))
        if temp_sum%k == 0:
            # beautiful_day.append(m)
            count +=1
    
    return count

print(beautifulDays(20,23,6))

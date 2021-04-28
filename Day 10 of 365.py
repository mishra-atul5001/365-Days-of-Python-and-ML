# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 09:54:13 2021

@author: Atul Mishra
"""

"""
UGLY NUMBER

Given an integer n, return whether its prime factors only include 2, 3 or 5.
Constraints
    0 ≤ n < 2 ** 31

Example 1

Input
n = 10

Output
True

Explanation
10's prime factors are 2 and 5.
"""

def is_ugly_number(number):
    
    
    '''
    Step 1: We will check wether the number is 0 or not, return FALSE if that is the case.
    Step 2: We will loop in the prime factor list and our main motive is to find wether the given number gets divided by all factors or not!.
    Step 3: Until the number return 1 upon continuous dividion by factors, we cannot say that factors are true.
    Step 4: Once, returned value is 1, that means, the factors are digested.
    '''
    prime_factors = [2,3,5]
    print('Welcome to Ugly Number Program!\nHere we will try to look wether the factors of your provided number lies in the following list {} or not!?\nYour entered number is {}\nIs your number UGLY!?'.format(prime_factors,number))
    
    if number == 0:
        return False
    else:
        for factor in prime_factors: # Factor: 2  || Factor: 3 || Factor: 5
            while number%factor == 0: # 10%2 == 0 (True) || 5%3 == 0 (False) || 5%5 == 0 (True)
                number = number/factor # number = 10/2 = 5 || Pass || number = 5/5 = 1 --> Final Answer is TRUE
    
    return number == 1

print(is_ugly_number(10),'\n')
print(is_ugly_number(14),'\n')
print(is_ugly_number(7),'\n')
print(is_ugly_number(3),'\n')
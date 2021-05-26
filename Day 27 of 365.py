# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:58:18 2021

@author: Atul Mishra
"""

'''
BINARY GAP

Find the longest subsequence of zeros in binary respresentation of an integer.

'''

def binary_gap(N):
    
    cnt = 0
    result = 0
    found_one = False
    
    i = N
    while i:
        if i & 1 == 1:
            
            if(found_one == False):
                found_one = True
            else:
                result = max(result,cnt)
            cnt = 0
        else:
            cnt +=1
        i >>=1
    
    return result

print(binary_gap(121))


# Another solution which is much easier
def binary_gap_sol2(N):
    
    # step1 = format(N,'b')
    # print('Step1 :',step1,'-> Number gets converted to its BINARY form')
    # step2 = format(N,'b').strip('0')
    # print('Step2 :',step2,'-> It removes all the trailing ZEROES')
    # step3 = format(N,'b').strip('0').split('1')
    # print('Step3 :',step3, '-> Here we split the BINARY number based on 1s and only keep ZEROES')
    # step4 = max(format(N,'b').strip('0').split('1'))
    # print('Step4 :',step4, '-> Here we take the MAXIMUM sequence and next step returns the count of that!')
    # step5 = len(max(format(N,'b').strip('0').split('1')))
    # print('Step5 :',step5)
    
    # Cumulatively is below:
    count = len(max(format(N,'b').strip('0').split('1')))
    return count

print(binary_gap_sol2(121))
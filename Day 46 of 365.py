# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:26:59 2021

@author: Atul Mishra
"""

'''
Multiprocessing in Python!

- 3 function performing different operations
- Will run them in a normal behaviour
- Then we will inject MULTIPROCESSING Method for these functions!
- Will monitor the RUN TIME of these functions separately!

'''

import multiprocessing as mp
import math
import time

result_1 = []
result_2 = []
result_3 = []

# This fnction will find the MAXIMUM PRODUCT of 3 integers from the incoming LIST 
def function_1(numbers):
    numbers.sort()
    my_max = max(numbers[0]*numbers[1]*numbers[-1],numbers[-1]*numbers[-2]*numbers[-3])
    result_1.append(my_max)

# This function will find the SQRT of INT**3
def function_2(numbers):
    for number in numbers:
        result_2.append(math.sqrt(number**3))
        
# This function will only perform SQRT for the incoming INTEGERS
def function_3(numbers):
    for number in numbers:
        result_3.append(math.sqrt(number))

# This part is necessary in order to tell my program not to messup when multi-processing is invoked
if __name__ == '__main__':
    
    numbers_list = list(range(10000000))
    
    # NORMAL RUN TIME FOR THE FUNCTIONS
    start = time.time()
    function_1(numbers_list)
    function_2(numbers_list)
    function_3(numbers_list)
    end = time.time()
    without_multi = end - start
    
    print('Time taken without multiprocessing:',round(without_multi,2))
    
    # RUN TIME WHEN THE SAME FUNCTIONS WITH MULTI_PROCESSING
    
    process_1 = mp.Process(target=function_1,args=(numbers_list,))
    process_2 = mp.Process(target=function_2,args=(numbers_list,))
    process_3 = mp.Process(target=function_3,args=(numbers_list,))
    
    start = time.time()
    process_1.start()
    process_2.start()
    process_3.start()
    end = time.time()
    with_multi = end - start
    print('Time taken WITH multiprocessing:',round(with_multi,2))
    
    print('After multi-processing, script is {} times faster.'.format(round(without_multi/with_multi,2)))
    
    
    
    
    
    
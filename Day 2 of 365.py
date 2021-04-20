
"""
Created on Tue Apr 20 20:15:02 2021

@author: Atul Mishra
"""

"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false


"""

def check_x_o_amount(input_str):
    equal_bool = 'false'
    
    '''
    Algorithm:
        Step 1: Break it into a Dictionary/Count of X and O. Lower case to be sure
        Step 2: Check for key as 'x' and 'o' and count their vals
        Step 3: Return based on equality achieved.
    '''
    x_count = 0
    o_count = 0
    
    input_str = input_str.lower()
    str_list = list(input_str)
    for char in str_list:
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1
        else:
            pass
    
    if x_count == o_count:
        equal_bool = 'true'
    else:
        pass
    
    return equal_bool

print(check_x_o_amount('ooxx'))
print(check_x_o_amount('xooxx'))
print(check_x_o_amount('ooxXm'))
print(check_x_o_amount('zzoo'))
print(check_x_o_amount('zpzpzpp'))
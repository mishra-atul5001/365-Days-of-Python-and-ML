# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:54:52 2021

@author: Atul Mishra
"""

# BINARY SEARCH

"""
Binary Search is an Iterative/Recursive methodology to find any element in any SORTED Array.

Steps involved are:
    1. Compare the element with the middle element of the list.
    If that_element > mid_element:
        we ignore left half of the list and make the search again in the right half
    Else if that_element < mid_element:
        we ignore right half of the list and make the search again in the left half.
    Else:
        we have reached there
        
    2. WE need variables like 'left_index' which will be '0' and 'right_index' which will be the 'len(list) - 1'.
    3. We perform 'mid_index + 1' to 'left_index' if we want to ignore the LEFT HALF and  'mid_index - 1' to 'right_index' to ignore the RIGHT HALF of the list.
"""

def binary_search(list_to_search,element_to_search):
    left_index = 0
    right_index = len(list_to_search) - 1
    mid = 0
    
    # Assuming that the element is present in the list, we stay inside the list until one of the index is exhausted
    while left_index <= right_index:
        mid = (right_index + left_index)//2
        
        # If element is smaller than middle element, move one step backward
        if  list_to_search[mid] > element_to_search:
            right_index = mid - 1
            
        # If element is greater than middle element, move one step forward.
        elif list_to_search[mid] < element_to_search:
            left_index = mid + 1
        
        # This would mean, that there is nowhere to go and we have reached that ELEMENT.
        else:
            return mid
     
    # If the element is not present in the list, it will return -1    
    return -1

list_to_search,element_to_search = [2,3,4,5,10,25],5
element_index = binary_search(list_to_search,element_to_search)

if element_index == -1:
    print('Man!, Make sure the number to be reported is present in the List!')

else:
    print('Element {} is present at index {}.'.format(element_to_search,element_index))
    print('Our original List is: {}'.format(list_to_search))
    

'''
Result:
    
Element 5 is present at index 3.
Our original List is: [2, 3, 4, 5, 10, 25]
'''
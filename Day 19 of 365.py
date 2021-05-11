# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:34:31 2021

@author: Atul Mishra
"""

'''
Drawing Book

A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page 1 is always on the right side.

When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is n pages long, and a student wants to turn to page p , what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.     

I/P:

    n = 6
    p = 2
    
O/P:
    
    1
    
'''

def pageCount(n, p):
    # Write your code here
    pages_to_turn = p//2
    total_turns = n //2
    
    print('Turns in which the whole book can be turned {}'.format(total_turns))
    print('Turns in which the specific page can be reached {}'.format(pages_to_turn))
    
    '''
    Now, in order to determine wether we start paging from left or right, we just need the minimum turns to figure that out.
    '''
    
    return min(pages_to_turn,(total_turns - pages_to_turn)) # min(1,2)

print('Total Turns to reach the page:',pageCount(6, 2),'\n')
print('Total Turns to reach the page:',pageCount(5, 3),'\n')
print('Total Turns to reach the page:',pageCount(5, 4),'\n')
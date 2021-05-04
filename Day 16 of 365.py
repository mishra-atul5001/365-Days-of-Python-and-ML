# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:41:43 2021

@author: Atul Mishra
"""

'''
Designer PDF Viewer

When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently.

There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight mm2 in assuming all letters are 1mm wide. 

Sample Input 0
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output 0
9

'''

def designerPdfViewer(h, word):
    # Write your code here
    char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    word = list(word.lower())
    word_list = []
    for i in range(len(char_list)):
            if char_list[i] in word:
                # word_list.append(i)
                word_list.append(h[i])
    
    max_num = max(word_list)
            
    return len(word)*max_num

print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],'abc'))
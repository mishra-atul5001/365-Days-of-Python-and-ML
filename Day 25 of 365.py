# -*- coding: utf-8 -*-
"""
Created on Tue May 18 10:19:54 2021

@author: Atul Mishra
"""

'''
Viral Advertising

HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those 5 people (i.e., floor(5/2) = 2 ) like the advertisement and each shares it with 3 of their friends. At the beginning of the second day,floor(5/2)*3 = 6 people receive the advertisement.

Each day, floor(reciepents/2) of the recipients like the advertisement and will share it with 3 friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.
'''

def viralAdvertising(n):
    customer = 5
    '''
    Seems very straight forward. Loop from 1 to N+1 and keep count of the liked customer and update the number of customers. Paralel to that keep on adding the liked customers, and there you go!
    '''
    # cum = []
    sum_num = 0
    for i in range(1,n+1):
        liked = customer//2
        # cum.append(liked)
        sum_num += liked
        customer = liked*3
    
    return sum_num

print('Total customers liking the adverstisement, are:',viralAdvertising(5))
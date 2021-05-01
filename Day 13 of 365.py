# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:59:20 2021

@author: Atul Mishra
"""

"""
 BILL DIVISION
 
wo friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6]. Anna declines to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2=3. If he includes the cost of bill[2], he will calculate (2+4+2)/2=6. In the second case, he should refund to 3 Anna.

Sample Input 0
4 1
3 10 2 9
12

Sample Output 0
5
------------------------------------------
Sample Input 1
4 1
3 10 2 9
7

Sample Output 1
Bon Appetit

"""

# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# k = int(first_multiple_input[1])
# bill = list(map(int, input().rstrip().split()))
# b = int(input().strip())

def bonAppetit(bill, k, b):
    
    '''
    Step 1: Ignore kth element which ANNA declined to pay and sum the sliced list!
    Step 2: Calculate the bill difference between total bill paid and sliced sum
    Step 3: Check if the difference bill is NUM, return the diff, else -> Bon Appetit
    '''
    bill_2 = (sum(bill[:k]) + sum(bill[k+1:]))// 2
    print('Total cost of the shared items is {}'.format(bill_2))
    diff_bill = b - bill_2
    print('Anna was overcharged by amount! {}'.format(diff_bill))
    if diff_bill == 0:
        print('Bon Appetit\n')
    else:
        print(diff_bill,'\n')

bill = [3,10,2,9]
k = 1
b = 12
bonAppetit(bill, k, b)

bill = [3,10,2,9]
k = 1
b = 7
bonAppetit(bill, k, b)
'''
CountDiv

Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
'''

def CountDiv(A,B,K):
    my_diff = B//K - A//K
    # This will gives us the count of numbers divisble between reange of (A,B] -> A is EXCLUDED and B is INCLUDED
    #  SO in order to include A
    if A%K == 0:
        my_diff +=1

    return my_diff 

print('Count of Numbers divisble in the range:',CountDiv(6,11,2))
print()
print('Count of Numbers divisble in the range:',CountDiv(5,12,2))
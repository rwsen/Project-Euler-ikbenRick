#PE004
# What is the largest palindromic product of two 3-digit integers?
from math import sqrt, floor

# predicate checking palindromicity by converting integer to list, reversing
def isPalindrome(number):
    list = [int(x) for x in str(number)]
    reversed = list.copy()
    reversed.reverse()

    if sum(map(diff,list,reversed)) == 0:
        return True
    else:
        return False


# function to determine the absolute difference between two numbers
def diff(a,b):
    return abs(a-b)


# find the largest palindromic product from two 3-digit numbers a and b
# search in order of increasing distance from highest possible 3-digit numbers
a = 999
b = 999
solution = 0 #

# generate distances
for distance in range(0, a*b):
    for i in range(0, distance+1):
        product = (a-i) * (b-(distance-i))
        if isPalindrome(product):
            if product > solution:
                solution = product
    if solution > 0:
        break

print(solution)
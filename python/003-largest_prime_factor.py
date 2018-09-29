#PE003
from math import sqrt, floor

def isPrime(x):
    # edge cases
    if x < 2:
        return False
    if x == 2:
        return True

    # sieve
    for i in range(3, floor(sqrt(x)), 2):
        if (x / i ) % 1 == 0:
            return False
    return True


# What is the largest prime factor of the given number?
number = 600851475143   # the number to be tested
limit = floor(sqrt(number))
solution = 1

# test edge case solution is 2
if (number / 2) % 1 == 0:
    solution = 2

# test candidate solutions
for candidate in range (3, limit, 2):
    if (number / candidate) % 1 == 0:
        if isPrime(candidate):
            solution = candidate

print(solution)

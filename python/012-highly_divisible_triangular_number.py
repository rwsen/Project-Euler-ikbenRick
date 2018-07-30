# Project Euler 12
import math

def factors(number):
    i = 1
    limit = math.ceil(math.sqrt(number))
    count = 0
    while i < limit:
        if number % i == 0:
            count = count + 2
        i += 1

    if math.sqrt(number) % 1 == 0:
        count += 1 

    return count

if __name__ == "__main__":
    number = 1
    triangle = number
    best = 1

    while True:
        number = number + 1
        triangle = triangle + number
        count = factors(triangle)
        if count > best:
            best = count
            print("triangle number %s has %s factors" % (triangle, count))
        if count > 500:
            break

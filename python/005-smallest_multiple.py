#PE005
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
solution = 0
highest_number = 20

while True:
    solution += 1
    for i in range (1,highest_number + 1):
        if not (solution / i) % 1 == 0:
            break
    else:
        # solution found
        print(solution)
        break

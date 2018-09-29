#PE002
evensum = 0     # cumulative result
prev1 = 1       # previous value n-1
prev2 = 1       # previous value n-2

while True:
    value = prev1 + prev2
    if not value < 4000000:
        break
    if not (value & 1):
        evensum += value
    prev2 = prev1
    prev1 = value

print(evensum)

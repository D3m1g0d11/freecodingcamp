#map, filter, reduce

numbers = [1, 2, 3]

double = lambda a : a * 2

mapRes = map(lambda a : a * 2, numbers)

result = map(double, numbers)

print(list(result))

#Filter

numbers = [1, 2, 3, 4, 5, 6]

def isEven(n):
    return n% 2 == 0

resultTwo = filter(lambda n : n % 2 == 0, numbers)

print(list(resultTwo))

#Reduce
from functools import reduce
expenses = [
    ('Dinner', 80),
    ('Car Repair', 120)
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)

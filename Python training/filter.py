from functools import reduce

lis = [1, 3, 5, 6, 2]


print(reduce(lambda a, b: a+b, lis))


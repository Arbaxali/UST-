from functools import reduce




list1 = [22,34,54,21,22,42,11,2,34,6667,8,89]


eve = list(filter(lambda a : a % 2 == 0, list1))

print(eve)

cub = list(map(lambda num : num*num*num , eve)) 
print(cub)

# suu = list(reduce(lambda a, b: a + b , cub))
# print(suu)


# Try to use lambda, Filter , Map & Reduce all in one Example. 
# Create a single line program that takes list -> list of even num -> take Cube (a^3) -> sum of all values
sum_all = reduce(lambda a, b : a + b, list(map(lambda num : num ** 3, list(filter(lambda num : num % 2 == 0, list1)))))
print(sum_all)

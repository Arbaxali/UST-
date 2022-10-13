from functools import reduce

list1 = [22,3,4,552,76,34,22,0,973,64,2,1]
maxx_list = reduce(lambda a,b : a if a > b else b, list1)
print(maxx_list)


minn_list = reduce(lambda a,b : a if a < b else b, list1)
print(minn_list)



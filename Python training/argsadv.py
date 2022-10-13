def myfunc(*args):
    return sum(args)



list1 =[1,2,3,4,5,6,7]
list2 = [78,89,70,76,544]
list3 = [54,2,3,14,144,908,4.5]
print(myfunc(*list1,*list2,*list3))
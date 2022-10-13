def maxmin(arr):
    lenn = len(arr) - 1
    sp = 0
    summ = 0
    for i in range(lenn):
        if sp != 0:
            summ = sum(arr)
            sp +=1
    print(summ)








arr = [1,2,3,4,5]

maxmin(arr)
from operator import le


def printDiagonal(lst):
     
    # To print Primary Diagonal
    # print('Diagonal 1 - ', end ="")
    # print(lst[0][1])
    # print(len(lst))
    # for i in range(len(lst)):
    #     print(lst[i][i])
    # # To print Secondary Diagonal
    s = len(lst)

    lst1 = [lst[i][i] for i in range(s)]
    lst2 = [lst[i][s-i-1] for i in range(s)]
    # print('Diagonal 2 - ', end ="")
    # print([lst[i][len(lst)-i-1] for i in range(len(lst))])
    diffe = abs(sum(lst1) - sum(lst2))
    
    print(diffe)
     
# Driver code
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printDiagonal(lst)
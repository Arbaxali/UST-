# def minmax(arr):
    # lenn = int(len(arr)-1)



#     # lst1=[arr[0],arr[1],arr[2],arr[3]]
#     # lst2=[arr[1],arr[2],arr[3],arr[4]]
#     # lst3=[arr[2],arr[3],arr[4],arr[0]]
#     # lst4=[arr[3],arr[4],arr[0],arr[1]]
#     # lst5=[arr[4],arr[0],arr[1],arr[2]]
#     print(lenn)
#     for i in lenn:
#         lst1 = [arr[i]]
#     print(lst1)    
#     # lst1 = sum(lst1)
#     # lst2 = sum(lst2)
#     # lst3 = sum(lst3)
#     # lst4 = sum(lst4)
#     # lst5 = sum(lst5)

#     # mai = [lst1,lst2,lst3,lst4,lst5]
#     # minn = min(mai)
#     # maxx = max(mai)
#     # print(maxx,minn)   



# ar = [1,2,3,4,5]
def minmax(ar):
    list1 = ar
    list2 = []
    sum1 = []
    lenn = len(ar)
    
    
    for x in list1:
        def numm(lenn):
            for y in reversed(range(lenn)):
                nu = y
                return nu   
        s = numm(lenn)        
        if x == s:
            continue
        list2.append(x)
        sum1 = sum(list2)
    list2 *= 0

    print(sum1)
    print(list2)
   
ar =[1,2,3,4,5]

minmax(ar)
# A= { 1,2,3,4,5,6,7}
# B = {6,7,8,9}
# print(A & B)
# print(A.intersection(B)) #INTERSECTION : COMMON IN BOTH



# A= { 1,2,3,4,5,6,7}
# B = {6,7,8,9}
# A - B
# print(A.difference(B)) #DIFFERENCE : ELEMENTS ONLY IN A NOT IN B



# print(B.difference(A)) # ONLY IN B NOT IN A



# #symmetric difference of sets
# A= { 1,2,3,4,5,6,7}
# B = {6,7,8,9}
# A ^ B
# print(A.symmetric_difference(B))



A = {1,2,3,4,5,6,7,8,9,10,11}
B = {4,5,6,7,8,9}
C = {20,30,40,60,50}

print(B.issubset(A))
print(A.issuperset(B))
print(C.isdisjoint(A))
print(B.isdisjoint(A))
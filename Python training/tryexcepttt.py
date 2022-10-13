import os
import sys

# key error
try:
    my_dict ={ 'id': 102, 'name':'suresh', 'city': 'bangalore', 'dept': 'it'}
    # print(my_dict(salary))  #error
    print(my_dict(id))
except TypeError:
    print("type error not callable")    
except KeyError:
    print('Key error exception raised')

# index error

try: 
    my_list = [1,2,3,4,5,6]
    print(my_list[10])
except IndexError :
    print("index error raised")

# type error

try: 
    a =50
    b = "python"
    c =a/b
except TypeError:
    print("type error exception raised")


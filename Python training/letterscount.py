# def countt(s):
#     res = {}
#     for letter in s:
#         if letter.isalpha():
#             if letter.lower() in res.keys():
#                 res[letter.lower()] += 1
#             else:
#                 res[letter.lower()] = 1
#         elif letter.isdigit():
#             if letter in res.keys():
#                 res[letter] +=1
#             else:
#                 res[letter] = 1   

#     return(res)

# s = input("enter the string ")
# print(countt(s))    





text = input("enter the string")
dict1 = {'letters': 0 , 'digits':0}

for char in text:
    if char.isalpha():
        dict1['letters'] +=1
    elif char.isdigit():
        dict1['digits']  +=1
    else:
        pass

print("letters", dict1['letters'])
print("digits", dict1['digits'])

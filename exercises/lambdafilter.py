mylist = ['php', 'madam','python','numpy','class','rewire','salas']

# def palindrome(mylist):
#     palindromed_list =[]
#     for i in mylist:
#         temp = i
#         temp1 = temp[::-1]

#         if temp == temp1:
#             palindromed_list.append(temp1)
#     return palindromed_list        



# lambda does not require for loop we can iterate through evry elements in the list

palindrome =list(filter(lambda word : word== word[::-1] ,mylist))
print(palindrome)
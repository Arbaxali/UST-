temp1 = input("enter the string ").lower()

temp2 =temp1[-1::-1]


if temp1 == temp2:
    print("given string is palindrome",temp2)
else:
    print("it is not a palindrome",temp2)    



#1465
num =int(input("Please enter the number "))
rev_num = 0
while num > 0:
    num1 = num % 10 
    rev_num = rev_num + num1
    num = num//10
print("rev numer",rev_num)    
import os
import sys

try:
    x =int(input("Enter the first number : "))
    y =int(input("Ente the second number: "))
    print(x/y)
    os.remove(r"C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\test2.txt")

except NameError:
    print('Name error exception occured')
except FileNotFoundError:
    print('file not found error') 
       
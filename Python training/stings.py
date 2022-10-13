


str1_demo = "Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"

strr = str1_demo.lower()
# print(strr)
vowels = 0
constant = 0 
for i in strr:
    if i == "a" or i == "e" or i == "o" or i =="i" or i == "u":
        vowels = vowels + 1
    else :
        if i!=' ' and i.isdigit() == False and i!="," and i!='.':
            constant = constant +1 

print("number of vowels",vowels)        
print("number of consonants", constant)

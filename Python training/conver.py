num  = int(input("enter the number "))
conv = input("select C or F ").lower()


if conv == "c":
    cel =(num*9/5)+32
    print("{0} f".format(cel))
else :
    f = (num-32)*5/9
    print("{0} c".format(f))
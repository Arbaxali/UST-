
m = input("Enter the number ")
m = int(m)
for j in range(2, m):
    if m % j == 0:
        print("not a prime nummber")
        break
else:
    print("prime number")
            
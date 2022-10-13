from itertools import count


file = open(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\twinkle.txt')
count =0
text = file.read()
if "star" in text:
    count +=1
    print("star is present",count)
else:
    print("star is not present")    
import sys
try:
    print(100/0)
except:
    print("exception occured")
else:
     print(sys.exc_info()[1],"No exception occured")    
finally:
    print("run this block of code")     
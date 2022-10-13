import sys
try:
    x =int(input('enter the first '))
    if x >50:
        raise ValueError(x)
except:
    print(sys.exc_info()[0])        
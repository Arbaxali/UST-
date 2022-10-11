def userdetails(licenseNo, *args, contact=0, **kwargs):
    print('License No. : ',licenseNo)
    j = ''
    for i in args:
        j = j + i
        print('Full name : ',j)
        print('phone Number : ',contact)
    
    for key, val in kwargs.items():
        print("{} : {}".format(key,val))
    
name = ['Haroon','Baig']
mydict ={'Name' : 'Haroon', 'ID': 191569, 'Pincode':110001, 'Age':26, "Country":'India'}
userdetails('DLT2022', *name, contact = 9845448747, **mydict)
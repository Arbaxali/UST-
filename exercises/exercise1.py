from subprocess import list2cmdline


python_libs = ['python','math','numpy','pandas','datetime','sys']
upper_python_libs = []


# for i in python_libs:
#     upper_python_libs.append(i.upper())

# # upper_python_libs.append(python_libs)
# print(upper_python_libs)



upper_python_libs = list(map(lambda num :num.upper()  , python_libs ))

print(upper_python_libs)
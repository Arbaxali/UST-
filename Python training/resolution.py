import pywin32_system32

 

i=0

res=set()

try:

    while True:

        ds=pywin32_system32.EnumDisplaySettings(None,i)

        res.add(f"{ds.PelsWidth}x{ds.PelsHeight}")

        i+=1

except:pass

 

print(res)
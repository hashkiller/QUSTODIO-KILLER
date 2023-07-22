import os
import time

os.system('net stop qengine')
os.system('net stop qupdate')

print('------------------------------- \n Qustudio was killed (use this program everytime your computer is up)')
time.sleep(5)
print('exit...')
os.system("exit")
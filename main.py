import os
import time

os.system('net stop qengine')
os.system('net stop qupdate')

print('------------------------------- \n Qustudio was killed (qustudio was killer only for this session)')
time.sleep(5)
print('exit...')
os.system("exit")

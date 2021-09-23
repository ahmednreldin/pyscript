# Modify in Repo and clone  

import os

print("Remove Repo if exist ")
os.system('rm -r c') 

print("clone localization repo ")
os.system('!git clone https://github.com/ahmednreldin/crossview_localisation c')

print(' Move modified file " ) 
os.system('!mv c/src/CVM-Net/test_model.py  crossview_localisation/src/CVM-Net/test_model.py')

print('test model')
os.system('python  crossview_localisation/src/CVM-Net/test_model.py')

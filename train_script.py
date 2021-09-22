
import os

# Run train script 
print('Run train script ' )

# install slim package 
print('install slim package ')
os.system('pip install --upgrade tf_slim')

print("Run train.py")

os.system('python /kaggle/working/crossview_localisation/src/CVM-Net/train.py')

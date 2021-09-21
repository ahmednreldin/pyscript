
import os

# Run Tran.py
print("install TF 1.13.2")
os.system('pip install tensorflow==1.13.2') # install suitable version for TF
import tensorflow as tf

print("Run train.py")

!python /kaggle/working/crossview_localisation/src/CVM-Net/train.py

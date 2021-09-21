
import os

# Run Tran.py
os.system('pip install tensorflow==1.13.2') # install suitable version for TF
import tensorflow as tf
os.system('python /kaggle/working/crossview_localisation/src/CVM-Net/train.py' )

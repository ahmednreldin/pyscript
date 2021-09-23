import os

# Run test script 
print('Run test script ' )


print('Copy Pre-trained model to location ')
os.system('mv /kaggle/CVM-Net_model/CVM-NET-I/CVM-Net-I_model/* /kaggle/working/crossview_localisation/src/Model/CVM-NET-I/test_model/')


# install slim package 
print('install slim package ')
os.system('pip install --upgrade tf_slim')

print("Run test_model.py")
os.system('python /kaggle/working/crossview_localisation/src/CVM-Net/test_model.py')

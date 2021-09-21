
import os

root_path = '/kaggle' 
working_path = '/kaggle/working'

print( "Change directory to /kaggle")
os.chdir(root_path)

print( "install gdown package") 
os.system('conda install -y gdown') 

os.system('gdown --id  1JtXz4q0kONNoEFE9tEfSCxLRuuJUWqIF # CVM-NET Model') 
os.system('unzip CVM-Net_model.zip')

os.chdir(working_path)

os.system('git clone https://github.com/ahmednreldin/crossview_localisation # clone repo')
os.system('mv '/kaggle/CVM-Net_model/CVM-NET-I/CVM-Net-I_init/' '/kaggle/working/crossview_localisation/src/Model/CVM-NET-I'')
#rename model init to 0 
os.system('mv /kaggle/crossview_localisation/src/Model/CVM-NET-I/CVM-Net-I_init /kaggle/crossview_localisation/src/Model/CVM-NET-I/0')
os.system('cp -r  /kaggle/input/cvusa-localization /kaggle/working')

# Modify Data 
os.system('mv /kaggle/working/cvusa-localization/splits/splits/* /kaggle/working/cvusa-localization/splits/')
os.system('mv /kaggle/working/cvusa-localization/bingmap/bingmap/* /kaggle/working/cvusa-localization/bingmap/')
os.system('mv /kaggle/working/cvusa-localization/split_locations/* /kaggle/working/cvusa-localization/')
os.system('mv /kaggle/working/cvusa-localization/streetview/streetview/* /kaggle/working/cvusa-localization/streetview/')


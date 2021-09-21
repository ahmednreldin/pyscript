
import os

root_path = '/kaggle' 
working_path = '/kaggle/working'

!echo "Change directory to /kaggle"
os.chdir(root_path)

!echo "install gdown package" 
! conda install -y gdown ; 

!gdown --id  1JtXz4q0kONNoEFE9tEfSCxLRuuJUWqIF # CVM-NET Model ; 
!unzip CVM-Net_model.zip

os.chdir(working_path)

!git clone https://github.com/ahmednreldin/crossview_localisation # clone repo
!mv '/kaggle/CVM-Net_model/CVM-NET-I/CVM-Net-I_init/' '/kaggle/working/crossview_localisation/src/Model/CVM-NET-I'
#rename model init to 0 
!mv /kaggle/crossview_localisation/src/Model/CVM-NET-I/CVM-Net-I_init /kaggle/crossview_localisation/src/Model/CVM-NET-I/0
!cp -r  /kaggle/input/cvusa-localization /kaggle/working

# Modify Data 
!mv /kaggle/working/cvusa-localization/splits/splits/* /kaggle/working/cvusa-localization/splits/
!mv /kaggle/working/cvusa-localization/bingmap/bingmap/* /kaggle/working/cvusa-localization/bingmap/
!mv /kaggle/working/cvusa-localization/split_locations/* /kaggle/working/cvusa-localization/
!mv /kaggle/working/cvusa-localization/streetview/streetview/* /kaggle/working/cvusa-localization/streetview/


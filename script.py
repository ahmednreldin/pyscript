cd .. ;
! conda install -y gdown ; 
!gdown --id  1JtXz4q0kONNoEFE9tEfSCxLRuuJUWqIF # CVM-NET Model ; 
!unzip CVM-Net_model.zip
cd /kaggle/working
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





## Kagle 
# Donwload from Drive # first enable internet from right sidebar 
# install package to download from drive 
! conda install -y gdown

# Donwload datasets from drive 
!gdown --id  1Sz_D9WKck5hNOpdtIyzx0DkS_loRj5pT # streetView
!gdown --id  1SxqE3BuKGC-T5APARyQIVOI99nqpo5Y6 # split
!gdown --id  1YDzjWNzbF3d4FTyTg9m94nlYaafeJK-3 # split localization 
!gdown --id  1T63r8qQ95IOQEEhOkcZJUuEePpiJKt6U # bingmap
!gdown --id  1JtXz4q0kONNoEFE9tEfSCxLRuuJUWqIF # CVM-NET Model




# extract 
!tar -xvf 'bingmap.tar.gz' 
!tar -xvf 'streetview.tar.gz' 
!tar -xvf 'splits.tar.gz'
!unzip 'split_locations.zip' 
!unzip 'CVM-Net_model.zip'

# then remove for spaces
!rm ./bingmap.tar.gz
!rm ./streetview.tar.gz
!rm ./split_locations.zip
!rm ./splits.tar.zip


!git clone https://github.com/ahmednreldin/crossview_localisation # clone repo

Move model to repo
mv '/kaggle/working/CVM-Net_model/CVM-NET-I/CVM-Net-I_init/' '/kaggle/working/crossview_localisation/src/Model/CVM-NET-I'

ls /kaggle/working/crossview_localisation/src

# Run Tran.py
pip install tensorflow==1.13.2 # install suitable version for TF
import tensorflow as tf
!python '/kaggle/working/crossview_localisation/src/CVM-Net/train.py'


mv /kaggle/input/cvusa-localization/splits/splits/* /kaggle/input/cvusa-localization/splits/

# Dateset 
# copy dataset to working flow 
!cp -r  /kaggle/input/cvusa-localization /kaggle/working

# Modify Data 
!mv /kaggle/working/cvusa-localization/splits/splits/* /kaggle/working/cvusa-localization/splits/
!mv /kaggle/working/cvusa-localization/bingmap/bingmap/* /kaggle/working/cvusa-localization/bingmap/
!mv /kaggle/working/cvusa-localization/split_locations/* /kaggle/working/cvusa-localization/
!mv /kaggle/working/cvusa-localization/streetview/streetview/* /kaggle/working/cvusa-localization/streetview/

#download specific file 
!wget https://github.com/ahmednreldin/crossview_localisation/blob/master/src/CVM-Net/train.py 



# Model & Repo
cd /kaggle # this make you use more space 
!gdown --id  1JtXz4q0kONNoEFE9tEfSCxLRuuJUWqIF # CVM-NET Model
!unzip CVM-Net_model.zip
cd /kaggle/working
!git clone https://github.com/ahmednreldin/crossview_localisation # clone repo
mv '/kaggle/CVM-Net_model/CVM-NET-I/CVM-Net-I_init/' '/kaggle/working/crossview_localisation/src/Model/CVM-NET-I'
#rename model init to 0 
!mv /kaggle/crossview_localisation/src/Model/CVM-NET-I/CVM-Net-I_init /kaggle/crossview_localisation/src/Model/CVM-NET-I/0


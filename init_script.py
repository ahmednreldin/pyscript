
import os

root_path = '/kaggle' 
working_path = '/kaggle/working'

print( "Change directory to /kaggle")
os.chdir(root_path)

print( "install gdown package") 
os.system('conda install -y gdown') 
print("Download CVM-NET Model")
os.system('gdown --id  1JtXz4q0kONNoEFE9tEfSCxLRuuJUWqIF # CVM-NET Model') 
os.system('unzip CVM-Net_model.zip')

print(f"change directory to {working_path}")
os.chdir(working_path)
print("Clone Cross-View Repo")
os.system('git clone https://github.com/ahmednreldin/crossview_localisation # clone repo')

print("Copy Init CVM-NET I Model to location")
os.system('mv /kaggle/CVM-Net_model/CVM-NET-I/CVM-Net-I_init/ /kaggle/working/crossview_localisation/src/Model/CVM-NET-I')
#rename model init to 0 
os.system('mv /kaggle/working/crossview_localisation/src/Model/CVM-NET-I/CVM-Net-I_init /kaggle/working/crossview_localisation/src/Model/CVM-NET-I/0')

print('Copy Pre-trained CVM-NET I model to location ')
os.system('mv /kaggle/CVM-Net_model/CVM-NET-I/CVM-Net-I_model/* /kaggle/working/crossview_localisation/src/Model/CVM-NET-I/test_model/')



#print("Copy Init CVM-NET II Model to location")
#os.system('mv /kaggle/CVM-Net_model/CVM-NET-II/CVM-Net-II_init/ /kaggle/working/crossview_localisation/src/Model/CVM-NET-II')
#rename model init to 0 
#os.system('mv /kaggle/working/crossview_localisation/src/Model/CVM-NET-II/CVM-Net-II_init /kaggle/working/crossview_localisation/src/Model/CVM-NET-II/0')
#print('Copy Pre-trained CVM-NET II model to location ')
#os.system('mv /kaggle/CVM-Net_model/CVM-NET-II/CVM-Net-II_model/* /kaggle/working/crossview_localisation/src/Model/CVM-NET-II/test_model/')

# Datasets
print("Copy dataset from input to working directory..")
os.system('cp -r  /kaggle/input/cvusa-localization /kaggle/working')

print("Chagne Directories for Datasets")
os.system('mv /kaggle/working/cvusa-localization/splits/splits/* /kaggle/working/cvusa-localization/splits/')
os.system('mv /kaggle/working/cvusa-localization/bingmap/bingmap/* /kaggle/working/cvusa-localization/bingmap/')
os.system('mv /kaggle/working/cvusa-localization/split_locations/* /kaggle/working/cvusa-localization/')
os.system('mv /kaggle/working/cvusa-localization/streetview/streetview/* /kaggle/working/cvusa-localization/streetview/')

print("Install Necessary Packages " )

print('install slim package ')
os.system('pip install --upgrade tf_slim') 




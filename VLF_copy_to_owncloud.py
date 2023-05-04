#
# BEFORE EXECUTE
#
#  conda pip install git pip
#  !git clone https://github.com/hpc-fci-mackenzie/pyocclient # updated pyocclient for owncloud mackenzie
#  cd C:/users/user/pyocclient
#  !pip install -e .
#

import os
import shutil
import pandas as pd
import owncloud

# Define the source directory where the files are located
source_dir = r'C:/Users/User/Documents/meusite/VLF/data'

# Define the destination directory where the files will be copied to
public_link = 'https://mackcloud.mackenzie.br/owncloud/index.php/s/m8W0728JBLszMm7' # pasta xyz pública e sem senha, vc pode acessar pelo Browser se quiser

step = 100 # save and print step to recovery

try:
  oc = owncloud.Client(url='https://mackcloud.mackenzie.br/owncloud/')
  oc.anon_login('m8W0728JBLszMm7')
  print('Successfully login at owncloud')
except Exception as e:
  print('Login at owncloud failed')
  print(str(e))

nr_files = 0

try:
    df_control = pd.read_csv(source_dir + r'\df_control.csv')
except:
    df_control = pd.DataFrame({'copied':[],'path':[], 'error':[]})

# Loop through all files and folders in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        
        if file.split('.')[1] != 'mat' and file != 'df_control.csv':
            break

        if nr_files%1 == step and nr_files!=0:
            print('All files read: ', nr_files)
            df_control.to_csv(source_dir + r'\df_control.csv',index=None)    
        
        # Construct the full path of the file
        src_path = os.path.join(root, file)
   
        try:
          oc.drop_file(os.path.join(src_path))
          # print('Upload Successfully Executed')
          df_control.at[file,['copied','path','error']] = True, os.path.join(src_path), None        
        except Exception as e:
          df_control.at[file,['copied','path','error']] = False, os.path.join(src_path), str(e)      

        nr_files += 1
 
df = df_control[ df_control.copied == False ]

if len(df) > 0:    
    print('Starting... ', len(df), ' recovery failed copies')    

    for i, row in df.iterrows():
        for attempt_number in range(3):
            try:
              oc.drop_file(row.path)
              df_control.at[i,'copied','error'] = True, None
              break
            except:
              None      

 
    
     
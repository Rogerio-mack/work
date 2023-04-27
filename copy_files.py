# -*- coding: utf-8 -*-
import os
import shutil
import pandas as pd

# Define the source directory where the files are located
source_dir = r'C:\VLF'

# Define the destination directory where the files will be copied to
dest_dir = r'C:\VLF_flat'

nr_files = 0
nr_files_mat = 0

try:
    df_control = pd.read_csv(source_dir + r'\df_control.csv')
except:
    df_control = pd.DataFrame({'ok':[]})

# Loop through all files and folders in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        
        if nr_files%10000 == 0 and nr_files!=0:
            print('All files read: ', nr_files)
            print('All files copied: ', nr_files_mat)
            
            df_control.to_csv(source_dir + r'\df_control.csv',index=None)    

        
        nr_files += 1
        
        if file.endswith('.mat'):
            try:
                break                
            except:

                df_control.at[file] = 1        
    
                nr_files_mat += 1
                # Construct the full path of the file
                src_path = os.path.join(root, file)
                
                # Construct the full path of the destination file
                dest_path = os.path.join(dest_dir, file)
                
                # Copy the file to the destination directory
                try:
                    shutil.copy2(src_path, dest_path)
                except Exception as e:
                    print(src_path, dest_path)
                    print(e)
    

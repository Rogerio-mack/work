# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:22:50 2023

@author: 1115665
"""
import os
# import shutil
import pandas as pd

source_dir = r'C:\VLF'
dest_dir = r'C:\VLF_flat'

try:
    df_control = pd.read_csv(source_dir + r'\df_control.csv')
except:
    df_control = pd.DataFrame({'ok':[]})

nr_files = 0

# Loop through all files and folders in the source directory
for root, dirs, files in os.walk(dest_dir):
    for file in files:
        df_control.at[file] = 1 
         
        nr_files += 1     
        if nr_files%10000 == 0:
            print('All files read: ', nr_files)
            
            df_control.to_csv(source_dir + r'\df_control.csv',index=None)    

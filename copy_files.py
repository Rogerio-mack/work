import os
import shutil

# Define the source directory where the files are located
source_dir = r'C:\path\to\source\directory'

# Define the destination directory where the files will be copied to
dest_dir = r'C:\path\to\destination\directory'

# Loop through all files and folders in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.mat'):
            # Construct the full path of the file
            src_path = os.path.join(root, file)
            
            # Construct the full path of the destination file
            dest_path = os.path.join(dest_dir, file)
            
            # Copy the file to the destination directory
            shutil.copy2(src_path, dest_path)

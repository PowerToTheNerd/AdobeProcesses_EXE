import os
import sys
import shutil

old_extension = '.exeZ'
new_extension = '.exe'
backup_dir = 'backup files'  

specific_files = [
    "C:\Program Files (x86)\Adobe\Adobe Sync\CoreSync\CoreSync.exe",
    "C:\Program Files\Adobe\Adobe Creative Cloud Experience\CCXProcess.exe",
    "C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\ADS\Adobe Desktop Service.exe",
    "C:\Program Files\Common Files\Adobe\Creative Cloud Libraries\CCLibrary.exe",
    "C:\Program Files\Adobe\Adobe Photoshop 2023\LogTransport2.exe",
]

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
backup_path = os.path.join(script_dir, backup_dir)

if not os.path.exists(backup_path):
    os.makedirs(backup_path)

for specific_file in specific_files:
    if os.path.exists(specific_file):
        dir_path, filename = os.path.split(specific_file)
        new_filename = os.path.splitext(filename)[0] + new_extension
        new_file_path = os.path.join(dir_path, new_filename)
        
        backup_file_path = os.path.join(backup_path, filename)
        shutil.copy(specific_file, backup_file_path)
        
        os.rename(specific_file, new_file_path)
        print(f'Renamed: {specific_file} -> {new_file_path}')
    else:
        print(f'File not found: {specific_file}')
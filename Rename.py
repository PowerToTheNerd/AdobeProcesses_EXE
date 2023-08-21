import os

old_extension = '.exe'
new_extension = '.exeZ'

specific_files = [
    "C:\Program Files (x86)\Adobe\Adobe Sync\CoreSync\CoreSync.exe",
    "C:\Program Files\Adobe\Adobe Creative Cloud Experience\CCXProcess.exe",
    "C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\ADS\Adobe Desktop Service.exe",
    "C:\Program Files\Common Files\Adobe\Creative Cloud Libraries\CCLibrary.exe",
    "C:\Program Files\Adobe\Adobe Photoshop 2021\LogTransport2.exe"\
]

for specific_file in specific_files:
    if os.path.exists(specific_file):
        dir_path, filename = os.path.split(specific_file)
        new_filename = os.path.splitext(filename)[0] + new_extension
        new_file_path = os.path.join(dir_path, new_filename)
        os.rename(specific_file, new_file_path)
        print(f'Renamed: {specific_file} -> {new_file_path}')
    else:
        print(f'File not found: {specific_file}')
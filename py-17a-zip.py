from zipfile import ZipFile
import os
from os.path import basename


with ZipFile('zip_create.zip', 'w') as zip_file_handle:
    for dir_name, sub_dir, file_names in os.walk('./extracted'):
        for file_name in file_names:
            path = os.path.join(dir_name, file_name)
            zip_file_handle.write(path, basename(path))

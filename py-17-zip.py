import zipfile
import os

file_path = os.path.join('.', 'Archive.zip')
extract_path = os.path.join('.', 'extracted')

with zipfile.ZipFile(file_path) as file_handle:
    for file_info in file_handle.filelist:
        print(f'{file_info.filename} -> {file_info.file_size} -> {file_info.date_time}')
    print('~'*50)

    file_handle.extractall(extract_path)
    print('Completed!')


# Also possible for individual file adding
# with zipfile.ZipFile('sample2.zip', 'w') as zip_handle_2:
#    zip_handle_2.write('filename.text')

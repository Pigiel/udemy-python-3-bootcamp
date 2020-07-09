#/usr/bin/env python3
import os
import re
import shutil

telephone_numbers = []

def search(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    
    with open(file, 'r') as f:
        text = f.read()
        # return re.search(pattern, text) or ''
        if re.search(pattern, text):
            return re.search(pattern, text).group(0)
        else:
            return ''

if __name__ == "__main__":
    print('Extracting file:\tunzip_me_for_instructions.zip\n')
    shutil.unpack_archive('unzip_me_for_instructions.zip','temp', 'zip')

    # Printing Instructions file
    with open('temp/extracted_content/Instructions.txt', 'r') as f:
        print('#' * 128)
        print(f.read())
        print('#' * 128)

    print('\nSearching files for pattern\n')

    for folder, sub_folder, files in os.walk(os.getcwd() + '/temp'):
        for file in files:
            full_path = folder + '/' + file
            print(full_path)
            telephone_numbers.append(search(full_path))

    print('\nSearch results\n')
    print(telephone_numbers)

    print('\nDeleting extracted files from temp folder')
    shutil.rmtree('temp')
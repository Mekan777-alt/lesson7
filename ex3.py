from shutil import copy, SameFileError
from os import walk, mkdir
from os.path import join, exists

dir = r'.\my_project'
new_dir_path = join(dir, 'templates')
if not exists(new_dir_path):
    mkdir(new_dir_path)
for directory, dirs, files in walk(dir):
    for file in files:
        if ".txt" in file:
            file_path = join(new_dir_path, directory.split("\\")[0])
            if not exists(file_path):
                mkdir(file_path)
            try:
                copy(join(directory, file), file_path)
            except SameFileError:
                break
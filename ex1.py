import os

my_project_folder = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in folders:
    os.makedirs(os.path.join(my_project_folder, folder))


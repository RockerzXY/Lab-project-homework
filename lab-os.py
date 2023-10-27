# Лаб. 15. Задание 1.
import os
from pathlib import Path

root_folder = Path('files/lab-os/')
os.makedirs(root_folder, exist_ok=True)

# Create subdirectories
subdirs = ['switches', 'routers', 'cisco']
doublesubdirs = ['cisco, huawei', 'juniper, huawei', 'cisco, meraki']

for i in range(len(doublesubdirs)):
    subdirs_list = doublesubdirs[i].split(', ')
    for dir in subdirs_list:
        dir_path = Path(root_folder, subdirs[i], 'other', dir)
        os.makedirs(dir_path, exist_ok=True)

os.rename(Path(root_folder, 'routers', 'other', 'juniper'), Path(root_folder, 'routers', 'other', 'nokia'))
with open(Path(root_folder, 'cisco', 'other', 'readme.txt'), 'w') as f:
    f.write("Don't forget to save all configurations!")
os.replace(Path(root_folder, 'cisco', 'other', 'readme.txt'), Path(root_folder, 'cisco', 'other', 'meraki', 'readme1.txt'))

with open(Path(root_folder, 'cisco', 'other', 'meraki', 'readme1.txt'), 'r') as f:
    data = f.read()
print(data)

dir_path = Path(root_folder, 'switches', 'other', 'junipers')
os.makedirs(dir_path, exist_ok=True)

for dirpath, dirnames, filenames in os.walk(root_folder):
    for dirname in dirnames:
        print('Каталог:', os.path.join(dirpath, dirname))
    for filename in filenames:
        print('Файл:', os.path.join(dirpath, filename))


dir_path = Path(root_folder, 'routers', 'other', 'nokia')
os.rmdir(dir_path)

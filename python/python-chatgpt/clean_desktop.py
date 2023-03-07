import os
import shutil

source = os.path.join(os.path.expanduser('~'), 'Desktop')
destination = os.path.join(os.path.expanduser('~'), 'png-desktop')

if not os.path.exists(destination):
    os.makedirs(destination)

for file in os.listdir(source):
    if file.endswith('.png'):
        shutil.move(os.path.join(source, file), destination)

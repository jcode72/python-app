import os
import shutil
from datetime import datetime, timedelta

downloads_folder = os.path.expanduser("~/Downloads")
to_delete_folder = os.path.expanduser("~/to_delete")

if not os.path.exists(to_delete_folder):
    os.mkdir(to_delete_folder)

threshold_date = datetime.now() - timedelta(days=30)

for file in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file)
    if os.path.isfile(file_path):
        file_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_date < threshold_date:
            shutil.move(file_path, to_delete_folder)

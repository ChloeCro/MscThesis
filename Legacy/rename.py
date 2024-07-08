import os
import re

folder_path = 'Results/Sectioned'

for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)

    if os.path.isdir(full_path):
        continue

    name, ext = os.path.splitext(filename)

    renamed = re.sub(r'\s+', '_', name)

    new_name = f"{renamed}{ext}"

    new_full = os.path.join(folder_path, new_name)

    os.rename(full_path, new_full)
    print(f"renamed: {filename} to {new_full}")
    
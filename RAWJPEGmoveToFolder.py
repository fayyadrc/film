import os
import shutil



source_folder = "/Volumes/CANONG7X/DCIM/181___10" #camera mounted path
destination_folder = '/Users/fayyadrc/Pictures/"new_folder_name"' 

file_numbers = [
8205,
8207,
8225,
8227,
8229,
8233,
8237,
]


os.makedirs(destination_folder, exist_ok=True)

# create a subfolder in the destination matching the source folder's basename
source_basename = os.path.basename(source_folder.rstrip('/'))
dest_subfolder = os.path.join(destination_folder, source_basename)
os.makedirs(dest_subfolder, exist_ok=True)

for number in file_numbers:
    for ext in ['.JPG', '.CR2']:
        filename = f"IMG_{number}{ext}"
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(dest_subfolder, filename)
        if os.path.exists(src_path):
            try:
                shutil.copy2(src_path, dst_path)
                print(f"Copied: {filename} -> {dest_subfolder}")
            except Exception as e:
                print(f"Failed to copy {filename}: {e}")
        else:
            print(f"Missing: {filename}")

print(f"Successfully copied files from '{source_folder}' to '{dest_subfolder}'")

import os
import shutil
from tqdm import tqdm

def mount_device(device, mount_point):
    os.system(f"sudo mount {device} {mount_point}")

def unmount_device(mount_point):
    os.system(f"sudo umount {mount_point}")

def copy_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for file in tqdm(files, desc="Copying files", unit="file"):
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)

            # Check if the file already exists in the destination folder
            if not os.path.exists(destination_path):
                shutil.copy2(source_path, destination_folder)

if __name__ == "__main__":
    source_device = "/dev/sda"
    mount_point = "/mnt/dash"
    destination_folder = "~/yaris-obd/dash/videos"

    try:
        # Mount the device
        mount_device(source_device, mount_point)

        # Copy files from source to destination
        copy_files(os.path.join(mount_point, "DCIM"), os.path.expanduser(destination_folder))

    finally:
        # Unmount the device (even if an exception occurs)
        unmount_device(mount_point)
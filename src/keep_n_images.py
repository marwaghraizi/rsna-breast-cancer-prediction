import os
import random
import sys

# Directory containing all the images
random.seed(9)
source_directory = sys.argv[1]
n = int(sys.argv[2])

# List all files in the source directory
all_files = os.listdir(source_directory)

# Check if there are more than 1158 images
if len(all_files) <= n:
    print(f"There are {n} or fewer images in the directory. No files will be deleted.")
else:
    # Randomly shuffle the list of files
    random.shuffle(all_files)

    # Select the first 1158 images to keep
    images_to_keep = all_files[:n]

    # Delete the remaining images
    for image in all_files:
        if image not in images_to_keep:
            file_path = os.path.join(source_directory, image)
            os.remove(file_path)

    print(f"{n} images have been selected and the rest have been deleted.")

import os
import shutil
import sys

# Base directory where "healthy" and "cancerous" directories are located
base_directory = sys.argv[1]
destination_directory = sys.argv[2]

# Define the target directory structure
target_structure = ["train", "test"]

# Loop through the target structure
for dataset_type in target_structure:
    dataset_directory = os.path.join(destination_directory, dataset_type)

    # Loop through the categories ("healthy" and "cancerous")
    for category in ["healthy", "cancerous"]:
        original_category_directory = os.path.join(base_directory, category)
        original_dataset_directory = os.path.join(original_category_directory, dataset_type)

        target_category_directory = os.path.join(dataset_directory, category)

        # Create the target category directory if it doesn't exist
        if not os.path.exists(target_category_directory):
            os.makedirs(target_category_directory)

        # Move the files from the original dataset directory to the target category directory
        files = os.listdir(original_dataset_directory)
        for file in files:
            source_path = os.path.join(original_dataset_directory, file)
            destination_path = os.path.join(target_category_directory, file)
            shutil.move(source_path, destination_path)

print("Directory structure reorganized.")

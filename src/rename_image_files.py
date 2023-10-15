import sys
import os
import shutil


def remove_patient_id(input_directory, destination_directory):
    all_files = os.listdir(input_directory)
    os.makedirs(destination_directory,  exist_ok=True)

    # Iterate through the files and remove the prefix
    for file_name in all_files:
        if "_" in file_name:
            new_file_name = file_name.split("_", 1)[1]  # Split at the first "_" and keep the rest
            source_path = os.path.join(input_directory, file_name)
            destination_path = os.path.join(destination_directory, new_file_name)
            shutil.copyfile(source_path, destination_path)

    print(f"Files copied to '{destination_directory}' with prefixes removed.")



input_directory = sys.argv[1]
destination_directory = sys.argv[2]
remove_patient_id(input_directory, destination_directory)
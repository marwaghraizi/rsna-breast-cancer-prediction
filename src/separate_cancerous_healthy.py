import sys
import pandas as pd
import os
import shutil


# Input DataFrame with "ID" and "Label" columns
train_data_path = "../data/train.csv"
train_metadata = pd.read_csv(train_data_path)

# Input directory containing image files
input_directory = sys.argv[1]

# Output directories for sorting images
output_directory_0 = sys.argv[2]
#"../data/labeled_data/healthy"
output_directory_1 = sys.argv[3]
#"../data/labeled_data/cancerous"

# Create output directories if they don't exist
os.makedirs(output_directory_0, exist_ok=True)
os.makedirs(output_directory_1, exist_ok=True)

# Iterate through the DataFrame and move images to the corresponding directories
for index, row in train_metadata.iterrows():
    image_id = row["image_id"]
    label = row["cancer"]
    source_path = os.path.join(input_directory, str(image_id) +".png")

    if label == 0:
        destination_path = os.path.join(output_directory_0, str(image_id)+".png")
    elif label == 1:
        destination_path = os.path.join(output_directory_1, str(image_id)+".png")
    else:
        print(f"Invalid label for image {image_id}: {label}")
        continue

    try:
        shutil.move(source_path, destination_path)
        print(f"Moved {image_id} to Directory {label}")
    except FileNotFoundError:
        print(f"File {image_id} not found in the input directory.")

print("Images sorted into directories based on their labels.")

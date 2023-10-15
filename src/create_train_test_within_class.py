import os
import sys
import random
import shutil

# Specify the paths to your original directories
original_cancerous_directory = sys.argv[2]
original_healthy_directory = sys.argv[1]

# Define the ratio of train to test (5:1)
train_ratio = 5
test_ratio = 1

# Function to move files from source to destination
def move_files(source, destination, file_list):
    os.makedirs(destination, exist_ok=True)
    for filename in file_list:
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination, filename)
        shutil.move(source_path, destination_path)

# Create train and test directories within the cancerous directory
train_cancerous_directory = os.path.join(original_cancerous_directory, 'train')
test_cancerous_directory = os.path.join(original_cancerous_directory, 'test')

# Create train and test directories within the healthy directory
train_healthy_directory = os.path.join(original_healthy_directory, 'train')
test_healthy_directory = os.path.join(original_healthy_directory, 'test')

# List all image files in the original cancerous directory
cancerous_images = [f for f in os.listdir(original_cancerous_directory) if os.path.isfile(os.path.join(original_cancerous_directory, f))]
random.shuffle(cancerous_images)

# Calculate the number of images for train and test
total_cancerous_images = len(cancerous_images)
print(len(cancerous_images))
train_cancerous_count = total_cancerous_images * train_ratio // (train_ratio + test_ratio)
test_cancerous_count = total_cancerous_images - train_cancerous_count

# Split the list of cancerous images into train and test
train_cancerous_images = cancerous_images[:train_cancerous_count]
test_cancerous_images = cancerous_images[train_cancerous_count:]

# Move cancerous images to train and test directories
move_files(original_cancerous_directory, train_cancerous_directory, train_cancerous_images)
move_files(original_cancerous_directory, test_cancerous_directory, test_cancerous_images)

# List all image files in the original healthy directory
healthy_images = [f for f in os.listdir(original_healthy_directory) if os.path.isfile(os.path.join(original_healthy_directory, f))]
random.shuffle(healthy_images)

# Calculate the number of images for train and test
total_healthy_images = len(healthy_images)
train_healthy_count = total_healthy_images * train_ratio // (train_ratio + test_ratio)
test_healthy_count = total_healthy_images - train_healthy_count

# Split the list of healthy images into train and test
train_healthy_images = healthy_images[:train_healthy_count]
test_healthy_images = healthy_images[train_healthy_count:]

# Move healthy images to train and test directories
move_files(original_healthy_directory, train_healthy_directory, train_healthy_images)
move_files(original_healthy_directory, test_healthy_directory, test_healthy_images)

print("Data organization completed.")

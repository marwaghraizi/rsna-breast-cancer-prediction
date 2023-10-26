import os
import sys
import numpy as np
from Augmentor import Pipeline

# Define input and output directories
input_dir = sys.argv[1]  # Replace with your input directory
output_dir = sys.argv[2]  # Replace with your output directory

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an augmentation pipeline
p = Pipeline(input_dir, output_directory=output_dir)

# Define augmentation operations (you can customize this)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.random_contrast(probability=0.5, min_factor=0.8, max_factor=1.2)
p.random_brightness(probability=0.5, min_factor=0.8, max_factor=1.2)
p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
p.skew_left_right(probability=0.4, magnitude=0.6)

# Set the number of images you want to create (per original image)
p.sample(965)  # Adjust the number as needed

# Execute the augmentation operations
p.process()

print("Data augmentation complete.")


import cv2
import numpy as np
import os
from tqdm import tqdm
import sys

path = sys.argv[1]
output_folder = sys.argv[2]
os.makedirs(output_folder, exist_ok=True)

image_files = [file for file in os.listdir(path) if file.endswith((".png"))]

# Batch size to not load all images in one go and kill my laptop again
batch_size = 2000 


for i in range(0, len(image_files), batch_size):
    batch_files = image_files[i:i + batch_size]
    images = []

    for file in tqdm(batch_files, desc=f"Normalizing images of batch {i} ..."):
        file_path = os.path.join(path, file)
        img = cv2.imread(file_path)

        if img is not None:
            # making sure that cv2 take the image as grayscale and not rgb
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            images.append(img)
        else:
            print(f"Failed to load image: {file_path}")

    # Process and save normalized images for the batch
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) #lower cliplimit if its too vibrant (2 seems to be the max?)
    # application of the CLAHE to our images    
    enhanced_images = [clahe.apply(img) for img in images]
    # try to normalize the image by highest and lowest value pixel (maybe comment here if already done by elouan?)
    normalized_images = [(img - np.min(img)) / (np.max(img) - np.min(img)) for img in enhanced_images]

    # save the norm images
    for j, normalized_img in enumerate(normalized_images):
        original_filename = os.path.splitext(batch_files[j])[0]
        output_path = os.path.join(output_folder, f"{original_filename}.jpg")
        cv2.imwrite(output_path, (normalized_img * 255).astype(np.uint8))


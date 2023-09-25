import os
import pandas as pd
import shutil

# Path to your dataset
CSV_PATH = 'C:/Users/amine/Documents/Personal/PYCAD/Learn/CNNs_ViT/boneage-training-dataset.csv'
IMAGES_PATH = 'C:/Users/amine/Documents/Personal/PYCAD/Learn/CNNs_ViT/boneage-training-dataset'
OUTPUT_PATH = 'C:/Users/amine/Documents/Personal/PYCAD/Learn/CNNs_ViT/boneage-training-dataset_subfolders_50'

# Define a function to determine the age range for a given bone age
def get_age_range(bone_age, range_size=50):
    lower_bound = (bone_age // range_size) * range_size
    upper_bound = lower_bound + range_size - 1
    return f"{lower_bound}-{upper_bound}"

# Load the CSV file
data = pd.read_csv(CSV_PATH)

# Create a folder for each unique age range
age_ranges = data['boneage'].apply(get_age_range).unique()
for age_range in age_ranges:
    folder_path = os.path.join(OUTPUT_PATH, age_range)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move each image to its corresponding age range folder
for index, row in data.iterrows():
    image_name = str(row['id']) + '.png'  # Assuming images are in PNG format
    age_range = get_age_range(row['boneage'])
    source_path = os.path.join(IMAGES_PATH, image_name)
    destination_path = os.path.join(OUTPUT_PATH, age_range, image_name)
    
    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)

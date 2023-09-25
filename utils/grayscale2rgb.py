from PIL import Image
from glob import glob

from tqdm import tqdm


images_train = sorted(glob('./boneage_training_dataset_subfolders_50/train/*/*'))
images_val = sorted(glob('./boneage_training_dataset_subfolders_50/val/*/*'))
images = images_train + images_val

for image in tqdm(images):
  img = Image.open(image).convert('RGB')
  img.save(image)
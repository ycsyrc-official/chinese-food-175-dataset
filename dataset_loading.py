import os
from PIL import Image
from tqdm import tqdm
import numpy as np

# function definition
def load_images_from_folder(folder):
    images = []
    labels = []
    subfolders = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
    for subfolder in tqdm(subfolders, desc="loading progress", ncols=80, dynamic_ncols=True):
        subfolder_path = os.path.join(folder, subfolder)
        files = [f for f in os.listdir(subfolder_path) if f.endswith((".jpg", ".png", ".jpeg"))]
        for filename in files:
            img_path = os.path.join(subfolder_path, filename)
            try:
                with Image.open(img_path) as img:
                    img = img.resize((150, 150))  # image size transfer
                    img = img.convert('RGB')  # convert to RGB
                    images.append(np.array(img))
                    labels.append(subfolder)
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
    return images, labels

# load chinese-food-175 dataset
folder_path = rf'chinese-food-175'
images, labels = load_images_from_folder(folder_path)

images = np.array(images)
labels = np.array(labels)

print(images)



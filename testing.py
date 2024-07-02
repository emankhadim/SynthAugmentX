import cv2
import os
from augmentations import random_rotation, random_scaling, random_translation, random_brightness, random_noise

output_dir = "synthetic_data"
test_output_dir = "test_data"
if not os.path.exists(test_output_dir):
    os.makedirs(test_output_dir)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def test_augmentation(image, augmentation_function):
    augmented_image = augmentation_function(image)
    return augmented_image

images = load_images_from_folder(output_dir)

for i, image in enumerate(images):
    augmented_image = test_augmentation(image, random_rotation)  # Change the function as needed
    cv2.imwrite(os.path.join(test_output_dir, f"test_image_{i}.png"), augmented_image)

print(f"Tested {len(images)} synthetic images and saved results in '{test_output_dir}' directory.")

import cv2
import numpy as np
import os
import random
from data_preprocessing import load_and_preprocess_data, get_label_name

# Parameters
num_images = 1000
output_dir = "synthetic_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load and preprocess CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = load_and_preprocess_data()

def augment_image(image):
    from augmentations import random_rotation, random_scaling, random_translation, random_brightness, random_noise
    augmentations = [random_rotation, random_scaling, random_translation, random_brightness, random_noise]
    aug_image = image.copy()
    for aug in augmentations:
        if random.random() < 0.5:
            aug_image = aug(aug_image)
    return aug_image

def generate_random_shape(image):
    shape_type = random.choice(["circle", "square", "triangle"])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    thickness = -1  # Fill the shape

    if shape_type == "circle":
        center = (random.randint(10, 22), random.randint(10, 22))
        radius = random.randint(3, 6)
        cv2.circle(image, center, radius, color, thickness)
        return {"type": "circle", "center": center, "radius": radius}
    
    elif shape_type == "square":
        top_left = (random.randint(5, 27), random.randint(5, 27))
        side = random.randint(6, 12)
        bottom_right = (top_left[0] + side, top_left[1] + side)
        cv2.rectangle(image, top_left, bottom_right, color, thickness)
        return {"type": "square", "top_left": top_left, "bottom_right": bottom_right}
    
    elif shape_type == "triangle":
        pt1 = (random.randint(10, 22), random.randint(10, 22))
        pt2 = (pt1[0] + random.randint(-6, 6), pt1[1] + random.randint(-6, 6))
        pt3 = (pt1[0] + random.randint(-6, 6), pt1[1] + random.randint(-6, 6))
        pts = np.array([pt1, pt2, pt3])
        cv2.drawContours(image, [pts], 0, color, thickness)
        return {"type": "triangle", "points": [pt1, pt2, pt3]}

# Generate images
for i in range(num_images):
    image = x_train[random.randint(0, len(x_train) - 1)].copy()
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Ensure the image is in the correct color format
    annotation = generate_random_shape(image)
    augmented_image = augment_image(image)
    cv2.imwrite(os.path.join(output_dir, f"image_{i}.png"), augmented_image)
    with open(os.path.join(output_dir, f"annotation_{i}.txt"), 'w') as f:
        f.write(str(annotation))

print(f"Generated {num_images} synthetic images with annotations in '{output_dir}' directory.")

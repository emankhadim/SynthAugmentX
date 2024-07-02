import streamlit as st
import cv2
import numpy as np
from augmentations import random_rotation, random_scaling, random_translation, random_brightness, random_noise, random_dilation, random_erosion
from data_preprocessing import load_and_preprocess_data

# Function to load image from file uploader
def load_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    return image

st.title("Synthetic Data Generator")

# Option to choose data source
data_source = st.radio("Choose the data source", ("CIFAR-10", "Upload an Image"))

if data_source == "CIFAR-10":
    (x_train, y_train), (x_test, y_test) = load_and_preprocess_data()
    image_index = st.slider("Select an image index", 0, len(x_train) - 1, 0)
    original_image = x_train[image_index]
    original_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2BGR)  # Ensure correct color format
    st.image(original_image, caption=f"Original CIFAR-10 Image {image_index}", use_column_width=True)

elif data_source == "Upload an Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        original_image = load_image(uploaded_file)
        st.image(original_image, caption="Original Uploaded Image", use_column_width=True)

# Augmentation options
augmentation_functions = {
    "Random Rotation": random_rotation,
    "Random Scaling": random_scaling,
    "Random Translation": random_translation,
    "Random Brightness": random_brightness,
    "Random Noise": random_noise,
    "Random Dilation": random_dilation,
    "Random Erosion": random_erosion
}

if 'original_image' in locals():
    augmentation_choice = st.selectbox("Choose augmentation", list(augmentation_functions.keys()) + ["Apply All"])

    if st.button("Apply Augmentation"):
        if augmentation_choice == "Apply All":
            augmented_images = [original_image]
            captions = ["Original Image"]
            for aug_name, aug_func in augmentation_functions.items():
                augmented_image = aug_func(original_image.copy())
                augmented_images.append(augmented_image)
                captions.append(aug_name)
            st.image(augmented_images, caption=captions, use_column_width=True)
        else:
            augmented_image = augmentation_functions[augmentation_choice](original_image)
            st.image(augmented_image, caption="Augmented Image", use_column_width=True)

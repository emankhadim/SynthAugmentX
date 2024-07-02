# SynthAugmentX: Dynamic Image Augmentation Toolkit

SynthAugmentX is a powerful toolkit designed for generating synthetic data using various image augmentation techniques. This project provides an interactive interface to visualize the effects of these augmentations, making it an excellent tool for data augmentation in machine learning projects.

## Features
- Load CIFAR-10 data or upload your own image
- Apply various augmentations including rotation, scaling, translation, brightness adjustment, noise addition, dilation, and erosion
- Display augmented images side by side for easy comparison

## Installation
1. Clone the repository: `git clone <your-repository-URL>`, then navigate to the directory: `cd SynthAugmentX`.
2. Install the required packages with `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.

## Usage
1. **Select Data Source**: Choose between CIFAR-10 dataset or upload an image.
2. **Choose Augmentation**: Select an augmentation technique from the dropdown menu.
3. **Apply Augmentation**: Click the "Apply Augmentation" button to see the augmented image.
4. **Apply All Augmentations**: Choose the "Apply All" option to apply all augmentations and display them side by side.

## Augmentations
- **Random Rotation**: Rotates the image by a random angle.
- **Random Scaling**: Scales the image by a random factor.
- **Random Translation**: Translates the image by a random offset.
- **Random Brightness**: Adjusts the brightness of the image randomly.
- **Random Noise**: Adds random noise to the image.
- **Random Dilation**: Applies dilation to the image.
- **Random Erosion**: Applies erosion to the image.



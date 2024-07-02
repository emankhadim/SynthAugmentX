# SynthAugmentX: Dynamic Image Augmentation Toolkit

SynthAugmentX is a powerful toolkit designed for generating synthetic data using various image augmentation techniques. This project provides an interactive interface to visualize the effects of these augmentations, making it an excellent tool for data augmentation in machine learning projects.

## Features
- Load CIFAR-10 data or upload your own image
- Apply various augmentations including rotation, scaling, translation, brightness adjustment, noise addition, dilation, and erosion
- Display augmented images side by side for easy comparison

## Installation
1. Clone the repository: `git clone https://github.com/emankhadim/SynthAugmentX`, then navigate to the directory: `cd SynthAugmentX`.
2. Install the required packages with `pip install -r requirements.txt`.

## Usage
1. **Run the training script**: This will generate synthetic data and create the `synthetic_data` folder. Use the command `python train.py`.
2. **Run the testing script**: This will test the generated synthetic data. Use the command `python test.py`.
3. **Run the Streamlit app**: This will launch the interactive interface to visualize the augmentations. Use the command `streamlit run app.py`.

## Augmentations
- **Random Rotation**: Rotates the image by a random angle.
- **Random Scaling**: Scales the image by a random factor.
- **Random Translation**: Translates the image by a random offset.
- **Random Brightness**: Adjusts the brightness of the image randomly.
- **Random Noise**: Adds random noise to the image.
- **Random Dilation**: Applies dilation to the image.
- **Random Erosion**: Applies erosion to the image.



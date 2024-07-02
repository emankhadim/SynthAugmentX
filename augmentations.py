import cv2
import numpy as np
import random

def random_rotation(image):
    angle = random.uniform(-30, 30)
    M = cv2.getRotationMatrix2D((image.shape[1]//2, image.shape[0]//2), angle, 1)
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def random_scaling(image):
    scale = random.uniform(0.7, 1.3)
    return cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

def random_translation(image):
    tx = random.uniform(-5, 5)
    ty = random.uniform(-5, 5)
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def random_brightness(image):
    value = random.uniform(0.5, 1.5)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype=np.float64)
    hsv[:,:,2] = hsv[:,:,2]*value
    hsv[:,:,2][hsv[:,:,2]>255] = 255
    hsv = np.array(hsv, dtype=np.uint8)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def random_noise(image):
    noise = np.random.normal(0, 25, image.shape)
    noisy_image = image + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def random_dilation(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

def random_erosion(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

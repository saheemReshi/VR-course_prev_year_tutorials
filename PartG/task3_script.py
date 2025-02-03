# File: /image-processing-project/image-processing-project/PartG/task3_script.py

# This script provides a template for applying transformations to an image and observing SIFT keypoints.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_transformations(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply transformations (rotation, scaling, illumination changes)
    # Example: Rotate the image
    height, width = gray_image.shape
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotate by 45 degrees
    rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (width, height))

    # Example: Scale the image
    scaled_image = cv2.resize(gray_image, None, fx=0.5, fy=0.5)

    # Example: Change illumination (simple brightness adjustment)
    bright_image = cv2.convertScaleAbs(gray_image, alpha=1.5, beta=0)  # Increase brightness

    # Detect SIFT keypoints
    sift = cv2.SIFT_create()
    keypoints_original = sift.detect(gray_image, None)
    keypoints_rotated = sift.detect(rotated_image, None)
    keypoints_scaled = sift.detect(scaled_image, None)
    keypoints_bright = sift.detect(bright_image, None)

    # Draw keypoints
    img_keypoints_original = cv2.drawKeypoints(gray_image, keypoints_original, None)
    img_keypoints_rotated = cv2.drawKeypoints(rotated_image, keypoints_rotated, None)
    img_keypoints_scaled = cv2.drawKeypoints(scaled_image, keypoints_scaled, None)
    img_keypoints_bright = cv2.drawKeypoints(bright_image, keypoints_bright, None)

    # Display results
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(img_keypoints_original)
    plt.title('Original Image Keypoints')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(img_keypoints_rotated)
    plt.title('Rotated Image Keypoints')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(img_keypoints_scaled)
    plt.title('Scaled Image Keypoints')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(img_keypoints_bright)
    plt.title('Brightened Image Keypoints')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# Example usage
# apply_transformations('../sample.png')  # Replace with your image path
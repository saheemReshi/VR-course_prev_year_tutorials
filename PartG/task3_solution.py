# File: /image-processing-project/image-processing-project/PartG/task3_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_transformations(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply SIFT
    sift = cv2.SIFT_create()
    keypoints = sift.detect(gray_image, None)
    keypoints_blurred = sift.detect(blurred_image, None)

    # Draw keypoints
    image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, (0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    image_with_blurred_keypoints = cv2.drawKeypoints(image, keypoints_blurred, None, (255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image_with_keypoints, cv2.COLOR_BGR2RGB))
    plt.title('SIFT Keypoints on Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image_with_blurred_keypoints, cv2.COLOR_BGR2RGB))
    plt.title('SIFT Keypoints on Blurred Image')
    plt.axis('off')

    plt.show()

# Example usage
apply_transformations('../sample.png')
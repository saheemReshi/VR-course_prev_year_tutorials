# File: /image-processing-project/image-processing-project/PartE/task3_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_marr_hildreth(image_path, sigma):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Gaussian filter
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)

    # Compute the Laplacian of the Gaussian
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    # Zero-crossing detection
    zero_crossing = np.zeros_like(laplacian)
    zero_crossing[1:-1, 1:-1] = (
        (laplacian[1:-1, 1:-1] > 0) & (laplacian[:-2, 1:-1] < 0) |
        (laplacian[1:-1, 1:-1] > 0) & (laplacian[1:-1, :-2] < 0) |
        (laplacian[1:-1, 1:-1] < 0) & (laplacian[2:, 1:-1] > 0) |
        (laplacian[1:-1, 1:-1] < 0) & (laplacian[1:-1, 2:] > 0)
    ).astype(np.uint8) * 255

    return image, zero_crossing

def main():
    image_path = '../sample.png'  # Replace with your image path
    sigma = 1.0  # Standard deviation for Gaussian kernel

    original_image, zero_crossing_image = apply_marr_hildreth(image_path, sigma)

    # Display results
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(original_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Zero-Crossing Map')
    plt.imshow(zero_crossing_image, cmap='gray')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
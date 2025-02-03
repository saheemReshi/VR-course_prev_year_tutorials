# File: /image-processing-project/image-processing-project/PartD/task3_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def high_pass_filter(image, kernel_size):
    # Create a Gaussian filter
    gaussian_filter = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    # Subtract the Gaussian filter from the original image
    high_pass_image = cv2.subtract(image, gaussian_filter)
    return high_pass_image

def main():
    # Load the image
    image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)

    # Apply high-pass filtering with different kernel sizes
    hpf_3x3 = high_pass_filter(image, 3)
    hpf_5x5 = high_pass_filter(image, 5)

    # Apply Sobel filter for edge detection
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)

    # Apply Laplacian filter
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # Create sharpened image by combining original and Laplacian
    sharpened_image = cv2.add(image.astype(np.float64), laplacian)

    # Display results
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
    plt.subplot(2, 3, 2), plt.imshow(hpf_3x3, cmap='gray'), plt.title('HPF 3x3')
    plt.subplot(2, 3, 3), plt.imshow(hpf_5x5, cmap='gray'), plt.title('HPF 5x5')
    plt.subplot(2, 3, 4), plt.imshow(sobel_combined, cmap='gray'), plt.title('Sobel Filter')
    plt.subplot(2, 3, 5), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian Filter')
    plt.subplot(2, 3, 6), plt.imshow(sharpened_image, cmap='gray'), plt.title('Sharpened Image')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
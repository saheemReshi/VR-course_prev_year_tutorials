# File: /image-processing-project/image-processing-project/PartC/task2_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_impulse_noise(image, amount=0.02):
    noisy_image = np.copy(image)
    num_salt = np.ceil(amount * image.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 1

    num_pepper = np.ceil(amount* image.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0
    return noisy_image

def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

def main():
    # Load the image
    image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)

    # Add impulse noise
    noisy_image = add_impulse_noise(image)

    # Apply median filter
    filtered_image_3x3 = median_filter(noisy_image, 3)
    filtered_image_5x5 = median_filter(noisy_image, 5)

    # Display results
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    plt.title('Noisy Image')
    plt.imshow(noisy_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Filtered Image (3x3 Median)')
    plt.imshow(filtered_image_3x3, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Filtered Image (5x5 Median)')
    plt.imshow(filtered_image_5x5, cmap='gray')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
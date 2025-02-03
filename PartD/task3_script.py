# Contents of /image-processing-project/image-processing-project/PartD/task3_script.py

# This script provides a template for high-pass filtering in the frequency domain.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def high_pass_filter(image_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Perform 2D Fourier Transform
    f_transform = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    f_transform_shifted = np.fft.fftshift(f_transform)
    
    # Create a mask for high-pass filtering
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols, 2), np.uint8)
    r = 30  # Radius for the high-pass filter
    cv2.circle(mask, (ccol, crow), r, (0, 0, 0), -1)
    
    # Apply the mask to the shifted Fourier transform
    f_transform_shifted_filtered = f_transform_shifted * mask
    
    # Inverse Fourier Transform to get the filtered image
    f_transform_filtered = np.fft.ifftshift(f_transform_shifted_filtered)
    img_filtered = cv2.idft(f_transform_filtered)
    img_filtered = cv2.magnitude(img_filtered[:, :, 0], img_filtered[:, :, 1])
    
    # Display the original and filtered images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img, cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title('High-Pass Filtered Image')
    plt.imshow(img_filtered, cmap='gray')
    
    plt.show()

# Example usage
# high_pass_filter('../sample.png')  # Replace with your image path
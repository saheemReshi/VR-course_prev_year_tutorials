# File: /image-processing-project/image-processing-project/PartD/task4_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_notch_filter(shape, notch_radius, notch_center):
    rows, cols = shape
    x = np.arange(cols)
    y = np.arange(rows)
    X, Y = np.meshgrid(x, y)
    D = np.sqrt((X - notch_center[0])**2 + (Y - notch_center[1])**2)
    notch_filter = np.ones((rows, cols), dtype=np.float32)
    notch_filter[D < notch_radius] = 0
    return notch_filter

def apply_notch_filter(image, notch_radius, notch_center):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    notch_filter = create_notch_filter(image.shape, notch_radius, notch_center)
    filtered_dft = dft_shift * notch_filter[:, :, np.newaxis]
    
    img_back = cv2.idft(np.fft.ifftshift(filtered_dft))
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    return img_back

def main():
    # Load the image
    image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)
    
    # Define notch filter parameters
    notch_radius = 30
    notch_center = (100, 100)  # Example coordinates, adjust as needed
    
    # Apply notch filter
    filtered_image = apply_notch_filter(image, notch_radius, notch_center)
    
    # Display results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title('Filtered Image')
    plt.imshow(filtered_image, cmap='gray')
    
    plt.show()

if __name__ == "__main__":
    main()
    
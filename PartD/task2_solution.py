# File: /image-processing-project/image-processing-project/PartD/task2_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def ideal_low_pass_filter(image, cutoff):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), cutoff, 1, thickness=-1)
    return mask

def gaussian_low_pass_filter(image, cutoff):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    x = np.linspace(-ccol, ccol-1, cols)
    y = np.linspace(-crow, crow-1, rows)
    X, Y = np.meshgrid(x, y)
    gaussian_mask = np.exp(-(X**2 + Y**2) / (2 * (cutoff / 2.0)**2))
    return gaussian_mask

def apply_filter(image, mask):
    f_transform = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    f_transform_shifted = np.fft.fftshift(f_transform)
    filtered = f_transform_shifted * mask[:, :, np.newaxis]
    f_ishift = np.fft.ifftshift(filtered)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    return img_back

# Load image
image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)

# Apply Ideal Low Pass Filter
cutoff = 30
ideal_mask = ideal_low_pass_filter(image, cutoff)
ideal_filtered = apply_filter(image, ideal_mask)

# Apply Gaussian Low Pass Filter
gaussian_mask = gaussian_low_pass_filter(image, cutoff)
gaussian_filtered = apply_filter(image, gaussian_mask)

# Display results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Ideal Low Pass Filtered')
plt.imshow(ideal_filtered, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Gaussian Low Pass Filtered')
plt.imshow(gaussian_filtered, cmap='gray')
plt.axis('off')

plt.show()
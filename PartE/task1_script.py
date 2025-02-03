# Contents of /image-processing-project/image-processing-project/PartE/task1_script.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Apply Prewitt operator
prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewitt_x_result = cv2.filter2D(image, -1, prewitt_x)
prewitt_y_result = cv2.filter2D(image, -1, prewitt_y)
prewitt_magnitude = np.sqrt(prewitt_x_result**2 + prewitt_y_result**2)

# Display results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Sobel Magnitude')
plt.imshow(sobel_magnitude, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Prewitt Magnitude')
plt.imshow(prewitt_magnitude, cmap='gray')
plt.axis('off')

plt.show()
# File: /image-processing-project/image-processing-project/PartB/task2_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def log_transformation(image, c=1):
    # Apply log transformation
    log_image = c * np.log1p(image)
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image

# Load the image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply log transformation
transformed_image = log_transformation(image)

# Display the original and transformed images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Log Transformed Image')
plt.imshow(transformed_image, cmap='gray')
plt.axis('off')

plt.show()
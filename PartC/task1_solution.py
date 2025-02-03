import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../sample.png')

# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply low-pass filtering using average filter
average_filter_3x3 = cv2.blur(image_rgb, (3, 3))
average_filter_5x5 = cv2.blur(image_rgb, (5, 5))

# Apply low-pass filtering using Gaussian filter
gaussian_filter_3x3 = cv2.GaussianBlur(image_rgb, (3, 3), 0)
gaussian_filter_5x5 = cv2.GaussianBlur(image_rgb, (5, 5), 0)

# Display the original and filtered images
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Average Filter 3x3')
plt.imshow(average_filter_3x3)
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Average Filter 5x5')
plt.imshow(average_filter_5x5)
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Gaussian Filter 3x3')
plt.imshow(gaussian_filter_3x3)
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title('Gaussian Filter 5x5')
plt.imshow(gaussian_filter_5x5)
plt.axis('off')

plt.tight_layout()
plt.show()
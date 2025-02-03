# File: /image-processing-project/image-processing-project/PartA/task4_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
image = cv2.imread('../sample.png')

# Downsample the image
downsampled_image = cv2.pyrDown(image)

# Upsample the image back to original size
upsampled_image = cv2.pyrUp(downsampled_image, dstsize=(image.shape[1], image.shape[0]))

# Display the original, downsampled, and upsampled images
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Downsampled Image')
plt.imshow(cv2.cvtColor(downsampled_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Upsampled Image')
plt.imshow(cv2.cvtColor(upsampled_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
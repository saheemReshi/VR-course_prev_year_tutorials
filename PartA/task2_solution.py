# File: /image-processing-project/image-processing-project/PartA/task2_solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the RGB image
image = cv2.imread('../sample.png')

# Split the image into its respective Red, Green, and Blue channels
b, g, r = cv2.split(image)

# Display the original image and the individual channels
plt.figure(figsize=(10, 5))

plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(r, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(g, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(b, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.tight_layout()
plt.show()
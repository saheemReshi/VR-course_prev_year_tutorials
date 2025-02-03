# File: /image-processing-project/image-processing-project/PartA/task3_solution.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the RGB image
image = cv2.imread('../sample.png')

# Convert RGB to different color spaces
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Split the channels
h_channel, s_channel, v_channel = cv2.split(hsv_image)
l_channel, a_channel, b_channel = cv2.split(lab_image)
y_channel, cr_channel, cb_channel = cv2.split(ycrcb_image)

# Display the channels
plt.figure(figsize=(12, 8))

plt.subplot(3, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(h_channel, cmap='gray')
plt.title('Hue Channel (HSV)')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(s_channel, cmap='gray')
plt.title('Saturation Channel (HSV)')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(v_channel, cmap='gray')
plt.title('Value Channel (HSV)')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(l_channel, cmap='gray')
plt.title('L Channel (Lab)')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.imshow(a_channel, cmap='gray')
plt.title('A Channel (Lab)')
plt.axis('off')

plt.subplot(3, 3, 7)
plt.imshow(b_channel, cmap='gray')
plt.title('B Channel (Lab)')
plt.axis('off')

plt.subplot(3, 3, 8)
plt.imshow(y_channel, cmap='gray')
plt.title('Y Channel (YCrCb)')
plt.axis('off')

plt.subplot(3, 3, 9)
plt.imshow(cr_channel, cmap='gray')
plt.title('Cr Channel (YCrCb)')
plt.axis('off')

plt.tight_layout()
plt.show()
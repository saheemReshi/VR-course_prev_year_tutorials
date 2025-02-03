# Contents of /image-processing-project/image-processing-project/PartA/task3_script.py

import cv2
import numpy as np

# Load the RGB image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path)

# Convert RGB image to different color spaces
# 1. HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 2. LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

# 3. YCrCb
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Display the original and converted images
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('LAB Image', lab_image)
cv2.imshow('YCrCb Image', ycrcb_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
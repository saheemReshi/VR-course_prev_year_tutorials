import cv2
import numpy as np 

image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)

# Define the minimum and maximum pixel values
min_pixel = np.min(image)
max_pixel = np.max(image)

# Perform contrast stretching
stretched_image = ((image - min_pixel) / (max_pixel - min_pixel)) * 255
stretched_image = np.uint8(stretched_image)

# Display the original and stretched images
cv2.imshow('Original Image', image)
cv2.imshow('Contrast Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
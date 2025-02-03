# Contents of /image-processing-project/image-processing-project/PartD/task2_script.py

import cv2
import numpy as np

# Load the image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform 2D Fourier Transform
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Create a mask for low-pass filtering
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
radius = 30  # Adjust the radius as needed
mask = np.zeros((rows, cols, 2), np.uint8)
cv2.circle(mask, (ccol, crow), radius, (1, 1), thickness=-1)

# Apply the mask to the DFT
fshift = dft_shift * mask

# Inverse DFT to get the filtered image
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Display the results
cv2.imshow('Input Image', image)
cv2.imshow('Filtered Image', img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
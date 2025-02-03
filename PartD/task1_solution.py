import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../sample.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform 2D Fourier Transform
dft = cv2.dft(np.float32(gray_image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Calculate the magnitude spectrum
magnitude_spectrum = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])
magnitude_spectrum = np.log(magnitude_spectrum + 1)

# Display the frequency spectrum
plt.figure(figsize=(10, 10))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Frequency Spectrum')
plt.axis('off')
plt.show()
# Contents of /image-processing-project/image-processing-project/PartD/task1_script.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform 2D Fourier Transform
# Your code here to compute the Fourier Transform

# Shift the zero frequency component to the center
# Your code here to shift the frequency spectrum

# Compute the magnitude spectrum
# Your code here to compute the magnitude spectrum

# Display the frequency spectrum using a log scale
# Your code here to display the spectrum

plt.show()
# Contents of /image-processing-project/image-processing-project/PartC/task2_script.py

import cv2
import numpy as np

# Load the image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Split the image into its Red, Green, and Blue channels
# Your code here to extract channels

# Display the channels
# Your code here to display channels

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
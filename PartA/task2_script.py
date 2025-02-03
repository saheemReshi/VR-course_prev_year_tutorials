# Contents of /image-processing-project/image-processing-project/PartA/task2_script.py

import cv2
import numpy as np

# Load the RGB image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Split the image into Red, Green, and Blue channels
    # Your code here to extract and display the channels

    # Display the channels
    # Your code here to display the channels using cv2.imshow() or any other method

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
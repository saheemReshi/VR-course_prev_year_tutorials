# File: /image-processing-project/image-processing-project/PartB/task3_solution.py

import cv2
import numpy as np

def image_whitening(image):
    # Convert to float32 for precision
    image_float = image.astype(np.float32)
    
    # Normalize the image
    mean = np.mean(image_float)
    std_dev = np.std(image_float)
    
    # Normalize to have mean 0 and std deviation 1
    whitened_image = (image_float - mean) / std_dev
    
    # Clip values to be in the range [0, 255]
    whitened_image = np.clip(whitened_image * 255, 0, 255).astype(np.uint8)
    
    return whitened_image

# Load a grayscale image
image_path = '../sample.png'  # Update with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply image whitening
whitened_image = image_whitening(image)

# Display the original and whitened images
cv2.imshow('Original Image', image)
cv2.imshow('Whitened Image', whitened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
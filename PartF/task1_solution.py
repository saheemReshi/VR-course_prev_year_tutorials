# File: /image-processing-project/image-processing-project/PartF/task1_solution.py

import cv2
import numpy as np

def harris_corner_detection(image_path, threshold=0.01):
    # Load the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert to float32
    gray = np.float32(gray)

    # Harris corner detection
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Result is dilated for marking the corners
    dst = cv2.dilate(dst, None)

    # Thresholding the corners
    img[dst > threshold * dst.max()] = [0, 0, 255]

    return img

if __name__ == "__main__":
    image_path = '../sample.png'  # Replace with your image path
    result_image = harris_corner_detection(image_path)
    
    # Display the result
    cv2.imshow('Harris Corners', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
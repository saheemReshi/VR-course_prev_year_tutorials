# File: /image-processing-project/image-processing-project/PartG/task1_solution.py

import cv2
import numpy as np

def main():
    # Load the image
    image = cv2.imread('../sample.png')

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    keypoints, descriptors = sift.detectAndCompute(image, None)

    # Draw keypoints on the image
    img_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the image with keypoints
    cv2.imshow('SIFT Keypoints', img_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
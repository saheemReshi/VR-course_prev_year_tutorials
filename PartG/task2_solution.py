# File: /image-processing-project/image-processing-project/PartG/task2_solution.py

import cv2
import numpy as np

def compare_sift_keypoints(image1_path, image2_path):
    # Load images
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and compute descriptors
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # Create a BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)

    # Sort matches by distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw matches
    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Display results
    cv2.imshow('SIFT Keypoint Matches', img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return number of keypoints detected
    return len(keypoints1), len(keypoints2), len(matches)

if __name__ == "__main__":
    image1_path = '../sample.png'  # Replace with your image path
    image2_path = '../sample2.jpg'  # Replace with your image path2 
    keypoints1, keypoints2, matches = compare_sift_keypoints(image1_path, image2_path)
    print(f'Keypoints in Image 1: {keypoints1}')
    print(f'Keypoints in Image 2: {keypoints2}')
    print(f'Matches: {matches}')
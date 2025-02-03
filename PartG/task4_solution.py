# File: /image-processing-project/image-processing-project/PartG/task4_solution.py

import cv2
import numpy as np

def load_images(image1_path, image2_path):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    return img1, img2

def detect_and_match_features(img1, img2):
    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # Create a BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)

    # Sort matches by distance
    matches = sorted(matches, key=lambda x: x.distance)

    return keypoints1, keypoints2, matches

def draw_matches(img1, img2, keypoints1, keypoints2, matches):
    # Draw matches
    matched_image = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    return matched_image

def main():
    # Load images
    img1, img2 = load_images('../sample.png', '../sample2.jpg')

    # Detect and match features
    keypoints1, keypoints2, matches = detect_and_match_features(img1, img2)

    # Draw matches
    matched_image = draw_matches(img1, img2, keypoints1, keypoints2, matches)

    # Display the matched image
    cv2.imshow('Matched Features', matched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
# File: /image-processing-project/image-processing-project/PartG/task4_script.py

# This script provides a template for detecting features in two images of the same object.

import cv2
import numpy as np

def load_images(image_path1, image_path2):
    # Load the two images
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)
    return img1, img2

def detect_and_match_features(img1, img2):
    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # Create a matcher
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)

    # Sort matches by distance
    matches = sorted(matches, key=lambda x: x.distance)
    
    return keypoints1, keypoints2, matches

def draw_matches(img1, img2, keypoints1, keypoints2, matches):
    # Draw matches
    matched_image = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    return matched_image

def main():
    # Paths to the images
    image_path1 = '../sample.png'
    image_path2 = '../sample2.jpg'

    # Load images
    img1, img2 = load_images(image_path1, image_path2)

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
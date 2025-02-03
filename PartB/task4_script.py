import cv2
import numpy as np

def contrast_stretching(image):
    # Implement contrast stretching here
    pass

def main():
    # Load a grayscale image
    image_path = '../sample.png'  # Update with your image path
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Call the contrast stretching function
    stretched_image = contrast_stretching(image)

    # Display the original and stretched images
    cv2.imshow('Original Image', image)
    cv2.imshow('Contrast Stretched Image', stretched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
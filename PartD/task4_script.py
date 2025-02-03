# File: /image-processing-project/image-processing-project/PartD/task4_script.py

# This script provides a template for notch reject filtering to remove periodic noise.
# Students will fill in the necessary code.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def notch_filter(image, d0, u0, v0):
    # Create a mask for the notch filter
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.uint8)

    # Create the notch filter
    for u in range(rows):
        for v in range(cols):
            if np.sqrt((u - crow) ** 2 + (v - ccol) ** 2) <= d0:
                mask[u, v] = 0

    # Apply the mask to the frequency domain representation
    f_transform = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    f_transform_shifted = np.fft.fftshift(f_transform)
    f_transform_shifted *= mask[:, :, np.newaxis]

    # Inverse DFT to get the filtered image
    f_transform_ishifted = np.fft.ifftshift(f_transform_shifted)
    img_back = cv2.idft(f_transform_ishifted)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    return img_back

def main():
    # Load the image
    image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)

    # Parameters for the notch filter
    d0 = 30  # Cutoff frequency
    u0 = 0   # Frequency component to remove
    v0 = 0   # Frequency component to remove

    # Apply the notch filter
    filtered_image = notch_filter(image, d0, u0, v0)

    # Display the original and filtered images
    plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
    plt.subplot(122), plt.imshow(filtered_image, cmap='gray'), plt.title('Filtered Image')
    plt.show()

if __name__ == "__main__":
    main()
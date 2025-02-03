import cv2
import numpy as np
import matplotlib.pyplot as plt

def high_pass_filter(image):
    # Apply Sobel filter
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Apply Laplacian filter
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # Convert image to the same type as laplacian
    image_64f = image.astype(np.float64)
    # Combine original image with Laplacian result for sharpening
    sharpened_image = cv2.addWeighted(image_64f, 1.5, laplacian, -0.5, 0)

    return sobel_magnitude, laplacian, sharpened_image

# Load the image
image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)

# Apply high-pass filtering
sobel_magnitude, laplacian, sharpened_image = high_pass_filter(image)

# Display results
plt.figure(figsize=(12, 8))
plt.subplot(1, 3, 1)
plt.title('Sobel Magnitude')
plt.imshow(sobel_magnitude, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Laplacian Filter')
plt.imshow(laplacian, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Sharpened Image')
plt.imshow(sharpened_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
# File: /image-processing-project/image-processing-project/PartH/task2_solution.py

import cv2
import numpy as np

def compute_co_occurrence_matrix(image, distances, angles):
    co_matrix = np.zeros((256, 256), dtype=np.int32)
    for distance in distances:
        for angle in angles:
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    if angle == 0:  # 0 degrees
                        if j + distance < image.shape[1]:
                            co_matrix[image[i, j], image[i, j + distance]] += 1
                    elif angle == 45:  # 45 degrees
                        if i - distance >= 0 and j + distance < image.shape[1]:
                            co_matrix[image[i, j], image[i - distance, j + distance]] += 1
                    elif angle == 90:  # 90 degrees
                        if i - distance >= 0:
                            co_matrix[image[i, j], image[i - distance, j]] += 1
                    elif angle == 135:  # 135 degrees
                        if i - distance >= 0 and j - distance >= 0:
                            co_matrix[image[i, j], image[i - distance, j - distance]] += 1
    return co_matrix

def extract_texture_features(co_matrix):
    features = {}
    features['contrast'] = np.sum((np.arange(256)[:, None] - np.arange(256)) ** 2 * co_matrix)
    features['correlation'] = np.corrcoef(co_matrix.flatten())
    features['energy'] = np.sum(co_matrix ** 2)
    features['entropy'] = -np.sum(co_matrix / np.sum(co_matrix) * np.log(co_matrix + 1e-10))
    features['homogeneity'] = np.sum(co_matrix / (1 + np.abs(np.arange(256)[:, None] - np.arange(256))))
    return features

def main():
    image1 = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('../sample2.jpg', cv2.IMREAD_GRAYSCALE)

    distances = [1]
    angles = [0, 45, 90, 135]

    co_matrix1 = compute_co_occurrence_matrix(image1, distances, angles)
    co_matrix2 = compute_co_occurrence_matrix(image2, distances, angles)

    features1 = extract_texture_features(co_matrix1)
    features2 = extract_texture_features(co_matrix2)

    print("Texture features for Image 1:", features1)
    print("Texture features for Image 2:", features2)

if __name__ == "__main__":
    main()
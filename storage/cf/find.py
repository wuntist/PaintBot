import numpy as np
from PIL import Image

def find_nearest_color(pixel, limited_colors):
    distances = np.linalg.norm(limited_colors - pixel, axis=1)  # Compute Euclidean distances
    nearest_index = np.argmin(distances)  # Find index of the nearest color
    return limited_colors[nearest_index]  # Return the nearest color value

def find_nearest_colors(real_image, limited_colors):
    result_colors = []

    for i in range(real_image.shape[0]):
        for j in range(real_image.shape[1]):
            pixel = real_image[i, j]
            nearest_color = find_nearest_color(pixel, limited_colors)
            result_colors.append(nearest_color)

    return result_colors

limited_colors = np.array([
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 255],
    [0, 0, 0]
])
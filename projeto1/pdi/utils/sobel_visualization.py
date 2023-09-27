import numpy as np

def sobelVisualization(image: np.ndarray):
    newImage = np.abs(image)

    minColor, maxColor = np.min(newImage), np.max(newImage)

    return np.round(((newImage - minColor) / (maxColor - minColor)) * 255)

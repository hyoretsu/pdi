import math
import numpy as np
from PIL import Image

def rgbToHsv(image: Image.Image):
    pixels = np.array(image)
    rows, columns = len(pixels), len(pixels[0])

    hsvImage = np.empty([rows, columns, 3], dtype=float)

    for i in range(rows):
        for j in range(columns):
            r, g, b = pixels[i][j] / 255

            maxColor = max(r, g, b)
            minColor = min(r, g, b)

            delta = maxColor - minColor

            h = 0
            if maxColor != minColor:
                if maxColor == r and g >= b:
                    h = 60 * (g - b) / delta
                elif maxColor == r and g < b:
                    h = 60 * (g - b) / delta + 360
                elif maxColor == g:
                    h = 60 * (b - r) / delta + 120
                elif maxColor == b:
                    h = 60 * (r - g) / delta + 240

            s = 0.0
            if maxColor > 0:
                s = 1 - (minColor / maxColor)

            v = maxColor

            hsvImage[i][j] = [h, s, v]

    return hsvImage


def hsvToRgb(tensor):
    rows, columns = len(tensor), len(tensor[0])

    rgbImage = np.empty([rows, columns, 3], dtype=np.int8)

    for i in range(rows):
        for j in range(columns):
            h, s, v = tensor[i][j]

            if s == 0:
                v *= 255

                rgbImage[i][j] = [v, v, v]

                continue

            r, g, b = 0, 0, 0

            sectorPos = h / 60
            sectorNumber = math.floor(sectorPos)

            fractionalSector = sectorPos - sectorNumber

            p = v * (1 - s)
            q = v * (1 - s * fractionalSector)
            t = v * (1 - s * (1 - fractionalSector))

            match sectorNumber:
                case 0:
                    r = v
                    g = t
                    b = p
                case 1:
                    r = q
                    g = v
                    b = p
                case 2:
                    r = p
                    g = v
                    b = t
                case 3:
                    r = p
                    g = q
                    b = v
                case 4:
                    r = t
                    g = p
                    b = v
                case 5:
                    r = v
                    g = p
                    b = q

            # Normalizing each value to 0-255 and saving them
            rgbImage[i][j] = [r * 255, g * 255, b * 255]

    return rgbImage

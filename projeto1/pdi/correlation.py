from PIL import Image
import math
import numpy as np

def correlation(image: Image.Image, kernel: np.ndarray, stride: int):
    image = np.array(image)
    # Convert a 2D kernel into 3D with RGB bands
    kernel = kernel[:, :, None]
    kernel = kernel.repeat(3, axis=2)

    dimensions = {
        "image": np.array([len(image), len(image[0])], dtype=int),
        "kernel": np.array([len(kernel), len(kernel[0])], dtype=float),
    }
    # Calculaating dimensions of the new image with (W - F + 2P) / S + 1 (rounded down to not restrict stride too much)
    dimensions["result"] = (
        np.floor((dimensions["image"] - dimensions["kernel"] + 2 * 0) / stride) + 1
    )

    # Creating a new RGB image with the dimensions calculated previously
    newImage = np.empty(
        (int(dimensions["result"][0]), int(dimensions["result"][1]), 3),
        dtype=np.int16,
    )

    # Calculating offset of the kernel (from the center, how many pixels we have to move)
    offsetL = math.floor(dimensions["kernel"][0] / 2)
    offsetC = math.floor(dimensions["kernel"][1] / 2)
    # This is a bit of a workaround, but it solves the offsetC/offsetL + 1 being out of bounds later on
    if dimensions["kernel"][0] % 2 == 0:
        offsetL = range(-offsetL, offsetL)
    else:
        offsetL = range(-offsetL, offsetL + 1)
    if dimensions["kernel"][1] % 2 == 0:
        offsetC = range(-offsetC, offsetC)
    else:
        offsetC = range(-offsetC, offsetC + 1)

    # We start from the first line and column that allows us to apply the kernel
    i, j = abs(offsetL[0]), abs(offsetC[0])
    line, col = 0, 0

    # While the line/column after applying the kernel is still in bounds of the image
    while i + max(offsetL) < dimensions["image"][0]:
        while j + max(offsetC) < dimensions["image"][1]:
            # Apply the kernel to all pixels and sum them
            newImage[line][col] = np.sum(
                # Stop index is excluded when slicing, hence the +1
                image[
                    i + offsetL[0] : i + offsetL[-1] + 1,
                    j + offsetC[0] : j + offsetC[-1] + 1,
                ]
                * kernel,
                axis=(0, 1),
            )

            # Apply stride and move to the next column
            j += stride
            col += 1

        # Reset to first column that allows us to apply the kernel and the first ever on the new image
        j = abs(offsetC[0])
        col = 0
        # Apply stride and move to the next line
        i += stride
        line += 1

    return newImage

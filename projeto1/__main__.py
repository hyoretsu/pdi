import numpy as np
from pdi.correlation import correlation
from pdi.utils.fix_image import fixImage
from pdi.utils.parse import parseInput
from pdi.utils.sobel_visualization import sobelVisualization
from PIL import Image
from sys import argv

try:
    filterIndex = argv.index("-f")
except:
    print("You must specify a path to the filter you wish to run using \"-f\".")
    exit()

try:
    outputIndex = argv.index("-o")
except:
    print("You must specify a path for the output image using \"-o\".")
    exit()

filterPath = argv[filterIndex + 1]
outputPath = argv[outputIndex + 1]

indicesToRemove = [0, filterIndex, filterIndex + 1, outputIndex, outputIndex + 1]
indicesToRemove.sort()
indicesToRemove.reverse()
for i in indicesToRemove:
    argv.pop(i)

image = Image.open(argv[0])

kernel, stride = parseInput(filterPath)

resultingImage = correlation(image, kernel, stride)

Image.fromarray(fixImage(resultingImage)).save(outputPath)

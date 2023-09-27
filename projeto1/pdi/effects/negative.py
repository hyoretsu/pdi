import numpy as np
from pdi import hsvToRgb, rgbToHsv

def negative(imagem):
    canais = np.array(imagem)

    canais[:, :, 0] = 255 - canais[:, :, 0]
    canais[:, :, 1] = 255 - canais[:, :, 1]
    canais[:, :, 2] = 255 - canais[:, :, 2]

    return canais


def negativeHsv(imagem):
    hsvImagem = rgbToHsv(imagem)
    hsvImagem[:, :, 2] = 1 - hsvImagem[:, :, 2]  # inverte brilho (100%)
    rgbImagem = hsvToRgb(hsvImagem)

    return rgbImagem

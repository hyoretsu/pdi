from color_spaces import hsvToRgb, rgbToHsv

def changeHue(image, value):
    if value < 0 or value > 360:
        raise Exception(f"O valor {value} está fora do intervalo permitido.")

    hsvImage = rgbToHsv(image)
    hsvImage[:, :, 0] = value
    rgbImage = hsvToRgb(hsvImage)

    return rgbImage


def changeSaturation(image, value):
    if value < 0 or value > 1:
        raise Exception(f"O valor {value} está fora do intervalo permitido.")

    hsvImage = rgbToHsv(image)
    hsvImage[:, :, 1] = value
    rgbImage = hsvToRgb(hsvImage)

    return rgbImage

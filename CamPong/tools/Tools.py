import numpy as np
import cv2
import pygame, os
from pygame import *


def translate(window_size, x = None, y = None):
    result = []
    if x is not None:
        xreal = (x * 640) / window_size[0]
        result.append(int(xreal))
    if y is not None:
        yreal = (y * 480) / window_size[1]
        result.append(int(yreal))
    return result


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def createMask(img):
    maskedRGBImage = img

    channel1Min = 27.000;
    channel1Max = 105.000;

    channel2Min = 101.000;
    channel2Max = 255.000;

    channel3Min = 54.000;
    channel3Max = 89.000;

    BW = ((img[:, :, 0] >= channel1Min) & (img[:, :, 0] <= channel1Max)) & (img[:, :, 1] >= channel2Min) & (
                img[:, :, 1] <= channel2Max) & (img[:, :, 2] >= channel3Min) & (img[:, :, 2] <= channel3Max)

    maskedRGBImage[np.tile(~BW[:, :, np.newaxis], (1, 1, 3))] = 0
    return maskedRGBImage

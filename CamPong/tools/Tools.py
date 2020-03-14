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
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)

    channel1Min = 0.259
    channel1Max = 0.508

    channel2Min = 0.578
    channel2Max = 1.000

    channel3Min = 0.000
    channel3Max = 0.961

    hsv_min = 255*np.array([channel1Min, channel2Min, channel3Min])
    hsv_max = 255*np.array([channel1Max, channel2Max, channel3Max])

    mask = cv2.inRange(img_hsv, hsv_min, hsv_max)
    imask = mask>0
    masked_img = np.zeros_like(img, np.uint8)

    masked_img[imask] = img[imask]

    return masked_img

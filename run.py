import sys
import os

from cv2 import cv2
import json

import retinex

data_path = 'data'
# size = 3
img = cv2.imread('timg.jpg')

img_ssr_re = retinex.singleScaleRetinex(img, 15)
img_ssr_cl = retinex.colorRestoration(img, 125.0, 46.0)
img_ssr = 5 * (img_ssr_re * img_ssr_cl + 25)
cv2.imshow('ssr', img_ssr)

img_msrcr = retinex.MSRCR(
    img,
    80,
    5.0,
    25.0,
    125.0,
    46.0,
    0.01,
    0.99
)

# cv2.imshow('MSRCR retinex', img_msrcr)

shape = img.shape
# cv2.imshow('Image', img)

cv2.waitKey()

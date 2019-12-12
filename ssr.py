import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt


def replaceZeroes(data):
    min_nonzero = min(data[np.nonzero(data)])
    data[data == 0] = min_nonzero
    return data


def ssr_c(img, size):
    img_G = replaceZeroes(cv2.GaussianBlur(img, (size, size), 0))
    img = replaceZeroes(img)
    # img_G = cv2.GaussianBlur(img, (size, size), 0)
    log_S = cv2.log(img/255.0)
    g_L = cv2.log(img_G/255.0)
    log_L = cv2.multiply(log_S, g_L)
    log_R = cv2.subtract(log_S, log_L)
    dst_R = cv2.normalize(log_R, None, 0, 255, cv2.NORM_MINMAX)
    R_c = cv2.convertScaleAbs(dst_R)
    return R_c


def singleScaleRetinex(img, size):
    # cv2.imshow('G', cv2.GaussianBlur(img, (size, size), 0))
    b_gray, g_gray, r_gray = cv2.split(img)
    Rb_ssr = ssr_c(b_gray, size)
    Rg_ssr = ssr_c(g_gray, size)
    Rr_ssr = ssr_c(r_gray, size)
    R = cv2.merge([Rb_ssr, Rg_ssr, Rr_ssr])
    return R


if __name__ == '__main__':
    img = 'Rumia_w.jpg'

    src_img = cv2.imread(img)

    result = singleScaleRetinex(src_img, 15)

    source = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    titles = ['Source Image', 'SSR Image']
    images = [source, result]
    for i in range(2):
        plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

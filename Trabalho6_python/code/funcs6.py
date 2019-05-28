# Aluno: Luiz Felipe da S. Coelho
# file name: funcs6.py
# date: 27/05/2019
import numpy as np

if __name__ == '__main__':
    print('Ester aquivo possui apenas funcoes.')


def rgb2ycbcr(rgb):
    """
    Transforms RGB into YCbCr:
    >>>>> ycbcr = rgb2ycbcr(rgb) <<<<<
    where, rgb stands for the rgb array format
           ycbcr stands for the ycbcr array format
    """
    # Defining array shape:
    lx, ly, k = rgb.shape
    # Separating RGB arrays:
    r = rgb[0:, 0:, 0]
    g = rgb[0:, 0:, 1]
    b = rgb[0:, 0:, 2]
    # Creating Y, Cb and Cr arrays:
    y = r*.2126 + g*.7152 + b*.0722
    cb = (b-y)/1.8556
    cr = (r-y)/1.5748
    # I, Q normalization:
    min_y = y.min()
    min_cb = cb.min()  # maior valor Cb
    min_cr = cr.min()  # maior valor Cr
    min_abs = min(min_y, min_cb, min_cr)  # Maior valor de Cb ou Cr
    y_aux = y-min_abs
    cb_aux = cb-min_abs
    cr_aux = cr-min_abs
    max_y = y_aux.max()
    max_cb = cb_aux.max()
    max_cr = cr_aux.max()
    max_abs = max(max_y, max_cb, max_cr)
    norm_fact = 255/max_abs
    y_norm = y_aux*norm_fact
    cb_norm = cb_aux*norm_fact
    cr_norm = cr_aux*norm_fact
    # Reuniting arrays:
    ycbcr = np.zeros([lx, ly, k])
    ycbcr[0:, 0:, 0] = y_norm
    ycbcr[0:, 0:, 1] = cb_norm
    ycbcr[0:, 0:, 2] = cr_norm
    return ycbcr


def subamostragem(imagem, r):
    """
    Function for downsampling an image by a given factor.
    >>>>> imagem_sub = subamostragem(imagem, r) <<<<<
    where, imagem a single matrix containing an image information
           r the downsampling factor
           imagem_sub a single matrix containing imagem downsampled
    """

    lx, ly = imagem.shape
    imagem_sub = np.zeros([int(lx/r), int(ly/r)])
    for i in np.arange(r-1, lx, r):
        for j in np.arange(r-1, ly, r):
            imagem_sub[int(i/r), int(j/r)] = imagem[i, j]
    return imagem_sub


def zoh_interpol(img, r):
    """
    Function for the Zero Order Hold Interpolation.
    >>>>> intr_img = zoh_interpol(img, r) <<<<<
    where, intr_img is the post_interpolation image
           img      is the image to be interpolated
           r        is the interpolation factor.
    """
    # Horizontal repetition:
    img_aux = np.repeat(img, r, axis=0)
    # Vertical repetition:
    intr_img = np.repeat(img_aux, r, axis=1)
    return intr_img


def bi_interpol(img, r):
    """
    Bilinear interpolation function. It implements a bilinear interpolation
    in a determined image with a determined factor.
    >>>>> intr_img = bi_interpol(img, r) <<<<<
    where, intr_img is the post-interpolation image
           img      is the image to be interpolated
           r        is the interpolation factor.
    """
    lx, ly = img.shape
    imagem_aux = np.zeros([lx, ly])
    for i in np.arange(1, lx, 2):
        for j in np.arange(1, ly, 2):
            imagem_aux[i, j] = img[int(i/2), int(j/2)]
    # Bilinear Interpolation:
    # First the horizontal iterations:
    imagem_aux[0, 0:] = imagem_aux[1, 0:]
    imagem_aux[lx-1, 0:] = imagem_aux[lx-2, 0:]
    for i in np.arange(2, lx-2, 2):
        imagem_aux[i, 0:] = .5*imagem_aux[i-1, 0:] + .5*imagem_aux[i+1, 0:]
    # Now the vertical iterations:
    imagem_aux[0:, 0] = imagem_aux[0:, 1]
    imagem_aux[0:, ly-1] = imagem_aux[0:, ly-2]
    for i in np.arange(2, ly-2, 2):
        imagem_aux[0:, i] = .5*imagem_aux[0:, i-1] + .5*imagem_aux[0:, i+1]


def zero_insert(img, r):
    """
    Inserts r zeros to the righ of each column and beneath each line.
    >>>>> img_zero = zero_insert(img, r) <<<<<
    where, img_zero is the image filled with zeros
           img is the original image
           r is the number of zeros between each column/line.
    """

    lx, ly = img.shape
    lx2 = r*lx
    ly2 = r*ly
    img_zero = np.zeros([lx2, ly2])
    for i in np.arange(0, lx2, r):
        for j in np.arange(0, ly2, r):
            img_zero[i, j] = img[i/r, j/r]
    return img_zero

def weighted_mean_interpol(img, r):
    """
    it makes something
    """

    if r = 2:
        img_zero = zero_insert(img, 2)

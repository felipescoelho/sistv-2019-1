# Aluno: Luiz Felipe da S. Coelho
# file name: funcs6.py
# date: 27/05/2019
import numpy as np

if __name__ == '__main__':
    print('Ester aquivo possui apenas funcoes.')


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


def bi_interpol(img, r):
    """
    Bilinear interpolation function. It implements a bilinear interpolation
    in a determined image with a determined factor.
    >>>>> intr_img = bi_interpol(img, r) <<<<<
    where, intr_img is the post-interpolation image
           img      is the image to be interpolated
           r        is the interpolation factor.
    """

    imagem_aux = np.zeros([lx, ly])
    for i in np.arange(1, lx, 2):
        for j in np.arange(1, ly, 2):
            imagem_aux[i, j] = imagem_sub[int(i/2), int(j/2)]
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

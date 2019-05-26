# Aluno: Luiz Felipe da S. Coelho
# File name: funcs5.py
# ----------------------------------------------------------------------------
from numpy import *


if __name__ == "__main__":
    print('Este arquivo contem apenas funcoes.')


def subamostragem(imagem, r):
    """
    Function for downsampling an image by a given factor.
    >>>>> imagem_sub = subamostragem(imagem, r) <<<<<
    where, imagem a single matrix containing an image information
           r the downsampling factor
           imagem_sub a single matrix containing imagem downsampled
    """
    lx, ly = imagem.shape
    imagem_sub = zeros([int(lx/r), int(ly/r)])
    for i in arange(r-1, lx, r):
        for j in arange(r-1, ly, r):
            imagem_sub[int(i/r), int(j/r)] = imagem[i, j]
    return imagem_sub


def subamost_media(imagem, r):
    """
    Function for downsampling an image by a given factor. The resulting pixels
    are given by the mean of a block r x r, centered in a pixel of interest.
    >>>>> img_sub_mean = subamost_media(imagem, r) <<<<<
    where, imagem a single matrix containing an image information
           r the downsampling factor
           img_sub_mean is the resulting matrix.
    """
    lx, ly = imagem.shape
    img_sub_mean = zeros([int(lx/r), int(ly/r)])
    img_aux = zeros([r, r])
    for i in arange(r-1, lx, r):
        for j in arange(r-1, ly, r):
            img_aux = imagem[i - r/2:i + r/2, j - r/2:j + r/2]
            img_sub_mean[int(i/r), int(j/r)] = img_aux.mean()
    return img_sub_mean

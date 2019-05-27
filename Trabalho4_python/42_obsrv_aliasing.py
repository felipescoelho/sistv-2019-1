# Aluno: Luiz Felipe da S. Coelho
# File name: 42_obsrv_aliasing.py
# Data: 10/05/2019

# 4. ALIASING EM IMAGENS DIGITAIS
# 4.1. OBSERVACAO DE ALIASING
# ----------------------------------------------------------------------------
# 1. Tarefa:
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from math import pi

if __name__ == '__main__':
    # 1. Tarefa:
    emezao = 256
    beta = 1
    r = 2
    l = np.arange(-emezao/2 + .5, emezao/2 - .5)
    c = np.arange(-emezao/2 + .5, emezao/2 - .5)
    ll, cc = np.meshgrid(l, c, sparse=True)
    imagem = 0.5*np.cos(beta*pi*(ll**2 + cc**2)/(2*emezao))
    # Normalizando:
    # min = imagem.min()
    # imagem = imagem-min
    # max = imagem.max()
    # imagem = imagem/max

    lx, ly = imagem.shape
    # subamostragem:
    imagem_sub = np.zeros([int(lx/2), int(ly/2)])
    for i in np.arange(1, lx, 2):
        for j in np.arange(1, ly, 2):
            imagem_sub[int(i/2), int(j/2)] = imagem[i, j]

    dpi = 80
    lx2, ly2 = imagem_sub.shape
    lx_inch = float(lx2)/dpi
    ly_inch = float(ly2)/dpi

    plt.figure(figsize=(lx_inch, ly_inch), dpi=dpi)
    fig1 = plt.subplot(111)
    fig1.imshow(imagem_sub, cmap='gray')
    fig1.axis('off')
    plt.savefig('imgs/fig2.eps')

    # 2. Tarefa:
    # Returning the matrix to its original size, spaced by zeros:
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
    print imagem_aux
    # Now the vertical iterations:
    imagem_aux[0:, 0] = imagem_aux[0:, 1]
    imagem_aux[0:, ly-1] = imagem_aux[0:, ly-2]
    for i in np.arange(2, ly-2, 2):
        imagem_aux[0:, i] = .5*imagem_aux[0:, i-1] + .5*imagem_aux[0:, i+1]
    print imagem_aux
    # Normalizando:
    # min = imagem_aux.min()
    # imagem_interpol = imagem_aux-min
    # max = imagem_interpol.max()
    # imagem_interpol = imagem_interpol/max

    dpi = 80
    lx, ly = imagem_aux.shape
    lx_inch = float(lx)/dpi
    ly_inch = float(ly)/dpi

    plt.figure(figsize=(lx_inch, ly_inch), dpi=dpi)
    fig2 = plt.subplot(111)
    fig2.imshow(imagem_aux, cmap='gray')
    fig2.axis('off')
    plt.savefig('imgs/interpol.eps')

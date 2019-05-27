# Aluno: Luiz Felipe da S. Coelho
# File name: 41_gera_znplt.py
# Data: 10/05/2019

# 4. ALIASING EM IMAGENS DIGITAIS
# 4.1. GERACAO DE ZONEPLATES
# ----------------------------------------------------------------------------
# 1. Tarefa:
import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi

if __name__ == '__main__':
    # (a)
    beta_a = 1
    emezao = 256
    l = np.arange(-emezao/2 + 0.5, emezao/2 - 0.5)
    c = np.arange(-emezao/2 + 0.5, emezao/2 - 0.5)
    ll, cc = np.meshgrid(l, c, sparse=True)
    imagem_a = 0.5*np.cos(beta_a*pi*(ll**2 + cc**2)/(2*emezao))
    # (b)
    beta_b1 = .5
    beta_b2 = 2
    imagem_b1 = 0.5*np.cos(beta_b1*pi*(ll**2 + cc**2)/(2*emezao))
    imagem_b2 = 0.5*np.cos(beta_b2*pi*(ll**2 + cc**2)/(2*emezao))

    dpi = 80
    lx_aux, ly_aux = imagem_a.shape
    lx = float(lx_aux)/dpi
    ly = float(ly_aux)/dpi

    plt.figure(1, figsize=(lx, ly), dpi=dpi)
    a = plt.subplot(111)
    a.imshow(imagem_a, cmap='gray')
    a.axis('off')
    plt.savefig('imgs/figura1a.eps')
    plt.figure(2, figsize=(lx, ly), dpi=dpi)
    b1 = plt.subplot(111)
    b1.imshow(imagem_b1, cmap='gray')
    b1.axis('off')
    plt.savefig('imgs/figura1b1.eps')
    plt.figure(3, figsize=(lx, ly), dpi=dpi)
    b2 = plt.subplot(111)
    b2.imshow(imagem_b2, cmap='gray')
    b2.axis('off')
    plt.savefig('imgs/figura1b2')
    plt.show()

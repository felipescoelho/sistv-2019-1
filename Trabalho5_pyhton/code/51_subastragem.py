# Aluno Luiz Felipe da S. Coelho
# file name: 51_subastragem.py
# data: 13/05/2019

# 5. AMOSTRAGEM E SUBASTRAGEM
# 5.1. SUBASTRAGEM:
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
from funcs5 import subamostragem as sb

if __name__ == "__main__":
    # 1. Tarefa:
    zelda_s = plt.imread('imgs/zelda_s.tif')
    lx, ly = zelda_s.shape
    dpi = 80.3
    lx_in = float(lx)/dpi
    ly_in = float(ly)/dpi
    plt.figure(figsize=(lx_in, ly_in))
    zld = plt.subplot(111)
    zld.imshow(zelda_s, cmap='gray')
    zld.axis('off')
    plt.subplots_adjust(wspace=0, hspace=0, top=1, right=1, bottom=0, left=0)
    plt.savefig('imgs/zelda.eps', bbox_inches='tight', pad_inches=0)
    # plt.show()

    # 2. Tarefa:
    lx, ly = zelda_s.shape
    zelda_aux = np.zeros([int(lx/2), int(ly/2)])  # int() arredonda para baixo
    for i in np.arange(1, lx, 2):  # python comeca com 0 != do MATLAB
        for j in np.arange(1, ly, 2):
            zelda_aux[int(i/2), int(j/2)] = zelda_s[i, j]
    lx_sub, ly_sub = zelda_aux.shape

    dpi = 80.3
    lx_sub_in = float(lx_sub)/dpi
    ly_sub_in = float(ly_sub)/dpi

    # 3. Tarefa:
    plt.subplots(figsize=(lx_sub_in, ly_sub_in))
    sub = plt.subplot(111)
    sub.imshow(zelda_aux, cmap='gray')
    sub.axis('off')
    plt.subplots_adjust(wspace=0, hspace=0, top=1, right=1, bottom=0, left=0)
    plt.savefig('imgs/zelda_sub.eps', bbox_inches='tight', pad_inches=0)

    # 4. Tarefa:
    r = 32
    zelda_sub2 = sb(zelda_s, r)

    # 5. Tarefa:
    zelda_sb4 = sb(zelda_s, 4)
    zelda_sb8 = sb(zelda_s, 8)
    zelda_sb16 = sb(zelda_s, 16)
    zelda_sb32 = sb(zelda_s, 32)
    # plot:
    plt.figure()
    sb4 = plt.subplot(221)
    sb4.imshow(zelda_sb4, cmap='gray')
    sb4.axis('off')
    sb4.set_title('r = 4')
    sb8 = plt.subplot(222)
    sb8.imshow(zelda_sb8, cmap='gray')
    sb8.axis('off')
    sb8.set_title('r = 8')
    sb16 = plt.subplot(223)
    sb16.imshow(zelda_sb16, cmap='gray')
    sb16.axis('off')
    sb16.set_title('r = 16')
    sb32 = plt.subplot(224)
    sb32.imshow(zelda_sb32, cmap='gray')
    sb32.axis('off')
    sb32.set_title('r = 32')
    plt.savefig('imgs/zelda_subs.eps')
    plt.show()

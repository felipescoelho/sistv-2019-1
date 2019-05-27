# Aluno Luiz Felipe da S. Coelho
# file name: 52_contin.py
# data: 14/05/2019

# 5. AMOSTRAGEM E SUBASTRAGEM
# 5.2. SUBASTRAGEM CONTINUACAO:
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from funcs5 import subamost_media as sbm
from funcs5 import msk_dwnsp as msksb

if __name__ == "__main__":
    # 1. Tarefa:
    zelda_s = plt.imread('../imgs/zelda_s.tif')

    # using the suggested method

    zelda_msksb4 = msksb(zelda_s, 4)
    zelda_msksb8 = msksb(zelda_s, 8)
    zelda_msksb16 = msksb(zelda_s, 16)
    zelda_msksb32 = msksb(zelda_s, 32)

    plt.figure()
    sbm4 = plt.subplot(221)
    sbm4.imshow(zelda_msksb4, cmap='gray')
    sbm4.axis('off')
    sbm4.set_title('r = 4')
    sbm8 = plt.subplot(222)
    sbm8.imshow(zelda_msksb8, cmap='gray')
    sbm8.axis('off')
    sbm8.set_title('r = 8')
    sbm16 = plt.subplot(223)
    sbm16.imshow(zelda_msksb16, cmap='gray')
    sbm16.axis('off')
    sbm16.set_title('r = 16')
    sbm32 = plt.subplot(224)
    sbm32.imshow(zelda_msksb32, cmap='gray')
    sbm32.axis('off')
    sbm32.set_title('r = 32')
    plt.savefig('../imgs/zelda_mskdwn.eps')
    print(zelda_msksb8.shape, zelda_s.shape)

    # using the mean method:
    zelda_sbm4 = sbm(zelda_s, 4)
    zelda_sbm8 = sbm(zelda_s, 8)
    zelda_sbm16 = sbm(zelda_s, 16)
    zelda_sbm32 = sbm(zelda_s, 32)

    plt.figure()
    sbm4 = plt.subplot(221)
    sbm4.imshow(zelda_sbm4, cmap='gray')
    sbm4.axis('off')
    sbm4.set_title('r = 4')
    sbm8 = plt.subplot(222)
    sbm8.imshow(zelda_sbm8, cmap='gray')
    sbm8.axis('off')
    sbm8.set_title('r = 8')
    sbm16 = plt.subplot(223)
    sbm16.imshow(zelda_sbm16, cmap='gray')
    sbm16.axis('off')
    sbm16.set_title('r = 16')
    sbm32 = plt.subplot(224)
    sbm32.imshow(zelda_sbm32, cmap='gray')
    sbm32.axis('off')
    sbm32.set_title('r = 32')
    plt.savefig('../imgs/zelda_subsm.eps')
    plt.show()

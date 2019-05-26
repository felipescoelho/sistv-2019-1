# Aluno Luiz Felipe da S. Coelho
# file name: 51_subastragem.py
# data: 14/05/2019

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

    # Primeira subamostragem: r = 2
    zelda_sb2 = np.zeros([int(lx/2), int(ly/2)])
    for i in np.arange(1, lx, 2):
        for j in np.arange(1, ly, 2):
            zelda_sb2[int(i/2), int(j/2)] = zelda_s[i, j]
    lx_sb2, ly_sb2 = zelda_sb2.shape

    # Segunda subamostragem: r = 4
    zelda_sb4 = np.zeros([int(lx_sb2/2), int(ly_sb2/2)])
    for i in np.arange(1, lx_sb2, 2):
        for j in np.arange(1, ly_sb2, 2):
            zelda_sb4[int(i/2), int(j/2)] = zelda_sb2[i, j]
    lx_sb4, ly_sb4 = zelda_sb4.shape

    # Terceira subamostragem: r = 8
    zelda_sb8 = np.zeros([int(lx_sb4/2), int(ly_sb4/2)])
    for i in np.arange(1, lx_sb4, 2):
        for j in np.arange(1, ly_sb4, 2):
            zelda_sb8[int(i/2), int(j/2)] = zelda_sb4[i, j]
    lx_sb8, ly_sb8 = zelda_sb8.shape

    # Quarta subamostragem: r = 16
    zelda_sb16 = np.zeros([int(lx_sb8/2), int(ly_sb8/2)])
    for i in np.arange(1, lx_sb8, 2):
        for j in np.arange(1, ly_sb8, 2):
            zelda_sb16[int(i/2), int(j/2)] = zelda_sb8[i, j]
    lx_sb16, ly_sb16 = zelda_sb16.shape

    # Quinta subamostragem: r = 32
    zelda_sb32 = np.zeros([int(lx_sb16/2), int(ly_sb16/2)])
    for i in np.arange(1, lx_sb16, 2):
        for j in np.arange(1, ly_sb16, 2):
            zelda_sb32[int(i/2), int(j/2)] = zelda_sb16[i, j]
    lx_sb32, ly_sb32 = zelda_sb32.shape

    # Subamostragem pela funcao:
    zelda_sub4 = sb(zelda_s, 4)
    zelda_sub8 = sb(zelda_s, 8)
    zelda_sub16 = sb(zelda_s, 16)
    zelda_sub32 = sb(zelda_s, 32)

    # Diferencas:
    sb4 = zelda_sb4 - zelda_sub4
    sb8 = zelda_sb8 - zelda_sub8
    sb16 = zelda_sb16 - zelda_sub16
    sb32 = zelda_sb32 - zelda_sub32

    if 0 == sb4.all() and 0 == sb8.all() and 0 == sb16.all() and 0 == sb32.all():
        print('Certo! Todos sao iguais.')
    else:
        print('Errado! Nem todos sao iguais.')

# Aluno: Luiz Felipe da S. Coelho
# File name: 33_visual_cor.py
# Data: 80/05/2019

# 3. INFORMACAO DE COR:
# 3.3. VISUALIZACAO DE ESPACOS DE CORES:
# ----------------------------------------------------------------------------
import numpy as np
from math import pi, cos, sin
import matplotlib.pyplot as plt
import imgconvfunc

if __name__ == '__main__':
    # 1 - Tarefa:
    a = np.arange(256)
    b = np.zeros([100, 256], np.int16)
    red = np.zeros([100, 512, 3], np.int16)
    green = np.zeros([100, 512, 3], np.int16)
    blue = np.zeros([100, 512, 3], np.int16)

    for i in range(100):
        b[i, 0:] = a
    c = b.repeat(2, axis=1)
    rgb = np.zeros([100, 512, 3])
    for i in range(3):
        rgb[0:, 0:, i] = c

    # 2 - Tarefa:
    red[0:, 0:, 0] = c
    green[0:, 0:, 1] = c
    blue[0:, 0:, 2] = c

    plt.figure(figsize=(14.5, 2.5))
    r = plt.subplot(131)
    r.imshow(red)
    r.axis('off')
    r.set_title('R')
    g = plt.subplot(132)
    g.imshow(green)
    g.axis('off')
    g.set_title('G')
    b = plt.subplot(133)
    b.imshow(blue)
    b.axis('off')
    b.set_title('B')
    plt.savefig('imgs/RGB.eps')

    # 5 - Tarefa:

    y = np.ones([100, 512])

    y = 128*y
    # Assumming all the possible values for I and Q:

    yiq_y = np.zeros([100, 512, 3])
    yiq_i = np.zeros([100, 512, 3])
    yiq_q = np.zeros([100, 512, 3])
    yiq_i[0:, 0:, 0] = y
    yiq_i[0:, 0:, 1] = c
    yiq_q[0:, 0:, 0] = y
    yiq_q[0:, 0:, 2] = c
    yiq_y[0:, 0:, 0] = y
    yiq_y[0:, 0:, 1] = c
    yiq_y[0:, 0:, 2] = c
    yiq_i_rgb = imgconvfunc.yiq2rgb(yiq_i)  # (y, c, 0)
    yiq_q_rgb = imgconvfunc.yiq2rgb(yiq_q)  # (y, 0, c)
    yiq_y_rgb = imgconvfunc.yiq2rgb(yiq_y)  # (y, c, c)

    plt.figure(figsize=(14.5, 2.5))
    r = plt.subplot(131)
    r.imshow(yiq_y_rgb/255)
    r.axis('off')
    r.set_title('Y')
    g = plt.subplot(132)
    g.imshow(yiq_i_rgb/255)
    g.axis('off')
    g.set_title('I')
    b = plt.subplot(133)
    b.imshow(yiq_q_rgb/255)
    b.axis('off')
    b.set_title('Q')
    plt.savefig('imgs/YIQ.eps')

    ycbcr_cb_rgb = imgconvfunc.ycbcr2rgb(yiq_i)  # (y, c, 0)
    ycbcr_cr_rgb = imgconvfunc.ycbcr2rgb(yiq_q)  # (y, 0, c)
    ycbcr_y_rgb = imgconvfunc.ycbcr2rgb(yiq_y)  # (y, c, c)

    plt.figure(figsize=(14.5, 2.5))
    r = plt.subplot(131)
    r.imshow(ycbcr_y_rgb/255)
    r.axis('off')
    r.set_title('Y')
    g = plt.subplot(132)
    g.imshow(ycbcr_cb_rgb/255)
    g.axis('off')
    g.set_title('Cb')
    b = plt.subplot(133)
    b.imshow(ycbcr_cr_rgb/255)
    b.axis('off')
    b.set_title('Cr')
    plt.savefig('imgs/YCbCr.eps')

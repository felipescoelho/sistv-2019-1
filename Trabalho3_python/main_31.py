# Aluno: Luiz Felipe da S. Coelho, lfscoelho@ieee.org
# Data: 04/05/2019

# file name: main_31.py

# reference: http://scipy-lectures.org/advanced/image_processing/

# 3. INFORMACAO DE COR
# 3.1. ESPACOS DE CORES
# ----------------------------------------------------------------------------
# 1 - Tarefa: Para cada uma das imagens CAPE, MANDRILL, CLOWN e TREES, fazer o
# seguinte:

# (a) Carrega-las e vizualiza-las:
import numpy as np
import matplotlib.pyplot as plt
import imgconvfunc
import imgplotfunc

# Figure reading:
cape = plt.imread('./imgs/cape.tif')
mandrill = plt.imread('./imgs/mandrill.tif')
clown = plt.imread('./imgs/clown.tif')
trees = plt.imread('./imgs/trees.tif')


# (b) Transform from RGB to YIQ and YCbCr:
# RGB -> YIQ transformation:
cape_yiq = imgconvfunc.rgb2yiq(cape)
mandrill_yiq = imgconvfunc.rgb2yiq(mandrill)
clown_yiq = imgconvfunc.rgb2yiq(clown)
trees_yiq = imgconvfunc.rgb2yiq(trees)

# RGB -> YCbCr transformation:
cape_ycbcr = imgconvfunc.rgb2ycbcr(cape)
mandrill_ycbcr = imgconvfunc.rgb2ycbcr(mandrill)
clown_ycbcr = imgconvfunc.rgb2ycbcr(clown)
trees_ycbcr = imgconvfunc.rgb2ycbcr(trees)


# (c) Mostre as matrizes de R, G e B juntamente com as de Y, I e Q e as de Y,
# Cb e Cr, como se cada uma fosse uma imagem separada em niveis de cinza.

imgplotfunc.rgbplot(cape, 'imgs/cape_rgb.eps')

imgplotfunc.rgbplot(mandrill, 'imgs/mandrill_rgb.eps')

imgplotfunc.rgbplot(clown, 'imgs/clown_rgb.eps')

imgplotfunc.rgbplot(trees, 'imgs/trees_rgb.eps')

imgplotfunc.yiqplot(cape_yiq/255, 'imgs/cape_yiq.eps')

imgplotfunc.yiqplot(mandrill_yiq/255, 'imgs/mandrill_yiq.eps')

imgplotfunc.yiqplot(clown_yiq/255, 'imgs/clown_yiq.eps')

imgplotfunc.yiqplot(trees_yiq/255, 'imgs/trees_yiq.eps')

imgplotfunc.ycbcrplot(cape_ycbcr/255, 'imgs/cape_ycbcr.eps')

imgplotfunc.ycbcrplot(mandrill_ycbcr/255, 'imgs/mandrill_ycbcr.eps')

imgplotfunc.ycbcrplot(clown_ycbcr/255, 'imgs/clown_ycbcr.eps')

imgplotfunc.ycbcrplot(trees_ycbcr/255, 'imgs/trees_ycbcr.eps')

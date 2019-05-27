# Aluno: Luiz Felipe da S. Coelho
# file name: 61_img_interpol.py
# data: 27/05/2019

# 6. INTERPOLACAO DE IMAGENS
# 6.1. INTERPOLACAO "ZOH"
# ----------------------------------------------------------------------------
# 1. TAREFA:

import matplotlib.pyplot as plt
from funcs6 import subamostragem as sb
from funcs6 import zoh_interpol as zoh
from funcs6 import rgb2ycbcr

img = plt.imread('../imgs/mandrill.tif')
# Converting to YCbCr:
img_aux = rgb2ycbcr(img)
img_y = img_aux[0:, 0:, 0]
# downsampling
img_sb2 = sb(img_y, 2)
img_sb4 = sb(img_y, 4)
img_sb8 = sb(img_y, 8)
# interpolation
img_int2 = zoh(img_sb2, 2)
img_int4 = zoh(img_sb4, 4)
img_int8 = zoh(img_sb8, 8)
# plotting
dpi = 80.3
# Downsampling factor 2:
lx_int2, ly_int2 = img_int2.shape
lx_int2_inch = float(lx_int2)/dpi
ly_int2_inch = float(ly_int2)/dpi
plt.figure(figsize=(lx_int2_inch, ly_int2_inch))
int2 = plt.subplot(111)
int2.imshow(img_int2, cmap='gray')
plt.subplots_adjust(wspace=0, hspace=0, top=1, right=1, bottom=0, left=0)
plt.savefig('../imgs/mandrill_sub2.eps', bbox_inches='tight', pad_inches=0)
int2.axis('off')
# Downsampling factor 4:
lx_int4, ly_int4 = img_int4.shape
lx_int4_inch = float(lx_int4)/dpi
ly_int4_inch = float(ly_int4)/dpi
plt.figure(figsize=(lx_int4_inch, ly_int4_inch))
int4 = plt.subplot(111)
int4.imshow(img_int4, cmap='gray')
plt.subplots_adjust(wspace=0, hspace=0, top=1, right=1, bottom=0, left=0)
plt.savefig('../imgs/mandrill_sub4.eps', bbox_inches='tight', pad_inches=0)
int4.axis('off')
# Downsampling factor 8:
lx_int8, ly_int8 = img_int8.shape
lx_int8_inch = float(lx_int8)/dpi
ly_int8_inch = float(ly_int8)/dpi
plt.figure(figsize=(lx_int8_inch, ly_int8_inch))
int8 = plt.subplot(111)
int8.imshow(img_int8, cmap='gray')
plt.subplots_adjust(wspace=0, hspace=0, top=1, right=1, bottom=0, left=0)
plt.savefig('../imgs/mandrill_sub8.eps', bbox_inches='tight', pad_inches=0)
int8.axis('off')

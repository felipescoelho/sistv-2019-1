# Aluno: Luiz Felipe da S. Coelho
# file name: 63_weightedmean_interpol.py
# Date: 28/05/2019

# 6. INTERPOLACAO
# 6.3. INTERPOLACAO USANDO MEDIAS PONDERADAS
# ----------------------------------------------------------------------------
# 1 - Tarefa:
import matplotlib.pyplot as plt
from funcs6 import subamostragem as submos
from funcs6 import zero_insert as zins
from funcs6 import rgb2ycbcr
from funcs6 import subamostragem as sb

lena_256 = plt.imread('../imgs/lena_256.tif')
lena_dwn = submos(lena_256, 2)

plt.figure()
lena_orig = plt.subplot(131)
lena_orig.imshow(lena_256, cmap='gray')
lena_orig.axis('off')
lena_sub = plt.subplot(132)
lena_sub.imshow(lena_dwn, cmap='gray')
lena_sub.axis('off')


# 2 - Tarefa:
lena_zfill = zins(lena_dwn, 2)
lena_int = plt.subplot(133)
lena_int.imshow(lena_zfill, cmap='gray')
lena_int.axis('off')
plt.show()

# 4 - Tarefa:
mandrill = plt.imread('../imgs/mandrill.tif')
# Converting to YCbCr:
img_aux = rgb2ycbcr(mandrill)
img_y = img_aux[0:, 0:, 0]
# downsampling
img_sb2 = sb(img_y, 2)
img_sb4 = sb(img_y, 4)
img_sb8 = sb(img_y, 8)
# zero filling:
img_z2 = zins(img_sb2, 2)
img_z4 = zins(img_sb4, 4)
img_z8 = zins(img_sb8, 8)

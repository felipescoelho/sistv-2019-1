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
from funcs6 import weighted_mean_interpol as wmi

lena_256 = plt.imread('../imgs/lena_256.tif')
lena_dwn = submos(lena_256, 2)

plt.figure(num='Lena')
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
# plotting the zerofilled
plt.figure(num='Zero filled images')
plt_z2 = plt.subplot(131)
plt_z2.imshow(img_z2, cmap='gray')
plt_z2.axis('off')
plt_z2.set_title('r = 2')
plt_z4 = plt.subplot(132)
plt_z4.imshow(img_z4, cmap='gray')
plt_z4.axis('off')
plt_z4.set_title('r = 4')
plt_z8 = plt.subplot(133)
plt_z8.imshow(img_z8, cmap='gray')
plt_z8.axis('off')
plt_z8.set_title('r = 8')

# 3x3 interpolation:
img_int2 = wmi(img_sb2, 2, 1)
img_int4 = wmi(img_sb4, 4, 1)
img_int8 = wmi(img_sb8, 8, 1)
# plotting 3x3 interpolation
plt.figure(num='3x3 Interpolation')
plt_int2 = plt.subplot(131)
plt_int2.imshow(img_int2, cmap='gray')
plt_int2.axis('off')
plt_int2.set_title('r = 2')
plt_int4 = plt.subplot(132)
plt_int4.imshow(img_int4, cmap='gray')
plt_int4.axis('off')
plt_int4.set_title('r = 4')
plt_int8 = plt.subplot(133)
plt_int8.imshow(img_int8, cmap='gray')
plt_int8.axis('off')
plt_int8.set_title('r = 8')

# 7x7 interpolation:
img_int2_7x7 = wmi(img_sb2, 2, 2)
img_int4_7x7 = wmi(img_sb4, 4, 2)
img_int8_7x7 = wmi(img_sb8, 8, 2)
print(img_int2_7x7[33:40, 33:40])
# plotting 7x7 interpolation
plt.figure(num='7x7 Interpolation')
plt_int2_7x7 = plt.subplot(131)
plt_int2_7x7.imshow(img_int2_7x7, cmap='gray')
plt_int2_7x7.axis('off')
plt_int2_7x7.set_title('r = 2')
plt_int4_7x7 = plt.subplot(132)
plt_int4_7x7.imshow(img_int4_7x7, cmap='gray')
plt_int4_7x7.axis('off')
plt_int4_7x7.set_title('r = 4')
plt_int8_7x7 = plt.subplot(133)
plt_int8_7x7.imshow(img_int8_7x7, cmap='gray')
plt_int8_7x7.axis('off')
plt_int8_7x7.set_title('r = 8')
plt.show()

from numpy import *
import matplotlib.pyplot as plt

imagem = plt.imread('imgs/zelda_s.tif')

lx, ly = imagem.shape

r = 2
img_sub_mean = zeros([int(lx/r), int(ly/r)])
print img_sub_mean.shape
img_aux = zeros([r, r])
for i in arange(r-1, lx, r):
    for j in arange(r-1, ly, r):
        img_aux = imagem[i - r/2:i + r/2, j - r/2:j + r/2]
        img_sub_mean[int(i/r), int(j/r)] = img_aux.mean()
plt.figure()
plt.imshow(img_sub_mean, cmap='gray')
plt.show()

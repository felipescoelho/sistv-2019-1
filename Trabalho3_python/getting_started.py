# Basic image manipulation and processing using the core scientific modules
# NumPy and SciPy. Some of the operations covered by this tutorial may be
# useful for other kinds of multidimensional array processing than image
# processing. In particular, the submodule scipy.ndimage provides functions
# operating on n-dimensional NumPy arrays.

# imports needed:
from scipy import misc
import imageio as imageio
import numpy as np


# Opening and writing to image files:
# ----------------------------------------------------------------------------
# writing an array to a file:
f = misc.face()
imageio.imwrite('face.png', f)

import matplotlib.pyplot as plt
plt.figure(1)
plt.imshow(f)


# creating a numpy array from an image file:
face = imageio.imread('face.png')
type(face)
face.shape, face.dtype
# dtype is uint8 for 8-bit images (0-255)

# opening raw files (camera, 3-D images)
face.tofile('face.raw') # Create raw file
face_from_raw = np.fromfile('face.raw', dtype=np.uint8)
face_from_raw.shape
face_from_raw.shape = (768, 1024, 3)
# Need to know the shape and dtype of the image (how to separate data bytes).

# For large data, use np.memmap for memory mapping
face_memmap = np.memmap('face.raw', dtype=np.uint8, shape=(768, 1024, 3))

# (data are read from the file, and not loaded into memory)
# Working on a list of image files
for i in range(10):
    im = np.random.randint(0, 256, 10000).reshape((100, 100))
    imageio.imwrite('random_%02d.png' %i, im)
from glob import glob
filelist = glob('random*.png')
filelist.sort()


# Displaying images:
# ----------------------------------------------------------------------------
# Use matplotlib and imshow to display an image inside a matplotlib figure:
f = misc.face(gray=True)    # retrieve a grayscale image
import matplotlib.pyplot as plt
plt.figure(2)
plt.imshow(f, cmap=plt.cm.gray)

# Increase contrast by setting min and max values:
plt.figure(3)
plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=200)
# remover axes and ticks
plt.axis('off')


# Draw contour lines:
plt.figure(4)
plt.contour(f, [50, 200])
plt.axis('off')


# For smooth intensity variations, use interpolation='bilinear'.
# For fine inspection of intensity variations, use 'interpolation=nearest'

plt.figure(5)
plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')

plt.figure(6)
plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')

# plt.show()


# Basic manipulations:
# ----------------------------------------------------------------------------
# Images are arrays: use the whole numpy machinery
face = misc.face(gray=True)
pixel = face[0, 40]
bloco = face[10:13, 20:23] # slicing
print 'face[0, 40]', pixel, '\n'
print 'face[10:13, 20:23]', '\n', bloco, '\n'
face[100:120] = 255

lx, ly = face.shape
print face.shape
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4 # mask
face[mask] = 0
#fancy indexing
face[range(400), range(400)] = 255
plt.figure(7)
plt.imshow(face)
plt.axis('off')

#plt.show()


# Statistical information
face = misc.face(gray=True)
print 'face.mean()', face.mean(), '\n'
print '(face.max(), face.min())', '(', face.max(),',', face.min(), ')', '\n'


# Generical transformations
face = misc.face(gray=True)
lx, ly = face.shape
# cropping
crop_face = face[lx // 4: - lx // 4, ly // 4: - ly // 4]
# up < - > down flip
flip_ud_face = np.flipud(face)
# rotation
rotate_face = ndimage.rotate(face, 45)
rotate_face_noreshape = ndimage.rotate(face, 45, reshape=False)


# Image filtering
# ----------------------------------------------------------------------------
# LOCAL FILTERS: replace the value of pixels by a function of the values of
# neighboring pixels.
# Neighbourhood: square (choose size), disk, or more complicated structuring
# element.

# Blurring/smoothing:
# Gaussian filter from scipy.ndimage:
from scipy import misc
face = misc.face(gray=True)
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)

# uniform filter
local_mean = ndimage.uniform_filter(face, size=11)

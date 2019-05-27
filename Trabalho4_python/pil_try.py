from PIL import Image
import numpy

w, h = 1024, 768  # this is the size image we want to create
img = numpy.empty((w, h), numpy.uint32)
img.shape = h, w  # set the array shape to our image shape; yes i know it seems backwards, but it's not!

img[0, 0] = 0x800000FF
img[10:21, 512:1024] = 0xFFFF0000
img[21:401, 758:769] = 0xFFFF0000
img[401:411, 512:769] = 0xFFFF0000

pilImage = Image.frombuffer('RGBA', (w, h), img, 'raw', 'RGBA', 0, 1)
pilImage.save('my.png')

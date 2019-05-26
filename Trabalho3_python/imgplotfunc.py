# File name: imgplotfunc.py
# Functions to plot and save the RGB, YIQ and YCbCr images
import matplotlib.pyplot as plt


def rgbplot(arr, fname):
    '''
    Plots the RGB and the orginal images in one figure.
    >>>>> rgbplot(arr, fname) <<<<<
    where, arr is the array that defines the RGB image
           fname is the file name for the figure to be saved in
    '''

    fig = plt.figure(figsize=(40, 14))
    fig.suptitle('Imagens RGB e Imagem Original', fontsize=60)

    r = plt.subplot(141)
    r.imshow(arr[0:, 0:, 0], cmap=plt.cm.gray)
    r.axis('off')
    r.set_title('R', fontsize=50)

    g = plt.subplot(142)
    g.imshow(arr[0:, 0:, 1], cmap=plt.cm.gray)
    g.axis('off')
    g.set_title('G', fontsize=50)

    b = plt.subplot(143)
    b.imshow(arr[0:, 0:, 2], cmap=plt.cm.gray)
    b.axis('off')
    b.set_title('B', fontsize=50)

    orig = plt.subplot(144)
    orig.imshow(arr)
    orig.axis('off')
    orig.set_title('Original', fontsize=50)

    plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01, left=0.05,
                        right=0.99)
    plt.savefig(fname)
    return


def yiqplot(arr, fname):
    '''
    Plots the YIQ images in one figure.
    >>>>> rgbplot(arr, fname) <<<<<
    where, arr is the array that defines YIQ the image
           fname is the file name for the figure to be saved in
    '''

    fig = plt.figure(figsize=(40, 17.5))
    fig.suptitle('Imagens Y, I e Q, em cinza', fontsize=60)

    y = plt.subplot(131)
    y.imshow(arr[0:, 0:, 0], cmap=plt.cm.gray)
    y.axis('off')
    y.set_title('Y', fontsize=50)

    i_arr = plt.subplot(132)
    i_arr.imshow(arr[0:, 0:, 1], cmap=plt.cm.gray)
    i_arr.axis('off')
    i_arr.set_title('I', fontsize=50)

    q = plt.subplot(133)
    q.imshow(arr[0:, 0:, 2], cmap=plt.cm.gray)
    q.axis('off')
    q.set_title('Q', fontsize=50)

    plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01, left=0.05,
                        right=0.99)
    plt.savefig(fname)
    return


def ycbcrplot(arr, fname):
    '''
    Plots the YCbCr images in one figure.
    >>>>> rgbplot(arr, fname) <<<<<
    where, arr is the array that defines the YCbCr image
           fname is the file name for the figure to be saved in
    '''

    fig = plt.figure(figsize=(40, 17.5))
    fig.suptitle('Imagens Y, Cb e Cr, em cinza', fontsize=60)

    y = plt.subplot(131)
    y.imshow(arr[0:, 0:, 0], cmap=plt.cm.gray)
    y.axis('off')
    y.set_title('Y', fontsize=50)

    cb = plt.subplot(132)
    cb.imshow(arr[0:, 0:, 1], cmap=plt.cm.gray)
    cb.axis('off')
    cb.set_title('Cb', fontsize=50)

    cr = plt.subplot(133)
    cr.imshow(arr[0:, 0:, 2], cmap=plt.cm.gray)
    cr.axis('off')
    cr.set_title('Cr', fontsize=50)

    plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01, left=0.05,
                        right=0.99)
    plt.savefig(fname)
    return

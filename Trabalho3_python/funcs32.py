# File name: funcs32.py
# Date: 07/05/2019
# Functions applied in the section 3.2. of Lista 1:
from numpy import *
import matplotlib.pyplot as plt
import imgconvfunc

if __name__ == '__main__':
    print 'Rode o script resp_sist_32.py'


def hist_y(I_file):
    '''
    Fuction that recieves an image I and returns its luminescence's histogram
    >>>>> hist_y(I_file) <<<<<
    where, I_file is the image's file.
    '''
    im_rgb = plt.imread(I_file)  # image read into a rgb array
    # Separating the array in R, G and B:
    name = I_file[5:-4]  # Getting the file name, without the codec
    dirr = I_file[0:5]  # Getting the directory's name
    fname = dirr + 'histo_y_' + name + '.eps'
    r = im_rgb[0:, 0:, 0]
    g = im_rgb[0:, 0:, 1]
    b = im_rgb[0:, 0:, 2]
    # Calculating the image's luminescence, according to itu's standard for
    # digital image:
    y = r*.2126 + g*.7152 + b*.0722
    # Calculating the histogram, according to 'Dica':
    # Assuming that the matrix y has only integer numbers, the histogram can be
    # calculated as the following:
    y_vect = y.flatten()
    len, = y_vect.shape
    histo = zeros([256], int)
    for i in range(0, len):
        for j in range(0, 255):
            if int(y_vect[i]) == j:
                histo[j] = histo[j] + 1
    plt.figure(1)
    (markers, stemline, baseline) = plt.stem(histo, markerfmt=' ',
                                             basefmt='C3--')
    plt.setp(stemline, linewidth=6)
    plt.savefig(fname)
    return


def hist(I_file):
    '''
    Function that recieves a RGB image I and returns it's components' histogram
    >>>>> saida_rgb, saida_yiq, saida_ycbcr = hist(I_file) <<<<<
    where, I_file is the image's file
           saida_rgb is the r, g and b matrix histograms
           saida_yiq is the y, i and q matrix histograms
           saida_ycbcr is the y, cb and cr matrix histograms.
    '''
    im_rgb = plt.imread(I_file)  # image read into a rgb array
    im_yiq = imgconvfunc.rgb2yiq(im_rgb)  # using the transformation functions
    im_ycbcr = imgconvfunc.rgb2ycbcr(im_rgb)
    name = I_file[5:-4]  # Getting the file name, without the codec
    dirr = I_file[0:5]
    rgb = 'R', 'G', 'B'
    yiq = 'Yiq', 'I', 'Q'
    ycbcr = 'Y', 'Cb', 'Cr'
    # RGB loop:
    saida_rgb = zeros([256, 3], int)
    for i in range(3):
        val = im_rgb[0:, 0:, i].flatten()
        len, = val.shape
        histo = zeros([256], int)
        for j in range(0, len):
            for k in range(0, 255):
                if int(val[j]) == k:
                    histo[k] = histo[k] + 1
        saida_rgb[0:, i] = histo
        fname = dirr + name + '_' + 'histo' + '_' + rgb[i] + '.eps'
        plt.figure(i)
        (markers, stemline, baseline) = plt.stem(histo/len, markerfmt=' ',
                                                 basefmt='C3--')
        plt.setp(stemline, linewidth=6)
        plt.savefig(fname)
    # YIQ loop:
    saida_yiq = zeros([256, 3], int)
    for i in range(3):
        val = im_yiq[0:, 0:, i].flatten()
        len, = val.shape
        histo = zeros([256], int)
        for j in range(0, len):
            for k in range(0, 255):
                if int(val[j]) == k:
                    histo[k] = histo[k] + 1
        saida_yiq[0:, i] = histo
        fname = dirr + name + '_' + 'histo' + '_' + yiq[i] + '.eps'
        plt.figure(i)
        (markers, stemline, baseline) = plt.stem(histo/len, markerfmt=' ',
                                                 basefmt='C3--')
        plt.setp(stemline, linewidth=6)
        plt.savefig(fname)
    # YCbCr loop:
    saida_ycbcr = zeros([256, 3], int)
    for i in range(3):
        val = im_ycbcr[0:, 0:, i].flatten()
        len, = val.shape
        histo = zeros([256], int)
        for j in range(0, len):
            for k in range(0, 255):
                if int(val[j]) == k:
                    histo[k] = histo[k] + 1
        saida_ycbcr[0:, i] = histo
        fname = dirr + name + '_' + 'histo' + '_' + ycbcr[i] + '.eps'
        plt.figure(i)
        (markers, stemline, baseline) = plt.stem(histo/len, markerfmt=' ',
                                                 basefmt='C3--')
        plt.setp(stemline, linewidth=6)
        plt.savefig(fname)
    return saida_rgb, saida_yiq, saida_ycbcr


def entropy(entry):
    """
    Calculates the entropy of a given histogram
    >>>>> y = entropy(entry) <<<<<
    where, entry is the input histogram
           y is the calculated entropy foe each value of entry.
    """
    len, lvl = entry.shape
    ntrp = zeros([3], float)
    # Separating each colour level:
    for i in range(3):
        mat = entry[0:, i]
        for j in range(len):
            pk = mat[j]/float32(len)
            print pk
            if pk != 0:
                ntrp[i] = ntrp[i] + pk*(log2(1/pk))
    return ntrp

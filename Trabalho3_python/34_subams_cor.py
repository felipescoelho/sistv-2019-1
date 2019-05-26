# Aluno: Luiz Felipe da S. Coelho
# File name: 34_subams_cor.py
# Data 09/05/2019

# 3. INFORMACAO DE COR:
# 3.4. SUBAMOSTRAGEM DE COR:
# ----------------------------------------------------------------------------
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
from imgconvfunc import rgb2ycbcr as transf, ycbcr2rgb as detrans

if __name__ == '__main__':
    # 1. Tarefa:
    # Image converting:
    cape = plt.imread('imgs/cape.tif')
    mandrill = plt.imread('imgs/mandrill.tif')
    clown = plt.imread('imgs/clown.tif')
    trees = plt.imread('imgs/trees.tif')
    cape_trns = transf(cape)
    mandrill_trns = transf(mandrill)
    clown_trns = transf(clown)
    trees_trns = transf(trees)
    # Filter:
    filter = np.ones([3, 3])/9
    # Y - filtering:
    y_cape_filt = sig.convolve2d(cape[0:, 0:, 0], filter, boundary='symm',
                                 mode='same')
    y_mandrill_filt = sig.convolve2d(mandrill[0:, 0:, 0], filter,
                                     boundary='symm', mode='same')
    y_clown_filt = sig.convolve2d(clown[0:, 0:, 0], filter, boundary='symm',
                                  mode='same')
    y_trees_filt = sig.convolve2d(trees[0:, 0:, 0], filter, boundary='symm',
                                  mode='same')
    # Cb - filtering:
    cb_cape_filt = sig.convolve2d(cape[0:, 0:, 1], filter, boundary='symm',
                                  mode='same')
    cb_mandrill_filt = sig.convolve2d(mandrill[0:, 0:, 1], filter,
                                      boundary='symm', mode='same')
    cb_clown_filt = sig.convolve2d(clown[0:, 0:, 1], filter, boundary='symm',
                                   mode='same')
    cb_trees_filt = sig.convolve2d(trees[0:, 0:, 1], filter, boundary='symm',
                                   mode='same')
    # Cr - filtering:
    cr_cape_filt = sig.convolve2d(cape[0:, 0:, 2], filter, boundary='symm',
                                  mode='same')
    cr_mandrill_filt = sig.convolve2d(mandrill[0:, 0:, 2], filter,
                                      boundary='symm', mode='same')
    cr_clown_filt = sig.convolve2d(clown[0:, 0:, 2], filter, boundary='symm',
                                   mode='same')
    cr_trees_filt = sig.convolve2d(trees[0:, 0:, 2], filter, boundary='symm',
                                   mode='same')

    # Reuniting arrays:
    # Y:
    cape_yfilt_aux = np.zeros(cape.shape)
    mandrill_yfilt_aux = np.zeros(mandrill.shape)
    clown_yfilt_aux = np.zeros(clown.shape)
    trees_yfilt_aux = np.zeros(trees.shape)

    cape_yfilt_aux[0:, 0:, 0] = y_cape_filt
    for i in np.array([1, 2]):
        cape_yfilt_aux[0:, 0:, i] = cape_trns[0:, 0:, i]

    mandrill_yfilt_aux[0:, 0:, 0] = y_mandrill_filt
    for i in np.array([1, 2]):
        mandrill_yfilt_aux[0:, 0:, i] = mandrill_trns[0:, 0:, i]

    clown_yfilt_aux[0:, 0:, 0] = y_clown_filt
    for i in np.array([1, 2]):
        clown_yfilt_aux[0:, 0:, i] = clown_trns[0:, 0:, i]

    trees_yfilt_aux[0:, 0:, 0] = y_trees_filt
    for i in np.array([1, 2]):
        trees_yfilt_aux[0:, 0:, i] = trees_trns[0:, 0:, i]
    # Cb:
    cape_cbfilt_aux = np.zeros(cape.shape)
    mandrill_cbfilt_aux = np.zeros(mandrill.shape)
    clown_cbfilt_aux = np.zeros(clown.shape)
    trees_cbfilt_aux = np.zeros(trees.shape)

    cape_cbfilt_aux[0:, 0:, 0] = cape_trns[0:, 0:, 0]
    mandrill_cbfilt_aux[0:, 0:, 0] = mandrill_trns[0:, 0:, 0]
    clown_cbfilt_aux[0:, 0:, 0] = clown_trns[0:, 0:, 0]
    trees_cbfilt_aux[0:, 0:, 0] = trees_trns[0:, 0:, 0]
    cape_cbfilt_aux[0:, 0:, 1] = cb_cape_filt
    mandrill_cbfilt_aux[0:, 0:, 1] = cb_mandrill_filt
    clown_cbfilt_aux[0:, 0:, 1] = cb_clown_filt
    trees_cbfilt_aux[0:, 0:, 1] = cb_trees_filt
    cape_cbfilt_aux[0:, 0:, 2] = cape_trns[0:, 0:, 2]
    mandrill_cbfilt_aux[0:, 0:, 2] = mandrill_trns[0:, 0:, 2]
    clown_cbfilt_aux[0:, 0:, 2] = clown_trns[0:, 0:, 2]
    trees_cbfilt_aux[0:, 0:, 2] = trees_trns[0:, 0:, 2]
    # Cr:
    cape_crfilt_aux = np.zeros(cape.shape)
    mandrill_crfilt_aux = np.zeros(mandrill.shape)
    clown_crfilt_aux = np.zeros(clown.shape)
    trees_crfilt_aux = np.zeros(trees.shape)

    cape_crfilt_aux[0:, 0:, 2] = cr_cape_filt
    for i in range(2):
        cape_crfilt_aux[0:, 0:, i] = cape_trns[0:, 0:, i]

    mandrill_crfilt_aux[0:, 0:, 2] = cr_mandrill_filt
    for i in range(2):
        mandrill_crfilt_aux[0:, 0:, i] = mandrill_trns[0:, 0:, i]

    clown_crfilt_aux[0:, 0:, 2] = cr_clown_filt
    for i in range(2):
        clown_crfilt_aux[0:, 0:, i] = clown_trns[0:, 0:, i]

    trees_crfilt_aux[0:, 0:, 2] = cr_trees_filt
    for i in range(2):
        trees_crfilt_aux[0:, 0:, i] = trees_trns[0:, 0:, i]

    # YCbCr -> RGB:
    cape_yfilt = detrans(cape_yfilt_aux)
    mandrill_yfilt = detrans(mandrill_yfilt_aux)
    clown_yfilt = detrans(clown_yfilt_aux)
    trees_yfilt = detrans(trees_yfilt_aux)

    cape_cbfilt = detrans(cape_cbfilt_aux)
    mandrill_cbfilt = detrans(mandrill_cbfilt_aux)
    clown_cbfilt = detrans(clown_cbfilt_aux)
    trees_cbfilt = detrans(trees_cbfilt_aux)

    cape_crfilt = detrans(cape_crfilt_aux)
    mandrill_crfilt = detrans(mandrill_crfilt_aux)
    clown_crfilt = detrans(clown_crfilt_aux)
    trees_crfilt = detrans(trees_crfilt_aux)

    # Plot:
    plt.figure(figsize=(8, 2))
    fig_y_cape = plt.subplot(141)
    fig_y_cape.imshow(cape_yfilt/255)  # THE RGB(A) VALUE SHOULD BE IN THE RANGE
    # [0 ... 1] FOR FLOATS OR [0 ... 255] FOR INTEGERS. OUT-OF-RANGE VALUES
    # WILL BE CLIPPED TO THESE BOUNDS!
    fig_y_cape.axis('off')
    fig_y_mandrill = plt.subplot(142)
    fig_y_mandrill.imshow(mandrill_yfilt/255)
    fig_y_mandrill.axis('off')
    fig_y_clown = plt.subplot(143)
    fig_y_clown.imshow(clown_yfilt/255)
    fig_y_clown.axis('off')
    fig_y_trees = plt.subplot(144)
    fig_y_trees.imshow(trees_yfilt/255)
    fig_y_trees.axis('off')
    plt.savefig('imgs/yfilt.eps')

    plt.figure(figsize=(8, 2))
    fig_cb_cape = plt.subplot(141)
    fig_cb_cape.imshow(cape_cbfilt/255)
    fig_cb_cape.axis('off')
    fig_cb_mandrill = plt.subplot(142)
    fig_cb_mandrill.imshow(mandrill_cbfilt/255)
    fig_cb_mandrill.axis('off')
    fig_cb_clown = plt.subplot(143)
    fig_cb_clown.imshow(clown_cbfilt/255)
    fig_cb_clown.axis('off')
    fig_cb_trees = plt.subplot(144)
    fig_cb_trees.imshow(trees_cbfilt/255)
    fig_cb_trees.axis('off')
    plt.savefig('imgs/cbfilt.eps')

    plt.figure(figsize=(8, 2))
    fig_cr_cape = plt.subplot(141)
    fig_cr_cape.imshow(cape_crfilt/255)
    fig_cr_cape.axis('off')
    fig_cr_mandrill = plt.subplot(142)
    fig_cr_mandrill.imshow(mandrill_crfilt/255)
    fig_cr_mandrill.axis('off')
    fig_cr_clown = plt.subplot(143)
    fig_cr_clown.imshow(clown_crfilt/255)
    fig_cr_clown.axis('off')
    fig_cr_trees = plt.subplot(144)
    fig_cr_trees.imshow(trees_crfilt/255)
    fig_cr_trees.axis('off')
    plt.savefig('imgs/crfilt.eps')

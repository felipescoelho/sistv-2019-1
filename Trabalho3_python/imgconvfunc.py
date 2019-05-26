# File: imgconvfunc.py
# Functions to convert a image from RGB to YIQ or to YCbCr:
from numpy import *


def rgb2yiq(rgb):
    """
    Transforms RGB to YIQ:
    >>>>> yiq = rgb2yiq(rgb) <<<<<
    where, rgb stands for the rgb array format
           yiq stands for the yiq array format
    """
    # Defining array shape:
    lx, ly, k = rgb.shape
    # Separating RGB arrays:
    r = rgb[0:, 0:, 0]
    g = rgb[0:, 0:, 1]
    b = rgb[0:, 0:, 2]
    # Creating the y matrix:
    y = r*.299 + g*.587 + b*.114
    # Creating the u and v parameters:
    u = (b-y)*.492
    v = (r-y)*.877
    # Creating the i and q matrix:
    arg = radians(33)
    i_mat = v*cos(arg) - u*sin(arg)
    q = v*sin(arg) + u*cos(arg)
    # I, Q normalization:
    min_y = y.min()
    min_i = i_mat.min()  # menor valor I
    min_q = q.min()  # menor valor Q
    min_abs = min(min_y, min_i, min_q)  # Menor valor de I ou Q
    y_aux = y-min_abs
    i_aux = i_mat-min_abs
    q_aux = q-min_abs
    max_y = y_aux.max()
    max_i = i_aux.max()
    max_q = q_aux.max()
    max_abs = max(max_y, max_i, max_q)
    norm_fact = 255/max_abs
    y_norm = y_aux*norm_fact
    i_norm = i_aux*norm_fact
    q_norm = q_aux*norm_fact
    # Reuniting arrays
    yiq = zeros([lx, ly, k])
    yiq[0:, 0:, 0] = y_norm
    yiq[0:, 0:, 1] = i_norm
    yiq[0:, 0:, 2] = q_norm
    return yiq


def yiq2rgb(yiq):
    '''
    Transforms YIQ into RGB:
    >>>>> rgb = yiq2rgb(yiq) <<<<<
    where, yiq stands for the yiq array format
           rgb stands for the rgb array format
    '''
    # Defining array shape
    lx, ly, k = yiq.shape
    # Separating the YIQ arrays:
    y_mat = yiq[0:, 0:, 0]
    i_mat = yiq[0:, 0:, 1]
    q_mat = yiq[0:, 0:, 2]
    # Creating the u and v matrix:
    arg = radians(33)
    u = q_mat*cos(arg) - i_mat*sin(arg)
    v = q_mat*sin(arg) + i_mat*cos(arg)
    # Creating the r ang b matrix:
    r = y_mat + v/.877
    b = y_mat + u/.492
    # Creating the g matrix:
    g = (y_mat - r*.299 - b*.114)/.587
    # Normalizing RGB:
    min_r = r.min()
    min_g = g.min()
    min_b = b.min()
    min_abs = min(min_r, min_g, min_b)
    r_aux = r - min_abs
    g_aux = g - min_abs
    b_aux = b - min_abs
    max_r = r_aux.max()
    max_g = g_aux.max()
    max_b = b_aux.max()
    max_abs = max(max_r, max_g, max_b)
    norm_fact = 255/max_abs
    r_norm = r_aux*norm_fact
    g_norm = g_aux*norm_fact
    b_norm = b_aux*norm_fact
    # Reuniting arrays:
    rgb = zeros([lx, ly, k])
    rgb[0:, 0:, 0] = r_norm
    rgb[0:, 0:, 1] = g_norm
    rgb[0:, 0:, 2] = b_norm
    return rgb


def rgb2ycbcr(rgb):
    """
    Transforms RGB into YCbCr:
    >>>>> ycbcr = rgb2ycbcr(rgb) <<<<<
    where, rgb stands for the rgb array format
           ycbcr stands for the ycbcr array format
    """
    # Defining array shape:
    lx, ly, k = rgb.shape
    # Separating RGB arrays:
    r = rgb[0:, 0:, 0]
    g = rgb[0:, 0:, 1]
    b = rgb[0:, 0:, 2]
    # Creating Y, Cb and Cr arrays:
    y = r*.2126 + g*.7152 + b*.0722
    cb = (b-y)/1.8556
    cr = (r-y)/1.5748
    # I, Q normalization:
    min_y = y.min()
    min_cb = cb.min()  # maior valor Cb
    min_cr = cr.min()  # maior valor Cr
    min_abs = min(min_y, min_cb, min_cr)  # Maior valor de Cb ou Cr
    y_aux = y-min_abs
    cb_aux = cb-min_abs
    cr_aux = cr-min_abs
    max_y = y_aux.max()
    max_cb = cb_aux.max()
    max_cr = cr_aux.max()
    max_abs = max(max_y, max_cb, max_cr)
    norm_fact = 255/max_abs
    y_norm = y_aux*norm_fact
    cb_norm = cb_aux*norm_fact
    cr_norm = cr_aux*norm_fact
    # Reuniting arrays:
    ycbcr = zeros([lx, ly, k])
    ycbcr[0:, 0:, 0] = y_norm
    ycbcr[0:, 0:, 1] = cb_norm
    ycbcr[0:, 0:, 2] = cr_norm
    return ycbcr


def ycbcr2rgb(ycbcr):
    '''
    Transforms YCbCr into RGB:
    >>>>> rgb = ycbcr2rgb(ycbcr) <<<<<
    where, rgb stands for the rgb array format
           ycbcr stands for the ycbcr array format
    '''
    # Defining array shapes:
    lx, ly, k = ycbcr.shape
    # Separating YCbCr arrays:
    y = ycbcr[0:, 0:, 0]
    cb = ycbcr[0:, 0:, 1]
    cr = ycbcr[0:, 0:, 2]
    # Creating the R, G and B arrays:
    b = cb*1.8556 + y
    r = cr*1.5748 + y
    g = (y - r*.2126 - b*.0722)/.7152
    # Normalizing RGB:
    min_r = r.min()
    min_g = g.min()
    min_b = b.min()
    min_abs = min(min_r, min_g, min_b)
    r_aux = r - min_abs
    g_aux = g - min_abs
    b_aux = b - min_abs
    max_r = r_aux.max()
    max_g = g_aux.max()
    max_b = b_aux.max()
    max_abs = max(max_r, max_g, max_b)
    norm_fact = 255/max_abs
    r_norm = r_aux*norm_fact
    g_norm = g_aux*norm_fact
    b_norm = b_aux*norm_fact
    # Reuniting arrays:
    rgb = zeros([lx, ly, k])
    rgb[0:, 0:, 0] = r_norm
    rgb[0:, 0:, 1] = g_norm
    rgb[0:, 0:, 2] = b_norm
    return rgb


def yiq2ycbcr(yiq):
    '''
    Transforms YIQ into YCbCr:
    >>>>> ycbcr = yiq2ycbcr(yiq) <<<<<
    where, yiq stands for the yiq array format
           ycbcr stands for the ycbcr array format
    '''
    # Using the other functions to convert:
    rgb = yiq2rgb(yiq)
    ycrcb = rgb2ycbcr(rgb)
    return ycbcr


def ycbcr2yiq(ycbcr):
    '''
    Transforms YCbCr into YIQ:
    >>>>> yiq = ycbcr2yiq(ycbcr) <<<<<
    where, yiq stands for the yiq array format
           ycbcr stands for the ycbcr array format
    '''
    # Using the other functions to convert:
    rgb = ycbcr2rgb(ycbcr)
    yiq = rgb2yiq(rgb)
    return yiq

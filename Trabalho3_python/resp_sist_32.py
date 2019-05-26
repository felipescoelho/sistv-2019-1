# Aluno: Luiz Felipe da S. Coelho, lfscoelho@ieee.org
# Data: 07/05/2019

# File name: histfunc.py

# 3. INFORMACAO DE COR
# 3.2. RESPOSTA DO SISTEMA VISUAL A INFORMACAO DE COR
# ----------------------------------------------------------------------------
# 1 - Tarefa: A function tha recieves an image I, and returns its histogram:
import numpy as np
import matplotlib.pyplot as plt
import funcs32

if __name__ == '__main__':
    # 1 - Tarefa:
    funcs32.hist_y('imgs/cape.tif')  # Making the histogram of cape.tif, as an example.
    # 3 - Tarefa:
    # Making the histogram of cape.tif as an example.
    rgb, yiq, ycbcr = funcs32.hist('imgs/cape.tif')

    entropia = funcs32.entropy(rgb)
    print entropia

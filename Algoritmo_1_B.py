#Carlos Paredes Márquez
#13/08/2021
#Algoritmo #1.B
''' Construye una imagen de 12x6, en escala de grises y dibuja 2 rectángulos '''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import utils

im = np.zeros((12,6,3), dtype= np.uint8) #12 filas, 6 columnas.

col = -1
cont: int = 0
val_c = -36

while cont <= 5:
    val_c = val_c + 36
    col = col + 1
    im[0:12,col] = val_c
    cont = cont + 1

im[0:6,0:3,2] = 225
im[6:12,3:6,0] = 225

utils.grid(plt, im)
plt.imshow(im)
plt.show()
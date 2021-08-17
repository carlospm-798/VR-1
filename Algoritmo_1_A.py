#Carlos Paredes Márquez
#12/08/2021
#Algoritmo #1.A
''' Construye una imagen de 8x15, en escala de grises y dibuja 3 pixels de diferente color '''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import utils

im = np.zeros((8,15,3), dtype= np.uint8) #8 filas, 15 columnas.

col = -1
cont: int = 0
val_c = -17

#im[0:8,col] = val_c

while cont <= 14:
    val_c = val_c + 17
    col = col + 1
    im[0:8,col] = val_c
    cont = cont + 1
    print("Valor:", val_c, "Columa:", col, "Contador:", cont)

im[0,0,2] = 225
im[0,2,1] = 225
im[0,4,0] = 225

utils.grid(plt, im)
plt.imshow(im) #,cmap= 'gray'
plt.show()
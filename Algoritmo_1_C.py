#Carlos Paredes Márquez
#13/08/2021
#Algoritmo 1.C
''' Construye una imagen de 9x8, RGB y dibuja 3 pixels de diferente color '''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import utils

im = np.zeros((9,8,3), dtype= np.uint8) #5 filas, 10 columnas. #canales de color

im[0:9,0:8,2] = 225
#im[0:9,0:8,1] = 225
#im[0:9,0:8,0] = 225

im[1,1,0] = 225
im[1,1,1] = 225
im[1,1,2] = 225

im[4,4,1] = 225
im[7,6,0] = 225

rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
utils.grid(plt, rgb)
plt.imshow(rgb) #cmap='gray' | mapa de grises, cuando no usamos 3 colores
plt.show()
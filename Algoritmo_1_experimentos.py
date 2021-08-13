#Carlos Paredes Márquez
#12/08/2021
#Algoritmo #1

import cv2
import numpy as np
import matplotlib.pyplot as plt
import utils

im = np.zeros((5,10,3), dtype= np.uint8) #5 filas, 10 columnas. #canales de color

im[0:5,0:3,2] = 100 #El último número indica el color
im[0:5,3:6,1] = 100
im[0:5,6:10,0] = 100

im[1:2,0:10,2] = 225
im[3:4,0:10,1] = 150

im[2:3,3:6,2] = 255
im[2:3,3:6,1] = 255
im[2:3,3:6,0] = 255

rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

#utils.grid(plt, rgb) #Hacer paneles, no me funciona 'grid'
plt.imshow(rgb) #cmap='gray' | mapa de grises, cuando no usamos 3 colores
plt.show()
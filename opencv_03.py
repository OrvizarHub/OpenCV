# Cambiar espacio de color y mostrar 

import numpy as np
import cv2
import os 

def CargarImagen(mostrar=True):
    ruta = os.getcwd()
    nombreArchivo = r'recursos\paisaje_reducido.jpg'
    rutaAbrir = os.path.join(ruta, nombreArchivo)
    imagen = cv2.imread(rutaAbrir)

    if mostrar:
        cv2.imshow('imagen', imagen)
        cv2.moveWindow('imagen', 0, 0)

    return imagen

def CambiarEspacioColor(imagen, mostrar=True):
    h, w, c = imagen.shape

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(imagen, cv2.COLOR_BGR2LAB)

    if mostrar:
        cv2.imshow("Escala de grises", gris)
        cv2.moveWindow('Escala de grises', w, 0)
        
        cv2.imshow("HSV", hsv)
        cv2.moveWindow('HSV', 0, h)
        
        cv2.imshow("Lab", lab)
        cv2.moveWindow('Lab', w, h)

    return None

if __name__ == "__main__":
    imagen = CargarImagen()
    CambiarEspacioColor(imagen)

    cv2.waitKey(0)
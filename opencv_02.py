# Separar, mostrar canales individuales y combinar canales

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

def SepararCanales(imagen, mostrar=True):
    h, w, c = imagen.shape
    B, G, R = cv2.split(imagen)

    if mostrar:
        cv2.imshow('azul', B)
        cv2.moveWindow('azul', w, 0)

        cv2.imshow('verde', G)
        cv2.moveWindow('verde', 0, h)

        cv2.imshow('rojo', B)
        cv2.moveWindow('rojo', w, h)

    return B, G, R

def MostrarColoresSeparados(azul, verde, rojo, mostrar=True):
    h, w, c = imagen.shape

    canalVacio = np.zeros(shape=(h, w), dtype='uint8')
    
    imagenRojo = cv2.merge([canalVacio, canalVacio, rojo])
    imagenVerde = cv2.merge([canalVacio, verde, canalVacio])
    imagenAzul = cv2.merge([azul, canalVacio, canalVacio])

    if mostrar:
        cv2.imshow('rojo', imagenRojo)
        cv2.moveWindow('rojo', w, 0)

        cv2.imshow('verde', imagenVerde)
        cv2.moveWindow('verde', 0, h)

        cv2.imshow('azul', imagenAzul)
        cv2.moveWindow('rojo', w, h)

    return None

def CombinarCanales(azul, verde, rojo, mostrar=True):
    h, w = azul.shape
    # imagenComb = cv2.merge([verde, azul, rojo])
    # imagenComb = cv2.merge([rojo, verde, azul])
    imagenComb = cv2.merge([azul, verde, rojo])

    if mostrar:
        cv2.imshow('canales combinados', imagenComb)
        cv2.moveWindow('canales combinados', 0, h)

    return imagenComb

if __name__ == "__main__":
    imagen = CargarImagen()
    azul, verde, rojo = SepararCanales(imagen, False)
    MostrarColoresSeparados(azul, verde, rojo, False)
    CombinarCanales(azul, verde, rojo)


    cv2.waitKey(0)
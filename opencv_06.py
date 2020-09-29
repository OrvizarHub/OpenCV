import numpy as np
import cv2
import os

def CargarImagen():
    ruta = os.getcwd()
    nombreArchivo = r'recursos\paisaje.jpg'
    rutaAbrir = os.path.join(ruta, nombreArchivo)
    imagen = cv2.imread(rutaAbrir)

    cv2.imshow('img', imagen)
    cv2.moveWindow('img', 0, 0)

    return imagen

def TrasladarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    M = np.float32([[1, 0, 25], [0, 1, 50]])
    imgT1 = cv2.warpAffine(img, M, (w, h))

    cv2.imshow("imgT1", imgT1)
    cv2.moveWindow("imgT1", w, 0)

    M = np.float32([[1, 0, -90], [0, 1, -60]])
    imgT2 = cv2.warpAffine(img, M, (w, h))

    cv2.imshow("imgT2", imgT2)
    cv2.moveWindow("imgT2", w, h)

    return imgT1, imgT2

def RotarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    centro = (int(w//2), int(h//2))
    angulo = 45
    escala = 1

    M = cv2.getRotationMatrix2D(centro, angulo, escala)
    imgR1 = cv2.warpAffine(img, M, (w, h))

    centro = (int(w//2), int(h//2))
    angulo = -70
    escala = 1

    M = cv2.getRotationMatrix2D(centro, angulo, escala)
    imgR2 = cv2.warpAffine(img, M, (w, h))

    cv2.imshow("imgR1", imgR1)
    cv2.moveWindow("imgR1", 2*w, 0)

    cv2.imshow("imgR2", imgR2)
    cv2.moveWindow("imgR2", 2*w, h)

    return imgR1, imgR2

def EscalarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    rFactor = 0.5
    tamano = (int(rFactor*w), int(rFactor*h))

    imgE1 = cv2.resize(img, tamano)
    
    rFactor = 2.0
    tamano = (int(rFactor*w), int(rFactor*h))

    imgE2 = cv2.resize(img, tamano)

    cv2.imshow("imgE1", imgE1)
    cv2.moveWindow("imgE1", 3*w, 0)

    cv2.imshow("imgE2", imgE2)
    cv2.moveWindow("imgE2", 3*w, h)

    return imgE1, imgE2

def ReflejarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imgFV = cv2.flip(img, 0)
    imgFH = cv2.flip(img, 1)

    cv2.imshow("imgFV", imgFV)
    cv2.moveWindow("imgFV", w, 0)

    cv2.imshow("imgFH", imgFH)
    cv2.moveWindow("imgFH", w, h)

    return imgFV, imgFH

def RecortarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imgC1 = img[90:150, 80:200]
    imgC2 = img[150:250, 200:250]

    cv2.imshow('imgC1', imgC1)
    cv2.moveWindow('imgC1', 0, h)

    cv2.imshow('imgC2', imgC2)
    cv2.moveWindow('imgC2', 0, 2*h)

    return imgC1

if __name__ == "__main__":
    img = CargarImagen()

    TrasladarImagen(img)
    RotarImagen(img)
    EscalarImagen(img)
    ReflejarImagen(img)
    RecortarImagen(img)

    cv2.waitKey(0)

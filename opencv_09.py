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

def DifuminarImagen_Average(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imagenD1 = cv2.blur(img, (3, 3))
    imagenD2 = cv2.blur(img, (5, 5))
    imagenD3 = cv2.blur(img, (7, 7))

    imagenF = np.hstack((imagenD1, imagenD2, imagenD3))

    cv2.imshow('DifuminarImagen_Average', imagenF)
    cv2.moveWindow('DifuminarImagen_Average', 0, h)

    return imagenF

def DifuminarImagen_Gaussian(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imagenD1 = cv2.GaussianBlur(img, (3, 3), 0)
    imagenD2 = cv2.GaussianBlur(img, (5, 5), 0)
    imagenD3 = cv2.GaussianBlur(img, (7, 7), 0)

    imagenF = np.hstack((imagenD1, imagenD2, imagenD3))

    cv2.imshow('DifuminarImagen_Gaussian', imagenF)
    cv2.moveWindow('DifuminarImagen_Gaussian', 0, 2*h)

    return imagenF

def DifuminarImagen_Median(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imagenD1 = cv2.medianBlur(img, 3)
    imagenD2 = cv2.medianBlur(img, 5)
    imagenD3 = cv2.medianBlur(img, 7)

    imagenF = np.hstack((imagenD1, imagenD2, imagenD3))

    cv2.imshow('DifuminarImagen_Median', imagenF)
    cv2.moveWindow('DifuminarImagen_Median', 0, 3*h)

    return imagenF

def DifuminarImagen_Bilateral(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imagenD1 = cv2.bilateralFilter(img, 3, 21, 21)
    imagenD2 = cv2.bilateralFilter(img, 5, 31, 31)
    imagenD3 = cv2.bilateralFilter(img, 7, 41, 41)

    imagenF = np.hstack((imagenD1, imagenD2, imagenD3))

    cv2.imshow('DifuminarImagen_Bilateral', imagenF)
    cv2.moveWindow('DifuminarImagen_Bilateral', 0, 3*h)

    return imagenF

if __name__ == '__main__':
    img = CargarImagen()
    DifuminarImagen_Average(img)
    DifuminarImagen_Gaussian(img)
    DifuminarImagen_Median(img)
    DifuminarImagen_Bilateral(img)

    cv2.waitKey(0)


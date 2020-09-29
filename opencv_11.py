import numpy as np
import cv2
import os

def CargarImagen():
    ruta = os.getcwd()
    nombreArchivo = r'recursos\monedas.jpg'
    rutaAbrir = os.path.join(ruta, nombreArchivo)
    imagen = cv2.imread(rutaAbrir)

    h, w, c = imagen.shape
    factor = 0.85

    nAlto, nAncho = int(factor*h), int(factor*w)
    imagenT = cv2.resize(imagen, (nAncho, nAlto))

    cv2.imshow('img', imagenT)
    cv2.moveWindow('img', 0, 0)

    return imagenT

def Laplacian(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))

    cv2.imshow('laplacian', laplacian)
    cv2.moveWindow('laplacian', w, 0)

    return None

def Sobel(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobelC = cv2.bitwise_or(sobelX, sobelY)

    cv2.imshow('sobel x', sobelX)
    cv2.moveWindow('sobel x', w, 0)

    cv2.imshow('sobel y', sobelY)
    cv2.moveWindow('sobel y', w, h)

    cv2.imshow('sobel c', sobelC)
    cv2.moveWindow('sobel c', w, 2*h)

    return None

def Canny(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGris, (5, 5), 0)

    imgCanny = cv2.Canny(imgBlur, 30, 150)

    cv2.imshow('img canny', imgCanny)
    cv2.moveWindow('img canny', w, 0)

def DetectarBordeMoneda(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGris, (5, 5), 0)

    _, imgThres = cv2.threshold(imgBlur, 220, 255, cv2.THRESH_BINARY_INV)
    imgCanny = cv2.Canny(imgThres, 30, 150)

    cv2.imshow('img gris', imgGris)
    cv2.moveWindow('img gris', w, 0)

    cv2.imshow('img thres', imgThres)
    cv2.moveWindow('img thres', w, h)
    
    cv2.imshow('img canny', imgCanny)
    cv2.moveWindow('img canny', w, 2*h)

    return None


if __name__ == '__main__':
    img = CargarImagen()
    # Laplacian(img)
    # Sobel(img)
    # Canny(img)
    DetectarBordeMoneda(img)

    cv2.waitKey(0)
    
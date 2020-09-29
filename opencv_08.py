import numpy as np
import cv2
import os

class Color:
    blanco = (255, 255, 255)
    negro = (0, 0, 0)
    azul =  (255, 0, 0)
    verde = (0, 255, 0)
    rojo  = (0, 0, 255)

def CargarImagen():
    ruta = os.getcwd()
    nombreArchivo = r'recursos\paisaje.jpg'
    rutaAbrir = os.path.join(ruta, nombreArchivo)
    imagen = cv2.imread(rutaAbrir)

    cv2.imshow('img', imagen)
    cv2.moveWindow('img', 0, 0)

    return imagen

def CrearHistrograma(imagen, mascara=None, color=Color.blanco):
    h, w = imagen.shape

    histTamano = 256

    hist = cv2.calcHist([imagen], [0], mascara, [histTamano], [0, histTamano])

    histW, histH = 2*histTamano, h
    binW = histW//histTamano

    histImagen = np.zeros(shape=(histH, histW, 3), dtype='uint8')
    cv2.normalize(hist, hist, alpha=0, beta=histH, norm_type=cv2.NORM_MINMAX) 

    for i in range(1, histTamano):
        cv2.line(histImagen, (binW*(i-1), histH - hist[i-1]), (binW*(i), histH - hist[i]), color, 2)

    return histImagen

def DifHistogramas(imagen):
    h, w, c = imagen.shape

    imgGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    histSin = CrearHistrograma(imgGris)

    mascara = 255*np.ones_like(imgGris)
    cv2.circle(mascara, (350, 75), 30, 0, -1)

    imgE = cv2.bitwise_and(imgGris, imgGris, mask=mascara)

    histCon = CrearHistrograma(imgGris, mascara)

    cv2.imshow('imgG', imgGris)
    cv2.moveWindow('imgG', w, 0)

    cv2.imshow('imgHSM', histSin)
    cv2.moveWindow('imgHSM', 2*w, 0)

    cv2.imshow('imgGM', imgE)
    cv2.moveWindow('imgGM', w, h)

    cv2.imshow('imgHCM', histCon)
    cv2.moveWindow('imgHCM', 2*w, h)

def CrearHistogramaColor(imagen):
    h, w, c = imagen.shape

    planos = cv2.split(imagen)
    histAzul = CrearHistrograma(planos[0], color=Color.azul)
    histVerde = CrearHistrograma(planos[1], color=Color.verde)
    histRojo = CrearHistrograma(planos[2], color=Color.rojo)

    cv2.imshow('imgHAzul', histAzul)
    cv2.moveWindow('imgHAzul', 3*w, 0)

    cv2.imshow('imgHVerde', histVerde)
    cv2.moveWindow('imgHVerde', 3*w, h)

    cv2.imshow('imgHRojo', histRojo)
    cv2.moveWindow('imgHRojo', 3*w, 2*h)

    return None

def EcualizarHistograma(imagen):
    h, w, c = imagen.shape
    
    imgGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imgEq = cv2.equalizeHist(imgGris)

    histImgEq = CrearHistrograma(imgEq)

    cv2.imshow('imgEq', imgEq)
    cv2.moveWindow('imgEq', 0, h)

    cv2.imshow('imgHimgEq', histImgEq)
    cv2.moveWindow('imgEq', w, h)

    return None

if __name__ == '__main__':
    img = CargarImagen()
    DifHistogramas(img)
    # CrearHistogramaColor(img)
    EcualizarHistograma(img)


    cv2.waitKey(0)
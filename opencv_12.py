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

def DetectorBordeMoneda(imagen, mostrar=False):
    img = imagen.copy()
    h, w, c = img.shape

    imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGris, (5, 5), 0)

    _, imgThres = cv2.threshold(imgBlur, 210, 255, cv2.THRESH_BINARY_INV)
    cv2.circle(imgThres, (375, 240), 65, 255, -1)

    imgCanny = cv2.Canny(imgThres, 30, 150)

    if mostrar:
        cv2.imshow('img gris', imgGris)
        cv2.moveWindow('img gris', w, 0)

        cv2.imshow('img blur', imgBlur)
        cv2.moveWindow('img blur', 2*w, 0)

        cv2.imshow('img thres', imgThres)
        cv2.moveWindow('img thres', w, h)

        cv2.imshow('img canny', imgCanny)
        cv2.moveWindow('img canny', 2*w, h)

    return imgCanny

def DetectarContorno(imagen, imgCanny):
    img = imagen.copy()
    h, w, c = img.shape

    cnts, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Se han encontrado {} monedas en esta imagen".format(len(cnts)))

    cv2.drawContours(img, cnts, -1, (255, 0, 0), 2)

    cv2.imshow('img canny', imgCanny)
    cv2.moveWindow('img canny', w, 0)

    cv2.imshow('img contornos', img)
    cv2.moveWindow('img contornos', w, h)

    return cnts

def ContarMonedas(imagen, cnts):
    img = imagen.copy()
    # h, w, c = img.shape

    for i, c in enumerate(cnts):
        x, y, w, h = cv2.boundingRect(c)

        moneda = img[y:y+h, x:x+w]

        cv2.imshow('moneda {}'.format(i), moneda)
        
        cv2.waitKey(0)

    return None

if __name__ == '__main__':
    img = CargarImagen()
    imgCanny = DetectorBordeMoneda(img)
    cnts = DetectarContorno(img, imgCanny)
    ContarMonedas(img, cnts)
    
    cv2.waitKey(0)
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

def ThresholdBinary(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGris, (5, 5), 0)

    _, imgThres1 = cv2.threshold(imgBlur, 175, 255, cv2.THRESH_BINARY)
    _, imgThres2 = cv2.threshold(imgBlur, 175, 255, cv2.THRESH_BINARY_INV)

    imgSeg1 = cv2.bitwise_and(img, img, mask=imgThres1)
    imgSeg2 = cv2.bitwise_and(img, img, mask=imgThres2)

    cv2.imshow('imagen gris', imgGris)
    cv2.moveWindow('imagen gris', w, 0)

    cv2.imshow('imagen blur', imgBlur)
    cv2.moveWindow('imagen blur', 2*w, 0)

    cv2.imshow('imagen thres', imgThres1)
    cv2.moveWindow('imagen thres', w, h)

    cv2.imshow('imagen thres inv', imgThres2)
    cv2.moveWindow('imagen thres inv', 2*w, h)

    cv2.imshow('imagen seg', imgSeg1)
    cv2.moveWindow('imagen seg', w, 2*h)

    cv2.imshow('imagen seg inv', imgSeg2)
    cv2.moveWindow('imagen seg inv', 2*w, 2*h)

    return None

def ThresholdAdaptive(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGris, (5, 5), 0)

    imgTA_mean = cv2.adaptiveThreshold(imgGris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 8)
    imgTA_gauss = cv2.adaptiveThreshold(imgGris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 8)

    imgSeg_mean = cv2.bitwise_and(img, img, mask=imgTA_mean)
    imgSeg_gauss = cv2.bitwise_and(img, img, mask=imgTA_gauss)

    cv2.imshow('imagen gris', imgGris)
    cv2.moveWindow('imagen gris', w, 0)

    cv2.imshow('imagen blur', imgBlur)
    cv2.moveWindow('imagen blur', 2*w, 0)

    cv2.imshow('imagen thres mean', imgTA_mean)
    cv2.moveWindow('imagen thres mean', w, h)

    cv2.imshow('imagen thres gauss', imgTA_gauss)
    cv2.moveWindow('imagen thres gauss', 2*w, h)

    cv2.imshow('imagen seg mean', imgSeg_mean)
    cv2.moveWindow('imagen seg mean', w, 2*h)

    cv2.imshow('imagen seg gauss', imgSeg_gauss)
    cv2.moveWindow('imagen seg gauss', 2*w, 2*h)

    return None

if __name__ == '__main__':
    img = CargarImagen()
    # ThresholdBinary(img)
    ThresholdAdaptive(img)

    cv2.waitKey(0)
    
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

def CrearMascaras(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    offset = 50

    mascara1 = np.zeros(shape=(h, w), dtype='uint8')
    cv2.rectangle(mascara1, (offset, offset), (w - offset, h - offset), 255, -1)

    mascara2 = np.zeros(shape=(h, w), dtype='uint8')
    cv2.circle(mascara2, (int(w//2), int(h//2)), 3*offset, 255, -1)

    cv2.imshow("mascara1", mascara1)
    cv2.moveWindow("mascara1", w, 0)

    cv2.imshow("mascara2", mascara2)
    cv2.moveWindow("mascara2", w, h)

    return mascara1, mascara2

def CombinarMascaras(mascara1, mascara2):
    h, w = mascara1.shape

    mascaraAND = cv2.bitwise_and(mascara1, mascara2)
    mascaraOR = cv2.bitwise_or(mascara1, mascara2)
    mascaraXOR = cv2.bitwise_xor(mascara1, mascara2)
    mascaraNOT = cv2.bitwise_not(mascara1)

    cv2.imshow('mascaraAND', mascaraAND)
    cv2.moveWindow('mascaraAND', 2*w, 0)

    cv2.imshow('mascaraOR', mascaraOR)
    cv2.moveWindow('mascaraOR', 2*w, h)

    cv2.imshow('mascaraXOR', mascaraXOR)
    cv2.moveWindow('mascaraXOR', 2*w, 2*h)

    cv2.imshow('mascaraNOT', mascaraNOT)
    cv2.moveWindow('mascaraNOT', 2*w, 3*h)

    return mascaraAND, mascaraOR, mascaraXOR, mascaraNOT

def EnmascararImagen(imagen, mascaras):
    img = imagen.copy()
    h, w, c = img.shape

    imgM1 = cv2.bitwise_and(img, img, mask=mascaras[0])
    imgM2 = cv2.bitwise_and(img, img, mask=mascaras[1])
    imgM3 = cv2.bitwise_and(img, img, mask=mascaras[2])
    imgM4 = cv2.bitwise_and(img, img, mask=mascaras[3])

    cv2.imshow('imgM1', imgM1)
    cv2.moveWindow('imgM1', 3*w, 0)

    cv2.imshow('imgM2', imgM2)
    cv2.moveWindow('imgM2', 3*w, h)

    cv2.imshow('imgM3', imgM3)
    cv2.moveWindow('imgM3', 3*w, 2*h)

    cv2.imshow('imgM4', imgM4)
    cv2.moveWindow('imgM4', 3*w, 3*h)

    return imgM1, imgM2, imgM3, imgM4

if __name__ == "__main__":
    img = CargarImagen()

    masc1, masc2 = CrearMascaras(img)
    mascs = CombinarMascaras(masc1, masc2)
    EnmascararImagen(img, mascs)

    cv2.waitKey(0)
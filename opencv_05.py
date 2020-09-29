import numpy as np
import cv2

class Color:
    negro    = (0, 0, 0)
    azul     = (255, 0, 0)
    verde    = (0, 255, 0)
    rojo     = (0, 0, 225)
    celeste  = (255, 255, 0)
    fucsia   = (255, 0, 255)
    amarillo = (0, 255, 255)
    blanco   = (255, 255, 255)

def DibujarLineas(imagenVacia):
    img = imagenVacia.copy()

    cv2.line(img, (0, 0), (300, 300), Color.amarillo, 15)
    cv2.line(img, (300, 0), (0, 300), Color.azul, 5)

    return img

def DibujarRectangulos(imagenVacia):
    img = imagenVacia.copy()

    cv2.rectangle(img, (50, 50), (150, 150), Color.celeste)
    # cv2.imshow("imgR", img)
    # cv2.waitKey(0)

    cv2.rectangle(img, (200, 50), (250, 250), Color.verde, 10)
    # cv2.imshow("imgR", img)
    # cv2.waitKey(0)

    cv2.rectangle(img, (50, 150), (150, 250), Color.rojo, -1)
    # cv2.imshow("imgR", img)
    # cv2.waitKey(0)

    return img

def DibujarDiana(imagenVacia):
    img = imagenVacia.copy()
    h, w, c = img.shape

    cx, cy = int(w//2), int(h//2)

    for r in range(0, cx+1, 25):
        cv2.circle(img, (cx, cy), r, Color.blanco, 5)

    return img 

def DibujarBurbujas(imagenVacia):
    img = imagenVacia.copy()
    h, w, c = img.shape

    for i in range(25):
        centro = tuple(np.random.randint(0, h, size=(2,)))
        radio = np.random.randint(0, h//2)
        color = np.random.randint(0, high=255, size=(3, )).tolist()

        cv2.circle(img, centro, radio, color, -1)

    return img

if __name__ == "__main__":
    h, w, c = 300, 300, 3
    imagenVacia = np.zeros(shape=(h, w, c), dtype="uint8")

    imagenLineas = DibujarLineas(imagenVacia)
    imagenRect = DibujarRectangulos(imagenVacia)

    imagenDiana = DibujarDiana(imagenVacia)
    imagenBurbujas = DibujarBurbujas(imagenVacia)

    cv2.imshow("imgB", imagenBurbujas)
    cv2.waitKey(0)

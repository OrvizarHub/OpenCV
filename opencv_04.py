# segmentar imagen, y cambiar características

import cv2
import os 

def CargarImage(rutaArchivo):
    print('Cargando {}'.format(rutaArchivo))
    imagen = cv2.imread(rutaArchivo)
    cv2.imshow('imagen', imagen)
    cv2.moveWindow('image', 0, 0)
    # cv2.waitKey(0)

    return imagen

def RecortarEsquina(image):
    h, w, c = imagen.shape
    imagenRecortada = image[0:100, 0:100]

    cv2.imshow('imagen recortada', imagenRecortada)
    cv2.moveWindow('imagen recortada', 0, h)

    return imagenRecortada

def ColorearEsquina(imagen, color):
    h, w, c = imagen.shape
    imagenColoreada = imagen.copy()

    imagenColoreada[0:100, 0:100] = color
    cv2.imshow('imagen coloreada', imagenColoreada)
    cv2.moveWindow('imagen coloreada', w, 0)

    return imagenColoreada

if __name__ == "__main__":
    # Colores en RGB
    Azul     = (0,0,255)

    rutaInicial = os.getcwd()

    nombreArchivo = r'recursos\paisaje_reducido.jpg'
    rutaAbrir = os.path.join(rutaInicial, nombreArchivo)

    imagen = CargarImage(rutaAbrir)

    # Python usa BGR
    (b, g, r) = imagen[0, 0]
    print("Pixel en (0, 0) - Rojo (R): {}, Verde (G): {}, Azul (B): {}".format(r, g, b))

    imagen[0, 0] = Azul[::-1]
    (b, g, r) = imagen[0, 0]
    print("Pixel en (0, 0) - Rojo (R): {}, Verde (G): {}, Azul (B): {}".format(r, g, b))

    # Recortar una porció 
    imagenRecortada = RecortarEsquina(imagen)

    # Colorear una esquina
    imagenColoreada = ColorearEsquina(imagen, Aqua[::-1])

    cv2.waitKey(0)
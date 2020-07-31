# Cargar, cambiar tamaño y guardar imagen
# Conceptos básicos

import cv2
import os

def CargarImage(rutaArchivo):
    print('Cargando {}'.format(rutaArchivo))
    imagen = cv2.imread(rutaArchivo)
    cv2.imshow('imagen', imagen)
    cv2.moveWindow('image', 0, 0)
    # cv2.waitKey(0)

    return imagen

def CambiarTamaño(imagen, porcRed):
    #Alto, ancho, canales
    h, w, c = imagen.shape
    print('Alto: {} pixeles'.format(h))
    print('Ancho: {} pixeles'.format(w))
    print('Canales: {} pixeles'.format(c))

    nuevoH = int(porcRed*h)
    nuevoW = int(porcRed*w)

    imagenReducida = cv2.resize(imagen, (nuevoW, nuevoH))
    cv2.imshow('imagen reducida', imagenReducida)
    cv2.moveWindow('imagen reducida', 0, 0)
    # cv2.waitKey(0)

    return imagenReducida

def GuardarImagen(imagenReducida, rutaGuardar):
    print('Guardando {}'.format(rutaGuardar))
    cv2.imwrite(rutaGuardar, imagenReducida)

    return None

if __name__ == "__main__":
    rutaInicial = os.getcwd()

    nombreArchivo = r'recursos\paisaje.jpg'
    rutaAbrir = os.path.join(rutaInicial, nombreArchivo)

    imagen = CargarImage(rutaAbrir)
    imagenReducida = CambiarTamaño(imagen, 0.25)

    # nombreArchivo = r'recursos\naisaje_reducido.jpg'
    nombreArchivo = r'recursos\paisaje_reducido.jpg'
    rutaGuardar = os.path.join(rutaInicial, nombreArchivo)
    GuardarImagen(imagenReducida, rutaGuardar)

    cv2.waitKey(0)

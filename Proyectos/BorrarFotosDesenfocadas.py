'''
Dado un directorio con imagenes borrar las que están desenfocadas

- El programa recibe como argumentos [explorar argparse]:
    ■ directorio de entrada que almacena las imágenes (--image_folder)
    ■ directorio de salida donde se moverán las imágenes desenfocadas (--trash_folder)
        ● respetando misma estructura de subdirectorios que en el directorio de entrada
    ■ [opcional] fichero de salida que almacenará un reporte resultante del proceso (--report):
        ● tiempo invertido, número de imágenes procesadas, número de imágenes desenfocadas detectadas, lista de
        imágenes no desenfocadas con sus scores, lista de imágenes desenfocadas con sus scores, ...

-PASOS A SEGUIR:
○ Instalar y familiarizarse con el módulo de terceros PIL para manipular imágenes
    ■ carga una imagen de disco, rótala y muéstrala siguiendo el tutorial
○ Instalar y familiarizarse con el módulo de terceros tqdm que permite la visualización de barras de
progreso en Python
    ■ muestra una barra de progreso al iterar en un rango de valores
○ Familiarizarse con las diferentes formas que tenemos disponibles en la librería estándar para
listar el contenido de un directorio y elije una
    ■ os.walk, os.listdir, glob, …
        ● considera que el directorio podría a su vez contener subdirectorios con imágenes
    ■ muestra las rutas absolutas de todos los ficheros contenidos el directorio de entrada.
        ● muestra solo los que acaben en extensión: jpg, jpeg y png
○ Familiarizarse con el módulo shutil de la librería estándar
que permite llevar operaciones de alto nivel sobre ficheros y directorios: copiar, mover, etc…
    ■ mueve un fichero jpg de un directorio a otro con shutil
○ Familiarizarse con el módulo de la librería estándar json
    ■ crea un diccionario como el de la imagen y genera su fichero json equivalente (json.dumps)

○ Usa la siguiente función is_blurred para determinar si una imagen está desenfocada

import cv2
import numpy as np

def is_blurred (image, threshold=90):
    imagecv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    graycv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
    edgescv = cv2.Laplacian(graycv, cv2.CV_64F)

    variance = edgescv.var()

    return (variance<threshold, variance)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

import cv2
import numpy as np
import tqdm
import shutil
import json

from PIL import Image
with Image.open("./Images/python-hero.jpg") as im:
    im.rotate(45).show()


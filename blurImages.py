import cv2
import os


def aplicacionDeBlur():
    """
        Función que ayuda a aplicarle un filtro de blur (borroso) a 
        la imágen para poder hacer mejor el tratamiento de cada una de las 
        imágenes. De esta forma, el proceso de análisis resulta más eficiente 
        sin importar la calidad y tamaño de la imágen.
    """

    # Entramos al directorio en el que se encuentran las imagenes a las que se le aplicara
    # el filtro.------------------------------------------------------------------------------
    imagenes_path = r"C:.\imagenes_salida"
    nombre_de_imagenes = os.listdir(imagenes_path)
    # print(nombre_de_imagenes)


    # Ciclo que recorre el directorio para aplicar el filtro a todas las imagenes
    # contenidas en este.---------------------------------------------------------------
    for i in range(len(nombre_de_imagenes)):
        imagen_path = imagenes_path + "/" + nombre_de_imagenes[i]

        imagen = cv2.imread(imagen_path)
        # Filtros blur el cual se les puede aplicar a las imagenes. Uno consta 
        # del método Gausseano y otro es uno que aplica distintos métodos.--------------
        # image_blurred = cv2.GaussianBlur(imagen, (7, 7), 0)
        image_blurred = cv2.blur(imagen, (7, 7))

        # Guardamos la imágen con el filtro aplicado dentro del mismo directorio raíz.---------
        cv2.imwrite(imagenes_path + "/forestFire" + str(i).zfill(2) + ".png", image_blurred)



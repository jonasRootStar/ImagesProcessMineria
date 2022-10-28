import cv2
import os


def formatoDeImagenes():
    """
        Función la cual ayuda a darle formato al nombre y extensión a cada una de 
        las imagenes, de esta forma resultará más sencillo el tratamiento de estas.
    """

    # Colocar el nombre del directorio en donde se encuentran las imagenes 
    # para formatear-----------------------------------------------------------
    imagenes_path = r"C:.\imagenes"
    nombre_de_imagenes = os.listdir(imagenes_path)
    # print(nombre_de_imagenes)


    # Se nombra el directorio en que se guardaran las imagenes con el formato de nombre
    # especifico para comenzar el tratamiento de estas.--------------------------------------
    imagenes_nuevo_path = r"C:.\imagenes_salida"
    # En caso de que el directorio no ha sido creado o no se encontró, se crea para poder seguir
    # con el proceso.
    if not os.path.exists(imagenes_nuevo_path):
        os.makedirs(imagenes_nuevo_path)
        print(f"Directorio creado: {imagenes_nuevo_path}")


    # Recorremos el directorio donde se encuentra la muestra de imagenes a tratar y le aplicamos 
    # formato de nombre especifico.
    for i in range(len(nombre_de_imagenes)):
        imagen_path = imagenes_path + "/" + nombre_de_imagenes[i]

        imagen = cv2.imread(imagen_path)
        # Formato de nombre a la imágen.
        cv2.imwrite(imagenes_nuevo_path + "/forestFire" + str(i).zfill(2) + ".png", imagen)






        

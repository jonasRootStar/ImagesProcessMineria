import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from segmentacionCanales import segmentacionDeRGB



def deteccionMascarasImagenes():
    """
        Función principal que realiza la extracción de máscaras de cada una 
        de las imágenes contenidas en el directorio. Además de esto, hace uso
        de la función del script segmentacionCanales.py.

        NOTA: Ciertas partes del script están comentadas, sin embargo tienen
        cierta utilidad; en caso de querer ver que hacen, se pueden descomentar 
        para poder apreciar su acción.
    """


    # -----------------------------------------------------------------------
    # En caso de no contar con ninguno de los directorios siguientes        |
    # se crearan directamente en el directorio en el que estes trabajando   |
    #                                                                       |
    # Para guardar las mascaras donde se detecte fuego                      |
    # mascaras_fuego = r"C:.\mascaras_fuego"                                 #|
    # if not os.path.exists(mascaras_fuego):                                 #|
    #     os.makedirs(mascaras_fuego)                                        #|
    #     print(f"Directorio creado: {mascaras_fuego}")                      #|
    # #                                                                      #|
    # # Para guardar las mascaras donde se detecte humo                       |
    # mascaras_humo = r"C:.\mascaras_humo"
    # if not os.path.exists(mascaras_humo):
    #     os.makedirs(mascaras_humo)
    #     print(f"Directorio creado: {mascaras_humo}")

    # # Para guardar las mascaras donde se detecte no fuego
    # mascaras_nof = r"C:.\mascaras_nof"
    # if not os.path.exists(mascaras_nof):
    #     os.makedirs(mascaras_nof)
    #     print(f"Directorio creado: {mascaras_nof}")

    # ----------------------------------------------------------------------


    # ----------------------------------------------------------------------+
    # Directorio donde se encuentran las imagenes previamente formateadas   |
    # a un tipo png y se le aplico un blur                                  |
    imagenes_dir_path = r"C:.\imagenes_salida"                             #|
    # Se enlistan los nombres de las imagenes                               |
    imagenes_path = os.listdir(imagenes_dir_path)                          #|
    # ----------------------------------------------------------------------+



    # ------------------------CREACIÓN DE HEADERS DATAFRAME PARA EXPORTAR LOS DESCRIPTORES A CSV--------------------------
    df=pd.DataFrame(columns=['meanR','meanG','meanB','meanS','meanV','stdR','stdG','stdB','stdS','stdV','clase'])



    # ------------------------------------------------------------------------
    # Ciclo para automatizar la extraccion de mascaras de cada una de las imagenes
    for i in range(len(imagenes_path)):
        # Lectura de la imagen a trabajar
        img = cv2.imread(imagenes_dir_path + "/" + imagenes_path[i])
        # Convertimos a formato de color RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # plt.imshow(img)

        # ------------------INCENDIO-----------------------------------------------------------------------------+
        # Medidas en RGB para umbrales del fuego
        umbral_fuego_bajo1 = (200, 20, 5)
        umbral_fuego_bajo2 = (200, 50, 15)

        umbral_fuego_alto1 = (255, 100, 80)
        umbral_fuego_alto2 = (255, 175, 105)


        # Aplicamos los umbrales-------------------------------
        mask_fuego1 = cv2.inRange(img, umbral_fuego_bajo1, umbral_fuego_alto1)
        mask_fuego2 = cv2.inRange(img, umbral_fuego_bajo2, umbral_fuego_alto2)
        mask_fuego = mask_fuego1 + mask_fuego2

        # Separamos la mascara del fondo------------------------
        res_fuego = cv2.bitwise_and(img, img, mask=mask_fuego)
        res_fuego = cv2.cvtColor(res_fuego, cv2.COLOR_BGR2RGB)


        #Llamado a la función para obtener los descriptes de la máscara------------------------------------------|
        segmentacionDeRGB(res_fuego,img,df,"fuego")

        # # Guardamos la mascara en el directorio especifico para mascaras de fuego-----------
        # cv2.imwrite(mascaras_fuego + "/mascara_fuego_rgb" + str(i).zfill(2) + ".png", res_fuego)
        # -------------------------------------------------------------------------------------------------------+


        # --------------------HUMO--------------------------
        # Medidas en RGB para umbrales del humo
        umbral_humo_bajo1 = (90, 90, 90)
        umbral_humo_bajo2 = (150, 120, 115)

        umbral_humo_alto1 = (190, 180, 170)
        umbral_humo_alto2 = (230, 220, 220)

        # Aplicamos los umbrales---------------------------------------------
        mask_humo1 = cv2.inRange(img, umbral_humo_bajo1, umbral_humo_alto1)
        mask_humo2 = cv2.inRange(img, umbral_humo_bajo2, umbral_humo_alto2)
        mask_humo = mask_humo1 + mask_humo2
        # Separamos la mascara del fondo
        res_humo = cv2.bitwise_and(img, img, mask=mask_humo)
        res_humo = cv2.cvtColor(res_humo, cv2.COLOR_BGR2RGB)

        #Llamado a la función para obtener los descriptes de la máscara------------------------------------------
        segmentacionDeRGB(res_humo,img,df,"humo")

        # Guardamos la mascara en el directorio especifico para mascaras de humo------------
        # cv2.imwrite(mascaras_humo + "/mascara_humo_rgb" + str(i).zfill(2) + ".png", res_humo)


        # ----------------NO INCENDIO-------------------------
        # Medidas en RGB para umbrales de no fuego
        umbral_nof_bajo0 = (10, 20, 5)
        umbral_nof_bajo1 = (30, 50, 20)
        umbral_nof_bajo2 = (40, 60, 30)

        umbral_nof_alto0 = (50, 50, 50)
        umbral_nof_alto1 = (70, 70, 40)
        umbral_nof_alto2 = (90, 140, 50)

        # Aplicamos los umbrales-----------------------------------------
        mask_nof0 = cv2.inRange(img, umbral_nof_bajo0, umbral_nof_alto0)
        mask_nof1 = cv2.inRange(img, umbral_nof_bajo1, umbral_nof_alto1)
        mask_nof2 = cv2.inRange(img, umbral_nof_bajo2, umbral_nof_alto2)
        mask_nof = mask_nof0 + mask_nof1 + mask_nof2
        
        # Separamos la mascara del fondo----------------------------------
        res_nof = cv2.bitwise_and(img, img, mask=mask_nof)
        res_nof = cv2.cvtColor(res_nof, cv2.COLOR_BGR2RGB)

        #Llamado a la función para obtener los descriptes de la máscara------------------------------------------
        segmentacionDeRGB(res_nof,img,df,"no_fuego")

        # Guardamos la mascara en el directorio especifico para mascaras de no fuego-----------
        # cv2.imwrite(mascaras_nof + "/mascara_nof_rgb" + str(i).zfill(2) + ".png", res_nof)



    # Para el archivo .csv (dataframe) quitamos el índice y lo guardamos en un directorio especifico.------------
    df=df.set_index('meanR')
    df.to_csv("./csvsAnalisis/descriptores.csv")


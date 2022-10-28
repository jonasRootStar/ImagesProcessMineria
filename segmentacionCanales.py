import cv2
import numpy as np
import pandas as pd



def segmentacionDeRGB(mascara_resultado, imagen, df, clase):
    """
    Funcion para poder obtener una lista de RGB de cada una de las mascaras
    de las imagenes. Recibe como parametro la mascara a la cual se le va
    a extrar los valores mayores a cero.
    """

    #Separación por canales
    imgHSV= cv2.cvtColor(imagen,cv2.COLOR_RGB2HSV)
    (R, G, B) = cv2.split(mascara_resultado)
    (H, S, V) =cv2.split(imgHSV)
    channels=[R,G,B]
    #Vectores de canales
    cleanR=[]
    cleanG=[]
    cleanB=[]
    cleanS=[]
    cleanV=[]
    #imgHSV=cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    #Eliminación de ceros en las matrices.
    for count,channel in enumerate(channels):
        for i in range(len(channel)):
            for j in range(len(channel[i])):
                #Limpieza de canal R
                if channel[i][j]!=0 and count==0:
                    cleanR.append(channel[i][j])
                    cleanS.append(S[i][j])
                    cleanV.append(V[i][j])
                #Limpieza de canal G
                elif channel[i][j]!=0 and count==1:
                    cleanG.append(channel[i][j])
                    cleanS.append(S[i][j])
                    cleanV.append(V[i][j])
                #Limpieza de canal B
                elif channel[i][j]!=0 and count==2:
                    cleanB.append(channel[i][j])
                    cleanS.append(S[i][j])
                    cleanV.append(V[i][j])



    df.loc[len(df)] = [round(np.mean(R), 4), round(np.mean(G), 4), round(np.mean(B), 4),round(np.mean(S),4),round(np.mean(V),4),round(np.std(R),4),round(np.std(G),4),round(np.std(B),4), round(np.std(S),4), round(np.std(V),4), clase]



    
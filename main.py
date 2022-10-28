# Importamos las funciones principales de cada uno de los scripts.
from deteccionTwo import deteccionMascarasImagenes
from blurImages import aplicacionDeBlur
from openImage import formatoDeImagenes


# Mandamos a llamar a cada una de las funciones de los scripts, en el orden 
# el cual deben ser ejecutadas:
# 1) Dar formato de nombre a las imagenes.
# 2) Aplicar el filtro a cada una de las imagenes.
# 3) Procesamiento de las imagenes para poder extraer la información necesaria.
#       Este script contiene la función necesaria para poder extraer los datos numéricos que 
#       servirán para poder tener el valor de cada uno de los descriptores.
if __name__ == "__main__":
    formatoDeImagenes()
    aplicacionDeBlur()
    deteccionMascarasImagenes()
    


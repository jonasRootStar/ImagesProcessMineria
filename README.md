# ImagesProcessMineria
El presente trabajo tiene como objetivo la extracción de información necesaria para poder entrenar una red neuronal que sea capaz de predecir de la mejor
forma posible casos de ***incendios forestales***, todo esto haciendo uso de la información extraida de una determinada muestra que ha sifdo útil para este caso.
Esta primera parte de lo que será el proyecto final, ha sido dividida en dos secciones:

1) Procesamiento de imágenes y extracción de descriptores.
2) Inserción del archivo con los descriptores en el software ***Weka***, para poder hacer uso de la red neuronal Perseptron.

A continuación una serie de pasos y/o puntos importante, los cuales son necesarios para que el projecto funcione de la mejor forma posible:
1) [Instalación de las librerias.](#instalacion)
2) [Descripción de cada uno de los scripts que conforman el proyecto y de sus funciones.](#descripcion-scripts)
3) [Formato del dataframe para poder usarlo en Weka.](#formato)

***

<a name="instalacion"></a>
## Instalación de las librerias
Para que el proyecto pueda funcionar debidamente, necesitamos hacer uso de las siguientes librerias:
1. Pandas.
La cual nos ayudará en el apartado del `dataframe`, es decir, para poder manipularlo.
2. Numpy.
Ayudará para poder hacer distintas operaciones como la media y desviación de los valores obtenidos de la extracción de descriptores.
3. OpenCV (cv2).
Sin duda la más importante, ya que sin ella no podremos manipular y hacer le tratamiento de las imágenes.
##### Instalación de librerias:
Al tratarse de un proyecto el cual es en su mayoria Python, es recomendable hacer la isntalación de las librerias en un ***ambiente virtual de Python***.
Revisar la siguiente liga para conocer cómo crear un [ambiente virtual de Python.](https://docs.python.org/3/library/venv.html)

```
pip install cv2
pip install numpy
pip install pandas
```

Despúes de completar la instalación de las librerias podemos continuar con el proceso de ejecución del proyecto.

***

<a name="descripcion-scripts"></a>
## Descripción de cada uno de los scripts que conforman el proyecto y sus funciones.
El proyecto se compone de 5 scripts importantes para el funcionamiento, todos deben de ser ejecutados. Cabe recalcar que uno de estos es ejecutado dentro de otro
script diferente al principal.
El orden de los scripts es el siguiente:
1. `Main.py`: Su función principal es la de ejecutar todos los siguientes scripts. Importa las funciones de los otros scripts.
2. `openImage.py`: Su función es darle el formato de nombre y tipo a cada una de las imágenes a tratar. Necesita la dirección raíz del directorio en el que se
encuentran las imágenes a formatear. Es sumamente importante tener la dirección especifica clara. Además crea un directorio nuevo dentro del directorio de trabajo
donde se guardaran las imagenes formateadas, este recibe el nombre de `imagenes_salida`. Todas las imagenes tendran la extensión `.png`.
3. `blurImages.py`: Le aplica el filtro de ***blur*** a cada una de las imágenes que ya han sido formateadas. Entra al directorio anterior donde han sido guardadas las 
imágenes formateadas para poder aplicarles a cada una el filtro de blur. Estas imagenes serán guradadas en este mismo directorio.
4. `deteccionTwo.py`: Su función principal es la de recorrer cada una de las imágenes y extraer sus *máscaras de fuego, humo y no fuego*, esto con base a ciertos
valores de umbrales para cada uno de los casos, para esto fue utilizado `matplotlib` y poder tener los valores en RGB de las partes que deseabamos extraer.
Dentro de este mismo script se hace el llamado de la función `segmentacionDeRGB` del script `segmentacionCanales.py`. Esta función recorre las matrices de valores RGB
de cada imagen conservando unicamente los valores que no contengan 0 cero, ya que estos resultan iservibles para los cálculos necesarios. Además aplica operaciones 
de estadistica cuyos resultados que serán tomados como los valores de descriptores.

Al finalizar la ejecución se guardaran los datos dentro de un dataframe `descriptores.csv` el cual recibirá el formateo para poder ser usado en el programa de Weka.

***

<a name="formato"></a>
## Formato del dataframe para poder usarlo en Weka.
Al terminar el tratamiento de las imágenes y tener lista la información requerida, tenemos que hacer un paso importante para poder ingresar dicha información 
al programa de Weka, este resulta en darle el formato de documento `.arff`, debe tener el siguiente formato:

```
@relation 'PARCIAL'

@attribute meanR numeric
@attribute meanG numeric
@attribute meanB numeric
@attribute meanS numeric
@attribute meanV numeric
@attribute stdR numeric
@attribute stdG numeric
@attribute stdB numeric
@attribute stdS numeric
@attribute stdV numeric
@attribute clase {'fuego', 'humo', 'no_fuego'}

@data

NOTA: en la data se le debe poner ' ' a cada valor de clase.
```

***

Con este último paso terminamos el tratamiento y extracción de los descriptores y sus valores. Podemos continuar al paso dos del proyecto, el cual es llevar la 
información al programa Weka para poder entrenar la red neuronal.

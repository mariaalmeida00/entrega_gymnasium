# ENTREGA TRABAJO GYMNASIUM
Nombre: María Almeida Escobar
NIA: 100406453
Estudios: Máster Universitario en Robótica y Automatización

## Entrega básica:
- El programa es capaz de llevar al robot desde la posición inicial hasta la posición pedida (GOAL) de forma autónoma, planificando primero la trayectoria mediante el archivo rescatado de una entrega anterior de la asignatura de *Introducción a la Planificación de Robots* de este mismo máster. Este fichero es ***examples/trajectory_alg.py***.

## Extras:
- Se ha modificado la línea 17 del archivo con path ***entrega_gymnasium/gymnasium-csv-026/gymnasium_csv/envs/__init__.py*** para que la ventana de visualización se adaptara adecuadamente a las dimensiones de la pantalla de cualquier PC utilizado en el archivo ***entrega_gymnasium/gymnasium-csv-026/gymnasium_csv/envs/__init__.py***, como se muestra a continuación. Para ello se ha utilizado la librería *subprocess*. Por si hubiera algún problema al importarla o no existiera, se ha creado una excepción. Las dimensiones permanecerán como se escribieron por defecto en caso de no conseguir obtener las dimensiones de la pantalla:
```
# Lines [5 - 9]
try:
    import subprocess
    IMPORT_SUCCESS = True
except:
    IMPORT_SUCCESS = False

# Lines [22 - 29]
if IMPORT_SUCCESS:
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    resol_w = int(resolution[0])
    resol_h = int(resolution[1])
    MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT = resol_w - 70, resol_h - 70
else:
    MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT = 1920, 1080
```
- Se ha modificado la estética de la pantalla de visualización, tanto los colores del fondo y de las paredes, como del robot y la posición objetivo (GOAL) en el archivo ***entrega_gymnasium/gymnasium-csv-026/gymnasium_csv/envs/__init__.py***, como se muestra a continuación:
```
# Lines [31 - 34]
COLOR_BACKGROUND = (64, 33, 130)
COLOR_WALL = (61, 190, 169)
COLOR_ROBOT = (225, 179, 255)
COLOR_GOAL = (255, 250, 222)
```
- Se han creado 2 nuevos mapas (map2 y map3, siendo este último el de mayor complejidad).

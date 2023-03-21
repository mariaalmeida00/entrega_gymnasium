# ENTREGA TRABAJO GYMNASIUM
## Datos del alumno/a:
Nombre: María Almeida Escobar
NIA: 100406453
Estudios: Máster Universitario en Robótica y Automatización
Repositorio: https://github.com/mariaalmeida00/entrega_gymnasium.git

## Entrega básica:
- El programa es capaz de llevar al robot desde la posición inicial hasta la posición pedida (GOAL) de forma autónoma, planificando primero la trayectoria mediante el archivo rescatado de una entrega anterior de la asignatura de *Introducción a la Planificación de Robots* de este mismo máster. Este fichero es ***examples/trajectory_alg.py***. El archivo que debe lanzarse es el ***examples/my_code.py***.
```
python3 my_code.py
```
![MAPA 1 (básico): map1.csv](/assets/pictures/map1.png)

## Extras:
- Se ha modificado el archivo con path ***gymnasium_csv/envs/grid_world.py*** para que la ventana de visualización se adaptara adecuadamente a las dimensiones de la pantalla de cualquier PC utilizado, como se muestra a continuación. Para ello se ha utilizado la librería *subprocess*. Por si hubiera algún problema al importarla o no existiera, se ha creado una excepción. Las dimensiones permanecerán como se escribieron por defecto en caso de no conseguir obtener las dimensiones de la pantalla:
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
- Se han creado 2 nuevos mapas (map2 y map3, siendo este último el de mayor complejidad):
![MAPA 2: map2.csv](/assets/pictures/map2.png)
![MAPA 3: map2.csv](/assets/pictures/map3.png)
- Se tienen los siguentes argumentos que es posible introducir por terminal al lanzar el archivo **my_code.py** (se escribe el argumento con su valor por defecto a la derecha). De esta forma, es posible elegir por terminal un punto de inicio o final distintos a los predefinidos:
    - [--start_x START_X]
    - [--start_y START_Y]
    - [--end_x END_X]
    - [--end_y END_Y]
    - [--custom_map CUSTOM_MAP] Este argumento permite utilizar un mapa distinto. Si se quiere utilizar el mapa 2, sería: --custom_map=map2
    - [--sim_speed SIM_SPEED] Este argumento permite modificar la velocidad de avance de la simulación, dentro de unos límites establecidos. Si se desea que la simulación vaya más deprisa, podemos introducir: --sim_speed=2. De lo contrario: --sim_speed=0.5.

- Se pregunta al usuario por terminal si este quiere jugar. Si se responde con un valor distinto de 0, entonces el usuario será el que tome el control del robot y podrá enviarle órdenes por teclado (usando el teclado numérico, como se explica). Si el valor de respuesta es 0, entonces el robot irá hasta la meta de forma autónoma. En cualquiera de los dos casos, si el robot chocara con alguna pared, se mostraría un "Oh, no... GAME OVER" y se cerraría la simulación.

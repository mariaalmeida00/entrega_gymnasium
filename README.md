# ENTREGA TRABAJO GYMNASIUM
Nombre: María Almeida Escobar
NIA: 100406453
Estudios: Máster Universitario en Robótica y Automatización

Se ha modificado la línea 17 del archivo con path ***entrega_gymnasium/gymnasium-csv-026/gymnasium_csv/envs/__init__.py*** para que la ventana de visualización se adaptara adecuadamente a las dimensiones de la pantalla del PC utilizado:

```
MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT = 1366, 768 #1920, 1080
```

## Extras:
- Se ha modificado la estética de la pantalla de visualización, tanto los colores del fondo y de las paredes, como del robot y la posición objetivo (GOAL) en el archivo ***entrega_gymnasium/gymnasium-csv-026/gymnasium_csv/envs/__init__.py***, como se muestra a continuación:
```
MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT = 1366, 768 #1920, 1080
COLOR_BACKGROUND = (64, 33, 130)
COLOR_WALL = (61, 190, 169)
COLOR_ROBOT = (225, 179, 255)
COLOR_GOAL = (255, 250, 222)
```
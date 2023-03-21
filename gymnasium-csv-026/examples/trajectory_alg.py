#! /usr/bin/env python

## A nivel mapa
### Del mapa original
### * 0: libre
### * 1: ocupado (muro/obstáculo)
### Nós
### * 2: visitado
### * 3: start
### * 4: goal

## A nivel grafo
### Nós
### * -2: parentId del nodo start
### * -1: parentId del nodo goal PROVISIONAL cuando aun no se ha resuelto

## Initial values are hard-coded (A nivel mapa)

FILE_NAME = '../assets/map1.csv'
START_X = 1
START_Y = 1
END_X = 11
END_Y = 11

## creamos estructura de datos para mapa
charMap = []

def getInitialData(f_name, s_x, s_y, e_x, e_y):
    global FILE_NAME
    global START_X
    global START_Y
    global END_X
    global END_Y
    global charMap
    charMap = []
    FILE_NAME = f_name
    START_X = s_x
    START_Y = s_y
    END_X = e_x
    END_Y = e_y
    print([START_X,START_Y],'------->',[END_X,END_Y])

## creamos función para volcar estructura de datos para mapa

def dumpMap():
    '''for line in charMap:
        print(line)'''
    pass

## Define Node class (A nivel grafo/nodo)

class Node:
    def __init__(self, x, y, myId, parentId):
        self.x = x
        self.y = y
        self.myId = myId
        self.parentId = parentId
    def dump(self):
        print("---------- x "+str(self.x)+\
                         " | y "+str(self.y)+\
                         " | id "+str(self.myId)+\
                         " | parentId "+str(self.parentId))

def executeAlgorithm(map_file, init_x, init_y, obj_x, obj_y):
    global FILE_NAME
    global charMap
    global START_X
    global START_Y
    global END_X
    global END_Y
    START_X = init_x
    START_Y = init_y
    END_X = obj_x
    END_Y = obj_y
    FILE_NAME = map_file
    print(' ~~~~~~~~~~~~~~~~~~~~ TRAJECTORY PLANIFICATION ~~~~~~~~~~~~~~~~~~~~ ')
    ## `nodes` contendrá los nodos del grafo
    nodes = []

    ## creamos primer nodo
    init = Node(START_X, START_Y, 0, -2)
    # init.dump()  # comprobar que primer nodo bien

    ## añadimos el primer nodo a `nodos`

    nodes.append(init)

    ## de fichero, (to parse/parsing) para llenar estructura de datos para mapa

    with open(FILE_NAME) as f:
        line = f.readline()
        while line:
            charLine = line.strip().split(',')
            charMap.append(charLine)
            line = f.readline()

    ## a nivel mapa, integramos la info que teníamos de start & end

    charMap[START_X][START_Y] = '3' # 3: start
    charMap[END_X][END_Y] = '4' # 4: goal

    print(' ~~~~~~~~ First part: breadth-first search (BFS) algorithm ~~~~~~~~ ')
    ## volcamos mapa por consola
    dumpMap()

    ###### Empieza algoritmo

    done = False  # clásica condición de parada del bucle `while`
    goalParentId = -1  # -1: parentId del nodo goal PROVISIONAL cuando aun no se ha resuelto

    while not done:
        print("--------------------- number of nodes: "+str(len(nodes)))
        for node in nodes:
            node.dump()

            # up
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId  # aquí sustituye por real
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            # down
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId # aquí sustituye por real
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            # right
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId # aquí sustituye por real
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            # left
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId # aquí sustituye por real
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            dumpMap()

    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(' ~~~~~~~ Second part: get instructions and objective points ~~~~~~~ ')
    objectives_coords_aux = [[END_X, END_Y]]
    ok = False

    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                node.dump()
                next_node = node
                current_node = nodes[node.parentId]
                objectives_coords_aux.append([node.x, node.y])
                goalParentId = node.parentId
                if( goalParentId == -2):
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                    ok = True

    # TRAJECTORY PLANIFICATION
    objectives_coords_aux = list(reversed(objectives_coords_aux))

    instructions_aux = []

    for i in range(1,len(objectives_coords_aux)-1):
        if objectives_coords_aux[i][0] > objectives_coords_aux[i-1][0]:
            instructions_aux.append('down')
        elif objectives_coords_aux[i][0] < objectives_coords_aux[i-1][0]:
            instructions_aux.append('up')
        elif objectives_coords_aux[i][1] > objectives_coords_aux[i-1][1]:
            instructions_aux.append('right')
        elif objectives_coords_aux[i][1] < objectives_coords_aux[i-1][1]:
            instructions_aux.append('left')


    instructions = [instructions_aux[0]]
    objectives_coords = []

    for i in range(1, len(instructions_aux)):
        #print('\n',instructions_aux[i-1],'--->', instructions_aux[i], end=':')
        if instructions_aux[i] != instructions_aux[i-1]:
            instructions.append(instructions_aux[i])
            objectives_coords.append(objectives_coords_aux[i])
            #print('ADD!!')

    objectives_coords.append([END_X,END_Y])
    #print(instructions_aux)
    #print(objectives_coords_aux)
    #print(instructions)
    #print(objectives_coords)

    return instructions, objectives_coords

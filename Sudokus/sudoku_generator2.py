import pygame
import sys

solveable_grid =   [[4, 0, 0, 8, 0, 0, 0, 0, 0],
                    [0, 9, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 2, 0, 8, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 7],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

solveable_grid2 = [[8,0,0,0,0,0,0,0,0],
                  [0,0,3,6,0,0,0,0,0],
                  [0,7,0,0,9,0,2,0,0],
                  [0,5,0,0,0,7,0,0,0],
                  [0,0,0,0,4,5,7,0,0],
                  [0,0,0,1,0,0,0,3,0],
                  [0,0,1,0,0,0,0,6,8],
                  [0,0,8,5,0,0,0,1,0],
                  [0,9,0,0,0,0,4,0,0]]

empty_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

COLUMN_COUNT = 9
ROW_COUNT = 9

solved = False


def buscar_cero(grid):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if grid[row][col] == 0:
                coordenada = (row, col)
                return coordenada
    return solved == True


def calcular_posibilidades(grid, cell):
    posibilidades_ideales = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # print("Posibilidades al iniciar: ", posibilidades_ideales)
    row, col = cell

    #Revisar row
    for number in grid[row]:
        if number in posibilidades_ideales:
            indice = posibilidades_ideales.index(number)
            posibilidades_ideales.pop(indice)
    # print ("Posibilidades luego de revisar fila: ", posibilidades_ideales)

    # Revisar col
    columna_a_revisar = []
    for rows in grid:
        valor_a_comparar = rows[col]
        columna_a_revisar.append(valor_a_comparar)
        if valor_a_comparar in posibilidades_ideales:
            indice = posibilidades_ideales.index(valor_a_comparar)
            posibilidades_ideales.pop(indice)
    # print("Posibilidades luego de revisar columna: ", posibilidades_ideales)

    # Revisar square
    # Crear lista de cuadrantes
    lista_de_cuadrantes = []
    tuple = [(0, 3), (3, 6), (6, 9)]
    for combinacion in tuple:
        for combinacion2 in tuple:
            cuadrante = (combinacion, combinacion2)
            lista_de_cuadrantes.append(cuadrante)


    # Encontrar el cuadrante donde se ubica la celda objetivo
    for cuadrante in lista_de_cuadrantes:
        rango_fila, rango_columna = cuadrante
        lim_inf_fila, lim_sup_fila = rango_fila
        lim_inf_columna, lim_sup_columna = rango_columna
        if (row >= lim_inf_fila and row < lim_sup_fila) and (col >= lim_inf_columna and col < lim_sup_columna):
            cuadrado = cuadrante

    # Redefinir los límites
    rango_fila, rango_columna = cuadrado
    lim_inf_fila, lim_sup_fila = rango_fila
    lim_inf_columna, lim_sup_columna = rango_columna

    # Revisar el cuadrado en cuestión
    cuadrado_a_revisar = []
    for fila in range(lim_inf_fila, lim_sup_fila):
        for columna in range(lim_inf_columna, lim_sup_columna):
            valor = grid[fila][columna]
            cuadrado_a_revisar.append(valor)
    for item in cuadrado_a_revisar:
        if item in posibilidades_ideales:
            indice = posibilidades_ideales.index(item)
            posibilidades_ideales.pop(indice)
    # print("Posibilidades luego de revisar cuadrado: ", posibilidades_ideales)

    return posibilidades_ideales

contador = []
def resolver_sudoku(grid):

    SQUARE_SIZE = 70
    GRID_SIZE = 9
    FONT_SIZE = 40
    GREY = (220,220,220)
    MIDDLE_GREY = (200, 200, 200)
    DARK_GREY = (169, 169, 169)
    BLACK = (0, 0, 0)

    def show(grid, screen, contador):


        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):

                myfont = pygame.font.SysFont("roboto", FONT_SIZE)

                # Implementar función de que si la celda está junto al cero, las letras se ponen verdes
                pygame.draw.rect(screen, GREY, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))       
                if grid[r][c] != 0:                    
                    label = myfont.render(str(grid[r][c]), 1, BLACK)
                    screen.blit(label, (int(c*SQUARE_SIZE+SQUARE_SIZE/3), int(r*SQUARE_SIZE+ SQUARE_SIZE/3))) 
                else:
                    pygame.draw.rect(screen, DARK_GREY, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, DARK_GREY, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 7)

        label = myfont.render(str(len(contador)), 1, GREY)
        screen.blit(label, (10, ((SQUARE_SIZE+1)*GRID_SIZE)))

        print("***********************")
        for filas in grid:
            print (filas)
        print("***********************")



    pygame.init()
    height = SQUARE_SIZE * (GRID_SIZE+2)
    width = SQUARE_SIZE * GRID_SIZE
    screen_size = (width, height)
    screen = pygame.display.set_mode(screen_size)
   

    celda_objetivo = buscar_cero(grid)
    row, col = celda_objetivo
    print(celda_objetivo)
    lista_probables = calcular_posibilidades(grid, celda_objetivo)

    print(lista_probables)
    contador.append(1)
    print(len(contador))

    show(grid, screen, contador)
    pygame.display.update()

    for item in range(len(lista_probables)):
        print (lista_probables[item])
        if not lista_probables[item] == 0:
            grid[row][col] = lista_probables[item]

            resolver_sudoku(grid)

    grid[row][col] = 0

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

resolver_sudoku(empty_grid)
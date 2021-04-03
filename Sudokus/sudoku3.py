import random
import copy

def random_available(list):
   return random.choice(list)


class Sudoku(object):
    def __init__(self):
        self.grid = [[1,0,7,0,0,4,0,0,0],
                     [0,2,9,0,0,0,0,0,0],
                     [4,0,3,0,0,0,0,9,0],
                     [5,0,0,4,0,0,0,0,0],
                     [0,0,0,0,5,0,0,0,0],
                     [0,0,4,0,0,6,0,0,0],
                     [6,0,0,0,0,0,7,0,0],
                     [0,0,0,0,0,0,0,8,0],
                     [0,0,8,0,0,0,0,0,9]]

        self.vacias()
        self.dict_availables()

    def show(self):
        for i in range(3):
            print(self.grid[i][0], end=" ")
            print(self.grid[i][1], end=" ")
            print(self.grid[i][2], "|", end=" ")
            print(self.grid[i][3], end=" ")
            print(self.grid[i][4], end=" ")
            print(self.grid[i][5], "|", end=" ")
            print(self.grid[i][6], end=" ")
            print(self.grid[i][7], end=" ")
            print(self.grid[i][8], end=" ")
            print()
        print("---------------------")

        for i in range(3, 6):
            print(self.grid[i][0], end=" ")
            print(self.grid[i][1], end=" ")
            print(self.grid[i][2], "|", end=" ")
            print(self.grid[i][3], end=" ")
            print(self.grid[i][4], end=" ")
            print(self.grid[i][5], "|", end=" ")
            print(self.grid[i][6], end=" ")
            print(self.grid[i][7], end=" ")
            print(self.grid[i][8], end=" ")
            print()
        print("---------------------")

        for i in range(6, 9):
            print(self.grid[i][0], end=" ")
            print(self.grid[i][1], end=" ")
            print(self.grid[i][2], "|", end=" ")
            print(self.grid[i][3], end=" ")
            print(self.grid[i][4], end=" ")
            print(self.grid[i][5], "|", end=" ")
            print(self.grid[i][6], end=" ")
            print(self.grid[i][7], end=" ")
            print(self.grid[i][8], end=" ")
            print()
        print()

    def vacias(self):
        self.vacias = []
        for i in range(9):
            for j in range(9):
                if self.grid[i][j]==0:
                    self.vacias.append((i, j))
        return self.vacias

    def show_vacias(self):
        for i in self.vacias:
            print(i)

    def dict_availables(self):

        def column(matrix, i):
            return [row[i] for row in matrix]

        def square(cell):
            row, col = cell
            cuadrantes = []
            tupla = [(0, 3),(3, 6),(6, 9)]

            for i in tupla:
                for j in tupla:
                    cuadrantes.append((i,j))

            # Encontrar el cuadrante donde se ubica la celda objetivo
            for cuad in cuadrantes:
                filas, columnas = cuad
                min_fila, max_fila = filas
                min_col, max_col = columnas
                if (row >= min_fila and row < max_fila) and (col >= min_col and col < max_col):
                    cuadrado = cuad


                    rows, cols = cuadrado


                        # Revisar el cuadrado en cuestión
                    cuadrado_a_revisar = []
                    for fila in range(rows[0], rows[1]):
                        for columna in range(cols[0], cols[1]):
                            valor = self.grid[fila][columna]
                            cuadrado_a_revisar.append(valor)

                    return(cuadrado_a_revisar)
     

        def check_availability(cell):
            availability = [1,2,3,4,5,6,7,8,9]
            r, c = cell
            
            # check row
            row = self.grid[r]
            for v in row:
                if v in availability:
                    index = availability.index(v)
                    availability.pop(index)

            # check cols

            col = column(self.grid, r)
            for v in col:
                if v in availability:
                    index = availability.index(v)
                    availability.pop(index)

            # check squares
            sq = square(cell)
            for v in sq:
                if v in availability:
                    index = availability.index(v)
                    availability.pop(index)
            
            return availability

        self.mapa = {}
        for i in self.vacias:
            self.mapa[i] = check_availability(i)
        return self.mapa

    def show_availables(self):
        print(self.dict_availables())

    def resolver(self):


        for i in self.vacias:
            r, c = i
            avs = self.dict_availables()[i]
            for i in range(8):
                if len(avs) == i:
                    print(i, avs)





    # def armar_sudoku(self):
    #
    #     for i in self.vacias:
    #         availables = self.check_availability(i)
    #         i = self.random_available(availables)







juego = Sudoku()
juego.show()
juego.resolver()

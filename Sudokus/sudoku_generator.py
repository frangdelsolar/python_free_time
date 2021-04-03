import random



class Celda:
    def __init__(self, posicion, valor = 0):
        self.valores_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.posicion = posicion
        self.square = None
        self.valor = valor
        self.solved = False
        self.squarize(posicion)
        self.vecinos = []

    def squarize(self, posicion):
        if (self.posicion in range(4)) or (self.posicion in range(10, 13)) or (self.posicion in range(19, 22)):
            self.square = 1
        if (self.posicion in range(4, 7)) or (self.posicion in range(13, 16)) or (self.posicion in range(22, 25)):
            self.square = 2
        if (self.posicion in range(7, 10)) or (self.posicion in range(16, 19)) or (self.posicion in range(25, 28)):
            self.square = 3

        if (self.posicion in range(28, 31)) or (self.posicion in range(37, 40)) or (self.posicion in range(46, 49)):
            self.square = 4
        if (self.posicion in range(31, 34)) or (self.posicion in range(40, 43)) or (self.posicion in range(49, 52)):
            self.square = 5
        if (self.posicion in range(34, 37)) or (self.posicion in range(43, 46)) or (self.posicion in range(52, 55)):
            self.square = 6

        if (self.posicion in range(55, 58)) or (self.posicion in range(64, 67)) or (self.posicion in range(73, 76)):
            self.square = 7
        if (self.posicion in range(58, 61)) or (self.posicion in range(67, 70)) or (self.posicion in range(76, 79)):
            self.square = 8
        if (self.posicion in range(61, 64)) or (self.posicion in range(70, 73)) or (self.posicion in range(79, 82)):
            self.square = 9

    def dar_valor(self):
        return self.valor

    def dar_posibles(self):
        return self.valores_posibles

    def dar_posicion(self):
        return self.posicion

    def dar_square(self):
        return self.square



class Sudoku:
    def __init__(self):
        self.celdas = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.build()
        # self.random_a_cell()
        self.eliminar_posibles()
        # self.buscar_cero()



    def build(self):
        posicion = 1
        for i in range(9):
            for j in range(9):
                self.celdas[i][j] = Celda(posicion)
                posicion += 1

    def show_posicion(self):
        for i in range(3):
            print(self.celdas[i][0].dar_posicion(), end =" ")
            print(self.celdas[i][1].dar_posicion(), end =" ")
            print(self.celdas[i][2].dar_posicion(), "|", end=" ")
            print(self.celdas[i][3].dar_posicion(), end=" ")
            print(self.celdas[i][4].dar_posicion(), end=" ")
            print(self.celdas[i][5].dar_posicion(), "|", end=" ")
            print(self.celdas[i][6].dar_posicion(), end=" ")
            print(self.celdas[i][7].dar_posicion(), end=" ")
            print(self.celdas[i][8].dar_posicion(), end=" ")
            print()
        print ("---------------------")

        for i in range(3, 6):
            print(self.celdas[i][0].dar_posicion(), end =" ")
            print(self.celdas[i][1].dar_posicion(), end =" ")
            print(self.celdas[i][2].dar_posicion(), "|", end=" ")
            print(self.celdas[i][3].dar_posicion(), end=" ")
            print(self.celdas[i][4].dar_posicion(), end=" ")
            print(self.celdas[i][5].dar_posicion(), "|", end=" ")
            print(self.celdas[i][6].dar_posicion(), end=" ")
            print(self.celdas[i][7].dar_posicion(), end=" ")
            print(self.celdas[i][8].dar_posicion(), end=" ")
            print()
        print("---------------------")

        for i in range(6, 9):
            print(self.celdas[i][0].dar_posicion(), end=" ")
            print(self.celdas[i][1].dar_posicion(), end=" ")
            print(self.celdas[i][2].dar_posicion(), "|", end=" ")
            print(self.celdas[i][3].dar_posicion(), end=" ")
            print(self.celdas[i][4].dar_posicion(), end=" ")
            print(self.celdas[i][5].dar_posicion(), "|", end=" ")
            print(self.celdas[i][6].dar_posicion(), end=" ")
            print(self.celdas[i][7].dar_posicion(), end=" ")
            print(self.celdas[i][8].dar_posicion(), end=" ")
            print()

    def show_squares(self):
        for i in range(3):
            print(self.celdas[i][0].dar_square(), end =" ")
            print(self.celdas[i][1].dar_square(), end =" ")
            print(self.celdas[i][2].dar_square(), "|", end=" ")
            print(self.celdas[i][3].dar_square(), end=" ")
            print(self.celdas[i][4].dar_square(), end=" ")
            print(self.celdas[i][5].dar_square(), "|", end=" ")
            print(self.celdas[i][6].dar_square(), end=" ")
            print(self.celdas[i][7].dar_square(), end=" ")
            print(self.celdas[i][8].dar_square(), end=" ")
            print()
        print ("---------------------")

        for i in range(3, 6):
            print(self.celdas[i][0].dar_square(), end =" ")
            print(self.celdas[i][1].dar_square(), end =" ")
            print(self.celdas[i][2].dar_square(), "|", end=" ")
            print(self.celdas[i][3].dar_square(), end=" ")
            print(self.celdas[i][4].dar_square(), end=" ")
            print(self.celdas[i][5].dar_square(), "|", end=" ")
            print(self.celdas[i][6].dar_square(), end=" ")
            print(self.celdas[i][7].dar_square(), end=" ")
            print(self.celdas[i][8].dar_square(), end=" ")
            print()
        print("---------------------")

        for i in range(6, 9):
            print(self.celdas[i][0].dar_square(), end=" ")
            print(self.celdas[i][1].dar_square(), end=" ")
            print(self.celdas[i][2].dar_square(), "|", end=" ")
            print(self.celdas[i][3].dar_square(), end=" ")
            print(self.celdas[i][4].dar_square(), end=" ")
            print(self.celdas[i][5].dar_square(), "|", end=" ")
            print(self.celdas[i][6].dar_square(), end=" ")
            print(self.celdas[i][7].dar_square(), end=" ")
            print(self.celdas[i][8].dar_square(), end=" ")
            print()

    def show_valores(self):
        print()
        for i in range(3):
            print(self.celdas[i][0].dar_valor(), end =" ")
            print(self.celdas[i][1].dar_valor(), end =" ")
            print(self.celdas[i][2].dar_valor(), "|", end=" ")
            print(self.celdas[i][3].dar_valor(), end=" ")
            print(self.celdas[i][4].dar_valor(), end=" ")
            print(self.celdas[i][5].dar_valor(), "|", end=" ")
            print(self.celdas[i][6].dar_valor(), end=" ")
            print(self.celdas[i][7].dar_valor(), end=" ")
            print(self.celdas[i][8].dar_valor(), end=" ")
            print()
        print ("---------------------")

        for i in range(3, 6):
            print(self.celdas[i][0].dar_valor(), end =" ")
            print(self.celdas[i][1].dar_valor(), end =" ")
            print(self.celdas[i][2].dar_valor(), "|", end=" ")
            print(self.celdas[i][3].dar_valor(), end=" ")
            print(self.celdas[i][4].dar_valor(), end=" ")
            print(self.celdas[i][5].dar_valor(), "|", end=" ")
            print(self.celdas[i][6].dar_valor(), end=" ")
            print(self.celdas[i][7].dar_valor(), end=" ")
            print(self.celdas[i][8].dar_valor(), end=" ")
            print()
        print("---------------------")

        for i in range(6, 9):
            print(self.celdas[i][0].dar_valor(), end=" ")
            print(self.celdas[i][1].dar_valor(), end=" ")
            print(self.celdas[i][2].dar_valor(), "|", end=" ")
            print(self.celdas[i][3].dar_valor(), end=" ")
            print(self.celdas[i][4].dar_valor(), end=" ")
            print(self.celdas[i][5].dar_valor(), "|", end=" ")
            print(self.celdas[i][6].dar_valor(), end=" ")
            print(self.celdas[i][7].dar_valor(), end=" ")
            print(self.celdas[i][8].dar_valor(), end=" ")
            print()
        print()

    def show_posibles(self):
        for i in range(3):
            print(self.celdas[i][0].dar_posibles(), end =" ")
            print(self.celdas[i][1].dar_posibles(), end =" ")
            print(self.celdas[i][2].dar_posibles(), "|", end=" ")
            print(self.celdas[i][3].dar_posibles(), end=" ")
            print(self.celdas[i][4].dar_posibles(), end=" ")
            print(self.celdas[i][5].dar_posibles(), "|", end=" ")
            print(self.celdas[i][6].dar_posibles(), end=" ")
            print(self.celdas[i][7].dar_posibles(), end=" ")
            print(self.celdas[i][8].dar_posibles(), end=" ")
            print()
        print ("---------------------")

        for i in range(3, 6):
            print(self.celdas[i][0].dar_posibles(), end =" ")
            print(self.celdas[i][1].dar_posibles(), end =" ")
            print(self.celdas[i][2].dar_posibles(), "|", end=" ")
            print(self.celdas[i][3].dar_posibles(), end=" ")
            print(self.celdas[i][4].dar_posibles(), end=" ")
            print(self.celdas[i][5].dar_posibles(), "|", end=" ")
            print(self.celdas[i][6].dar_posibles(), end=" ")
            print(self.celdas[i][7].dar_posibles(), end=" ")
            print(self.celdas[i][8].dar_posibles(), end=" ")
            print()
        print("---------------------")

        for i in range(6, 9):
            print(self.celdas[i][0].dar_posibles(), end=" ")
            print(self.celdas[i][1].dar_posibles(), end=" ")
            print(self.celdas[i][2].dar_posibles(), "|", end=" ")
            print(self.celdas[i][3].dar_posibles(), end=" ")
            print(self.celdas[i][4].dar_posibles(), end=" ")
            print(self.celdas[i][5].dar_posibles(), "|", end=" ")
            print(self.celdas[i][6].dar_posibles(), end=" ")
            print(self.celdas[i][7].dar_posibles(), end=" ")
            print(self.celdas[i][8].dar_posibles(), end=" ")
            print()

    def random_a_cell(self):
        i, j = random.randint(0,8), random.randint(0,8)
        v = random.randint(1,9)
        self.celdas[i][j].valor = v
        self.celdas[i][j].solved = True

    def eliminar_posibles(self):

        #Recorrer cada celda
        for i in range(9):
            for j in range(9):
                celda_objetivo = self.celdas[i][j]

                #Revisar fila
                row = []
                for f in range(9):
                    row.append(self.celdas[f][j].valor)
                for item in row:
                    if item in celda_objetivo.valores_posibles:
                        index = celda_objetivo.valores_posibles.index(item)
                        celda_objetivo.valores_posibles.pop(index)


                #Revisar columna
                col = []
                for c in range(9):
                    col.append(self.celdas[i][c].valor)
                for item in col:
                    if item in celda_objetivo.valores_posibles:
                        index = celda_objetivo.valores_posibles.index(item)
                        celda_objetivo.valores_posibles.pop(index)

                #Revisar cuadrado
                cuadro = []
                cel_sq = self.celdas[i][j].square
                for fi in range(9):
                    for co in range(9):
                        if self.celdas[fi][co].square == cel_sq:
                            cuadro.append(self.celdas[fi][co].valor)
                for item in cuadro:
                    if item in celda_objetivo.valores_posibles:
                        index = celda_objetivo.valores_posibles.index(item)
                        celda_objetivo.valores_posibles.pop(index)

    def jugar(self):
        while True:
            self.show_valores()
            x = int(input("Fila (1 a 9): "))
            y = int(input("Columna (1 a 9): "))

            if self.celdas[x][y].solved == True:
                print("Esa celda ya está resuelta.")
            else:
                print()
                print("Valores posibles: ", self.celdas[x][y].valores_posibles)
                print()
                user_valor = int(input("Valor(1 a 9): "))
                if not (user_valor in self.celdas[x][y].valores_posibles):
                    print("Ese no se puede. Elegí otro.")
                else:
                    self.celdas[x][y].valor = user_valor
                    self.eliminar_posibles()


    def resolver(self):
        x, y = random.randint(0, 8), random.randint(0, 8)
        z = random.choice(self.celdas[x][y].valores_posibles)

        self.celdas[x][y].valor = z

        for i in range(9):
            for j in range(9):
                if self.celdas[i][j].valor == 0:
                    for item in self.celdas[i][j].valores_posibles:
                        self.celdas[i][j].valor = item
                        self.eliminar_posibles()
                        self.show_valores()
                        self.resolver()
                    self.celdas[i][j].valor = 0



miSudo = Sudoku()
miSudo.resolver()



















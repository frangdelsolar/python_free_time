import pygame

def check_win(board):
	lista_reveladas = []
	for i in range (board.size):
		for j in range(board.size):
			if board.grid[i][j].is_revealed:
				lista_reveladas.append(board.grid[i][j])
				

	if len(lista_reveladas) == ((board.size * board.size)-board.bombs):
		print("Has ganado!!!!")
		board.reveal()
		return True
	return False

def mostrar_vecinos(juego, row, col, clock, screen):
	celda = juego.grid[row][col]
	
	for i in celda.vecindad:
		if i.value == 0 and i.is_revealed == 0 :
			
			i.is_revealed=True
			celda.draw(screen)
			pygame.display.update()
			clock.tick(1000)				
			mostrar_vecinos(juego, i.row, i.col, clock, screen)

		i.is_revealed = True
		i.draw(screen)
		pygame.display.update()
		clock.tick(1000)	


def reveal_cell(juego, row, col, clock, screen):
	celda = juego.grid[row][col]

	if celda.value == 0:
		mostrar_vecinos(juego, row, col, clock, screen)		

	celda.is_revealed = True
	




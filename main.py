import pygame, sys

screen = pygame.display.set_mode((300, 300))
clock = pygame.Clock()

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
        ]

class MAP():
    def __init__(self):
        self.w = 100
        self.h = 100

    def draw_map(self):
        pygame.draw.line(screen, 'white', (0, 100), (300, 100), 5)
        pygame.draw.line(screen, 'white', (0, 200), (300, 200), 5)
        pygame.draw.line(screen, 'white', (100, 0), (100, 300), 5)
        pygame.draw.line(screen, 'white', (200, 0), (200, 300), 5)

    def controlla_vittoria(self, board):
        # 1. Controllo Righe
        for riga in range(3):
            if board[riga][0] == board[riga][1] == board[riga][2] and board[riga][0] != 0:
                return board[riga][0]  # Restituisce 1 o 2 (il giocatore che ha vinto)

        # 2. Controllo Colonne
        for colonna in range(3):
            if board[0][colonna] == board[1][colonna] == board[2][colonna] and board[0][colonna] != 0:
                return board[0][colonna]

        # 3. Controllo Diagonale Principale (\)
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
            return board[0][0]

        # 4. Controllo Diagonale Secondaria (/)
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
            return board[0][2]

        # 5. Controllo Pareggio (se non ci sono più zeri nella matrice)
        # Trasformiamo la matrice in una lista singola per controllare se c'è lo 0
        if 0 not in [cella for riga in board for cella in riga]:
            return "Pareggio"

        # Se nessuno ha vinto e c'è ancora spazio
        return None


map = MAP()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x_ms, y_ms = pygame.mouse.get_pos()
                x_cs = int(x_ms / 100)
                y_cs = int(y_ms / 100)
                num_cs = f"riga: {y_cs} colonna: {x_cs}"
                print(num_cs)
                if board[y_cs][x_cs] == 0:
                    board[y_cs][x_cs] = 1
            elif event.button == 3:
                x_ms, y_ms = pygame.mouse.get_pos()
                x_cs = int(x_ms / 100)
                y_cs = int(y_ms / 100)
                num_cs = f"riga: {y_cs} colonna: {x_cs}"
                print(num_cs)
                if board[y_cs][x_cs] == 0:
                    board[y_cs][x_cs] = 2
            
    screen.fill('black')
    map.draw_map()
    for y in range(3):
        for x in range(3):
            if board[y][x] == 1:
                pygame.draw.circle(screen, 'white', (x * 100 + 50, y * 100 + 50), 30)
            elif board[y][x] == 2:
                pygame.draw.rect(screen, 'white', (x * 100 + 20, y * 100 + 20, 60, 60))
    result = map.controlla_vittoria(board)
    if result:
        print(f"Vincitore: {result}")
    pygame.display.flip()

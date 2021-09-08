from random import randint
import time
a = 50
# creao una matrice con tutti i valori a '.'
matrix = [['.' for i in range(a)] for j in range(a)]


values = ['.', 'O']

# genera randomicamente i valori iniziali della griglia
for i in range(a):
    for j in range(a):
        matrix[i][j] = values[randint(0, 1)]


Halt = False

# ritorna il numero di vicini


def check(i, j):
    vicini = 0
    # controllo il numero di vicini (8 caselle limitrofe alla casella (i,j) della griglia) stando attento al caso in cui controllo la casella stessa (da escludere)
    for k in range(-1, 2):
        for l in range(-1, 2):
            if (i == j == 0):
                continue
            else:
                if matrix[i+k][j+l] == 'O':
                    vicini += 1
    return vicini


while Halt == False:
    Halt = True
    # controllo se il gioco è finito (tutti morti)
    for b in range(a-2):
        for c in range(a-2):
            if matrix[b][c] == 'O':
                Halt = False
    for i in range(a-2):
        for j in range(a-2):
            if i < 2 or j < 2:
                continue
            else:
                if (matrix[i][j] == '.'):
                    # controlla se ha 3 vicini vivi (=1)
                    if (check(i, j) == 3):
                        matrix[i][j] = 'O'
                else:
                    # se è attualmente viva controlla se deve esserlo ancora (esattamente 3 vicini vivi)
                    if(check(i, j) != 3):
                        matrix[i][j] = '.'

    for k in range(a):
        for l in range(a):
            print(matrix[k][l], end=' ')
        print(' ')
    # aspetta 0.5 secondi prima di ricominciare il ciclo e ristampare la nuova matrice aggiornata
    time.sleep(0.5)

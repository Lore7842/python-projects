from random import random, randint

# impiccato, migliorare il dizionario e controllare quando indovino la parola!

parole = open('./hangman/parole.txt', 'r')

dizionario = []
for word in parole:
    dizionario.append(word.replace('\n', ''))


game = True

while(game == True):
    gioco = input('Vuoi giocare? y/n\n')
    if (gioco == 'n'):
        game = False
        continue
    else:
        lettere_immesse = []
        indovinata = 0
        curr = 1
        parola = dizionario[randint(0, len(dizionario)-1)]
        found = []
        for char in parola:
            found.append({
                'lettera': char,
                'founded': False
            })
        attempts = len(parola)
        print('Ho scelto la parola\n')
    while(attempts > 0):
        index = 1
        exists = False
        currentWord = ''
        scelta = int(input('Tentativo numero ' + str(curr) + ': ' +
                           'Vuoi inserire una lettera o la parola? (1,2):'))
        if (scelta == 1):
            lettera = input('Inserisci una lettera:')

        else:
            tentativo = input('Inserisci la parola:')

        if (scelta == 2):
            if (parola == tentativo):
                print('Hai indovinato, la parola era ' + tentativo)
                indovinata = 1
                break
            else:
                print('Parola errata!')
                attempts -= 1
                continue

        if (len(lettera) != 1):
            print('Non hai inserito una lettera! Riprova\n')
            continue
        else:
            lettere_immesse.append(lettera)
        for char in parola:
            if (char == lettera):
                exists = True
                print('La lettera è presente in posizione ' + str(index))
                found[index-1]['founded'] = True
            index += 1

        for char in range(0, len(parola)):
            if (found[char]['founded'] == True):
                currentWord += (parola[char])
            else:
                currentWord += '_'

        print('Parola corrente: ' + currentWord)
        print('Lettere immesse: ')
        print(*lettere_immesse, sep=', ')
        curr += 1
        attempts -= 1
    if indovinata == 0:
        print('Hai finito i tentativi, la parola era ' + parola)

print('Fine gioco!')

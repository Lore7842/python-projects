from random import random, randint

cities = []
names = []
things = []
foods = []

alphabet = []

file = open('C:\\Users\\lollo\\Desktop\\python project\\nam_thing_city\\cities.txt', 'r', encoding='utf8')

citiesFile = open(
    'C:\\Users\\lollo\\Desktop\\python project\\nam_thing_city\\cities.txt', 'r', encoding='utf8')
namesFile = open(
    'C:\\Users\\lollo\\Desktop\\python project\\nam_thing_city\\names.txt', 'r', encoding='utf8')
ThingsFile = open(
    'C:\\Users\\lollo\\Desktop\\python project\\nam_thing_city\\things.txt', 'r', encoding='utf8')
foodsFile = open(
    'C:\\Users\\lollo\\Desktop\\python project\\nam_thing_city\\food.txt', 'r', encoding='utf8')

for line in citiesFile:
    cities.append(line.split(',')[0].lower())

for line in namesFile:
    names.append(line.split(',')[0].lower())

for line in ThingsFile:
    things.append(line.split('\n')[0].lower())

for line in foodsFile:
    foods.append(line.split('\n')[0].lower())

games = 0 #numero di partite svolte in una sessione
score = 0


while(True):
    punteggio = 0
    guessed = []
    scelta = input('Vuoi giocare? (y,n)')
    if scelta == 'n':
        break

    games += 1

    nome = input('Inserisci il nome: ')
    città = input('Inserisci la città: ')
    cibo = input('Inserisci il cibo : ')
    cosa = input('Inserisci la cosa: ')

    if (nome.lower() in names):
        punteggio += 1
        guessed.append((nome))

    if città.lower() in cities:
        punteggio += 1
        guessed.append((città))

    if cibo.lower() in foods:
        punteggio += 1
        guessed.append((cibo))

    if cosa.lower() in things:
        punteggio += 1
        guessed.append((cosa))

    print('Hai totalizzato: {}'.format(punteggio))
    score += punteggio
    print(*guessed, sep=", ")

print('Hai fatto {} partite e hai totalizzato in totale {} punti'.format(games, score))

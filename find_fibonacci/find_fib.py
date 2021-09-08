from random import random

num = input('Inserisci un numero: ')
num_int = int(num)

a = 1
b = 1
c = 1
pos = 0
trovato = False

while(num_int >= c and trovato == False):
    pos += 1
    print('Numero in posizione {} = {}'.format(pos, c))

    if (c == num_int):
        print('Il numero appartiene alla sequenza e si trova in posizione: {}'.format(pos))
        trovato = True
    elif num_int == 1:
        print('Il numero appartiene alla sequenza e si trova in posizione: {}'.format(pos))
        trovato = True

    a = b
    b = c
    c = a+b

if(trovato == False):
    print('Il numero {} non appartiene alla sequenza di fibonacci'.format(num))

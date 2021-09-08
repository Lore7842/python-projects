from random import random,randint

i = int(input('Quante parole? '))

parole=[]
parole_usate= []

for k in range(0,i):
    s = input('Inserisci parola: ')
    parole.append(s)

k = 0
while (k < i):
    n = randint(0, i-1)
    if (n in parole_usate):
        continue
    else:
        parole_usate.append(n)
        k = k+1
    print(str(k) + ' ' +parole[n] + ' ')


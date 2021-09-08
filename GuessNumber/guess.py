from random import random, randint

i = randint(0, 100)

print('Ho scelto un numero tra 0 e 100\n')

hints = []

for k in range(2, 51):
    if i % k == 0:
        hints.append('Il numero è divisibile per ' + str(k))
    else:
        hints.append('Il numero non è divisibile per ' + str(k))

n = 101
attempt = 0

while n != i:
    attempt += 1
    print(hints[attempt-1])
    n = int(input('Indovina il numero: '))
    

print('Hai indovinato il numero in ' + str(attempt) + ' tentativi!' +'\n\n\n')

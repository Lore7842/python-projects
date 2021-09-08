def binarySearch(vector, value):
    posizione = -1
    vector.sort()
    fine = 0
    i = 0
    f = len(vector) -1
    while(fine == 0):
        if (value > vector[int((i+f) /2) ]):
            i = (i+f) / 2
        elif value < vector[int((i+f) /2) ]:
            f = (i+f) / 2
        elif value == vector[int((i+f) /2) ]:
            fine = 1
            posizione = int((i+f)/2)
    return posizione+1

vettore = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

numero = int(input('Inserisci il numero da cercare: '))

posizione = binarySearch(vettore,numero)

if posizione > 0:
    print('Elemento in posizione: {}'.format(posizione))
else: 
    print('Elemento non trovato!')
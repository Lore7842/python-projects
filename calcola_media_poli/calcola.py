class Voto:
    def __init__(self, crediti, voto):
        self.crediti = crediti
        self.voto = voto

media = float(input('Inserisci la media corrente: '))
crediti = int(input('Numero crediti attuali: '))
voti = []


n = int(input('Inserisci il numero dei voti che vuoi aggiungere: '))

for i in range(0,n):
    voto = int(input('Inserisci voto: '))
    crediti_local = int(input('Inserisci crediti: '))
    v = Voto(crediti,voto)
    crediti = crediti + crediti_local
    media = (media*(crediti - crediti_local) + voto * crediti_local)/crediti
    voti.append(v)

# for i in range(0,len(voti)):
#     print(voti[i].voto)
#     print(voti[i].crediti)

print('La nuova media è {}'.format(media))


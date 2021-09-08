from faker import Faker

fake = Faker()
contatti = {}

Aggiungi = True
people = int(input('Quante persone: '))

for i in range(0,people):
    name = fake.name()
    
    o = {
        'name' : name.split(' ')[0],
        'cognome' : name.split(' ')[1],
        'tel' : fake.phone_number().split('x')[0]
    }
    contatti[name] = o

while Aggiungi:
    nome = input('Inserisci il nome: ')
    if nome == 'fine':
        break
    cognome = input('Inserisci il cognome: ')
    tel = int(input('Inserisci il telefono: '))

    o = {
        'nome': nome,
        'cognome': cognome,
        'tel': tel
    }
    contatti[nome] = o

    print('Hai aggiunto {}'.format(contatti[nome]))

print('Lista contatti:')
print(contatti)

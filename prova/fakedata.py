import requests
from faker import Faker

fake = Faker()


message = [
    {
    'name': fake.name(),
    'address': fake.address(),
    'phone': fake.phone_number(),
    'ssn' : fake.ssn()
    }
]
print()

for i in range(0,10):
    message.append({
        'name': fake.name(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'ssn' : fake.ssn(),
    })

for k in range(0,11):
    print('*' + str(k) + '\nNome: ' + message[k]['name'] + '\n' + 'Indirizzo: ' +
          message[k]['address'] + '\n' + 'Telefono: ' + message[k]['phone'] + '\nCodice fiscale: ' + message[k]['ssn'] + '\n')

from random import randint, random
import requests
import json

response = requests.get('http://www.google.com')
print(response.status_code)

joke = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
new = joke.json()
obj = json.dumps(new)
obj1 = json.loads(obj)
print (obj1['insult'])








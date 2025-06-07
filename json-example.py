import json

x = '{"brand": "BMW", "modal":"320", "year": 1998}'

carJson = json.loads(x)

print(carJson["brand"])
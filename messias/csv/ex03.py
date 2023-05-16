import json

list = {
    'fruits': {'avocado': 6.99,
                'grape': 7.99,
                'kiwi': 13.99},
    'data': '17/05/2023'
}

with open('file.json', 'w') as file:
    json.dump(list, file)

my_json = json.dumps(list)

print(my_json)
import json

people_string = '''
    {
        "people":[
          {
            "name": "Sainath Reddy",
            "age": 20,
            "email": null,
            "status": true 
          },
          {
            "name": "Gangi Reddy",
            "age": 50,
            "email": "rg@gmail.com",
            "status": true 
          }
        ]
    }
'''

data = json.loads(people_string)
print(type(data))
print(data)
old_data = json.dumps(data)
for person in data['people']:
    print( "{}  {}".format(person['name'], person))
    del person['age']

new_data = json.dumps(data, indent=3)
print(old_data)
print(new_data)
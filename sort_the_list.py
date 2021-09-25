persons = [
{
"name": "John",
"age": 36,
"country": "Norway"
},
{"name": "Bob",
"age": 36,
"country": "Norway"
},
{"name": "amul",
"age": 35,
"country": "ban"
}

]

new_persons = sorted(persons, key = lambda i: (i['age'], i['name'], i['country']))
print(new_persons)
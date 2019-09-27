import csv

users = [
    {'name': 'Masha', 'age': 21, 'job': 'Scientist'},
    {'name': 'John', 'age': 31, 'job': 'Programmer'},
    {'name': 'Boss', 'age': 25, 'job': 'Big boss'}
]

with open('users.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in users:
        writer.writerow(user)
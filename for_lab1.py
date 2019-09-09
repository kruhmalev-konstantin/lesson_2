from if_lab_2 import discounted

example_string = 'Я изучаю язык Python'

for number in range(3):
    print(f'Hello World {number}!')

for letter in 'python':
    print(letter.upper())

for word in example_string.split():
    print(f'Длинна слова "{word}": {len(word)}')

student_scores = [1, 21, 19, 6, 5]

print(f"Средняя оценка: {sum(student_scores)/len(student_scores)}")

scores_sum = 0
for score in student_scores:
    scores_sum += score
    print(scores_sum)

print(f"Средняя оценка: {scores_sum/len(student_scores)}")


stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
    {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

for phone in stock:
    print(phone)
    phone["final_price"] = discounted(phone["price"], phone["discount"], name=phone["name"])
    print(phone)
    print("---")

print(stock)
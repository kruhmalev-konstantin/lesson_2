age = input('Введите возраст: ')

def what_age(age):
    age = int(age)
    if age <= 7:
        return 'Дет.сад'
    elif age > 7 and age <= 21:
        return 'Школа'
    elif age > 21 and age <=25:
        return 'Университет'
    elif age > 26 and age < 65:
        return 'Работа'
    else:
        return 'Пенсия'

print(what_age(age))
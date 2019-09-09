"""
str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')

def check_str(str1,str2):
    if type(str1) != str and type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif len(str1) != len(str2) and str2 == 'learn':
        return 3
    else:
        return(str1,str2)

print(check_str(str1,str2))
"""

def discounted(price, discount, max_discount=20, name=""):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)
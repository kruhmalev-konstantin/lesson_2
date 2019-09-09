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
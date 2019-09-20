"""
Домашнее задание №1
Цикл while: ask_user
* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
answers = {
    "Как дела" : "Хорошо",
    "Чем занимаешься" : "Программирую"
}

def ask_user():
    user_say = ''
    while user_say not in answers:
        try:
            user_say = input('Задай вопрос? ')
            if user_say in answers:
                print(answers.get(user_say))
                break
            elif user_say == 'Пока':
                print('Ну пока')
                break
            else:
                print('Сам ты {}'.format(user_say))
        except KeyboardInterrupt:
            print('Ну и ладно. Пока!')
            break

ask_user()
school_list = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [5,4,3,2,3]},
    {'school_class': '4c', 'scores': [5,5,4,4,4]}
]

middle_score_all = 0

for number in range(len(school_list)):
    class_score = sum(school_list[number].get('scores'))/len(school_list[number].get('scores'))
    class_num = school_list[number].get('school_class')
    middle_score_all += class_score
    print(f'Средний балл в {class_num} классе: {class_score}')
else:
    result = middle_score_all / len(school_list)
    print(f'Средний балл по всем школам: {middle_score_all}')
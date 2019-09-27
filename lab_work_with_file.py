with open('referat.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    line_num = 0
    for line in f:
        line_num += 1
        line_lenght = len(line)
        word = len(line.split())
        print(f"Длинна строки: {line_num} - {line_lenght} Колличество слов в строке: {word}")

with open('referat2.txt', 'w', encoding='utf-8') as file:
    file.write(text.replace('.', '!'))
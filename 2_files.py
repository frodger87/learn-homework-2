"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

PREPOSITIONS = [
    'в', 'без', 'до', 'для', 'за', 'через', 'над', 'по', 'из',
    'у', 'около', 'под', 'о', 'про', 'на', 'к', 'перед', 'при',
    'с', 'между', 'и', 'или', 'а'
]


def open_file(file_path: str):
    with open(file_path, 'r', encoding='UTF8') as file:
        return file.read()


def remove_prepositions(file):
    splited_file = file.split()
    words = []
    prepositions = PREPOSITIONS
    for word in splited_file:
        if word.lower() not in prepositions:
            words.append(word)
    return words


def edit_file(file):
    return file.replace('.', '!')


def save_file(file_text, save_path: str):
    with open(save_path, 'w', encoding='UTF-8') as f:
        f.write(file_text)


def main():
    file_path = '/home/dkostarev/Загрузки/referat.txt'
    save_path = '/home/dkostarev/Загрузки/referat2.txt'
    file = open_file(file_path)
    print(f"Длинна файла: {len(file)}")
    file_words = remove_prepositions(file)
    print(f"Количество слов в файле: {len(file_words)}")
    edited_file = edit_file(file)
    save_file(edited_file, save_path)


if __name__ == "__main__":
    main()

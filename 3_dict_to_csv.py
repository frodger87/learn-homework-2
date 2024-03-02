"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

user_list = [
    {'name': 'Сергей', 'age': '20', 'job': 'Повар'},
    {'name': 'Анна', 'age': '25', 'job': 'Разработчик'},
    {'name': 'Антон', 'age': '30', 'job': 'Столяр'},
    {'name': 'Виктория', 'age': '27', 'job': 'Аналитик'},
]


def main():
    with open('users.csv', 'w', encoding='UTF-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)


if __name__ == "__main__":
    main()

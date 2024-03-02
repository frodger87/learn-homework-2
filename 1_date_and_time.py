"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta


def print_days():
    print(f"Yesterday: {(date.today() - timedelta(days=1)).strftime('%Y-%m-%d')}")
    print(f"Today: {date.today().strftime('%Y-%m-%d')}")
    print(f"30 days before: {(date.today() - timedelta(days=30)).strftime('%Y-%m-%d')}")


def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

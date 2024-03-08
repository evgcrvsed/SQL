import sqlite3 as sq
import os
import time

from colorama import init, Fore
init()


def clear():
    """Очистка консоли"""
    os.system('cls')

# Создать таблицу "События" с полями: Название, Дата, Описание.


class DB:
    def __init__(self, patch: str):
        self._patch = patch

    def create_table(self):
        self.get_cursor.execute("""CREATE TABLE IF NOT EXISTS Events (
                                   name TEXT NOT NULL,
                                   description TEXT,
                                   datee DATETIME NOT NULL
                                   )""")
        return 1

    def drop_table(self):
        self.get_cursor.execute("DROP TABLE IF EXISTS Events")
        self.create_table()

    def add_event(self, event_name, event_description, event_datee):
        self.get_cursor.execute('INSERT INTO Events (name, description, datee) VALUES (?, ?, ?)', (event_name, event_description, event_datee)).connection.commit()

    @property
    def get_cursor(self):
        with sq.connect(self._patch) as con:
            return con.cursor()


db = DB('events.db')
db.create_table()

while True:
    clear()
    print(f'Инструкция при работе с базой данных:')
    print(f'    {Fore.GREEN}/add{Fore.RESET} - Добавить ивент,')
    print(f'    {Fore.RED}/drop{Fore.RESET} - Пересоздать таблицу,')

    choice = input(f'\nВведите команду: ')
    match choice:
        case '/add':
            while True:
                event_name = input(f'Введите {Fore.GREEN}название{Fore.RESET} события: ')
                if len(event_name) > 0: break

            event_description = input(f'Введите {Fore.GREEN}описание{Fore.RESET} события: ')

            event_date = input(f'Введите дату события в формате YYYY-MM-DD HH:MM:SS: ')

            db.add_event(event_name, event_description, event_date)
            print(f'Ивент {Fore.GREEN}{event_name}{Fore.RESET} успешно добавлен!')
            time.sleep(1)
        case '/drop':
            db.drop_table()
            print(f'{Fore.YELLOW}Таблица успешно пересоздана!{Fore.RESET}')
            time.sleep(1)

# db.drop_table()

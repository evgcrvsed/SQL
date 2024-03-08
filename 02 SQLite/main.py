import sqlite3 as sq
import os
import time

from colorama import init, Fore
init()


def clear():
    """Очистка консоли"""
    os.system('cls')

# Создать таблицу "События" с полями: Название, Дата, Описание.


class DataBase:
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


db = DataBase('events.db')
db.create_table()
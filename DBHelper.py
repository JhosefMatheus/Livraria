import sqlite3
from sqlite3.dbapi2 import OperationalError


class DBHelper:
    def __init__(self):
        self.connection = sqlite3.connect('Livros.db')
        self.cursor = self.connection.cursor()

        try:
            self.cursor.execute('''
            CREATE TABLE books (
                id_book INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title_book TEXT NOT NULL,
                author_book TEXT NOT NULL,
                publishing_company_book TEXT NOT NULL,
                pages_book INTEGER NOT NULL,
                owner_book TEXT NOT NULL
            );
            ''')
        except OperationalError:
            None

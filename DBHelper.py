import sqlite3
from sqlite3.dbapi2 import OperationalError


class DBHelper:
    def __init__(self):
        self.connection = sqlite3.connect('Livros.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id_book INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title_book TEXT NOT NULL,
            author_book TEXT NOT NULL,
            publishing_company_book TEXT NOT NULL,
            pages_book INTEGER NOT NULL,
            owner_book TEXT NOT NULL
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id_author INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            author_name TEXT NOT NULL
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS publishing_companys (
            publishing_company_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            publishing_company_name TEXT NOT NULL
        );
        ''')

        self.connection.commit()
        self.connection.close()

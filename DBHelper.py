import sqlite3


class DBHelper:
    def __init__(self):

        self.__connection = sqlite3.connect('Livros.db')
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id_book INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title_book TEXT NOT NULL,
            author_book TEXT NOT NULL,
            publishing_company_book TEXT NOT NULL,
            pages_book INTEGER NOT NULL,
            owner_book TEXT NOT NULL
        );
        ''')

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id_author INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            author_name TEXT NOT NULL
        );
        ''')

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS publishing_companys (
            publishing_company_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            publishing_company_name TEXT NOT NULL
        );
        ''')

        self.__connection.commit()

    def add_valores(self, title_book, author_book, publishing_company, pages_book, owner_book):

        self.__cursor.execute('''
        INSERT INTO books (title_book, author_book, publishing_company_book, pages_book, owner_book)
        VALUES (?, ?, ?, ?, ?)
        ''',  (title_book, author_book, publishing_company, pages_book, owner_book))

        autores = self.__cursor.execute('''
        SELECT author_name FROM authors;
        ''').fetchall()

        editoras = self.__cursor.execute('''
        SELECT publishing_company_name FROM publishing_companys;
        ''').fetchall()

        if (author_book,) not in autores:
            self.__cursor.execute('''
            INSERT INTO authors (author_name) VALUES (?)
            ''', (author_book,))

        if (publishing_company,) not in editoras:
            self.__cursor.execute('''
            INSERT INTO publishing_companys (publishing_company_name) VALUES (?)
            ''', (publishing_company,))

        self.__connection.commit()

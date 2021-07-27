import sqlite3
from tkinter.constants import END


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

    def selecionar_dado(self, title_book_entry, author_book_entry, publishing_company_entry, n_pages_entry, owner_book_entry, my_tree):
        title_book_entry.delete(0, END)
        author_book_entry.delete(0, END)
        publishing_company_entry.delete(0, END)
        n_pages_entry.delete(0, END)
        owner_book_entry.delete(0, END)

        selecionado = my_tree.focus()

        values = my_tree.item(selecionado, 'values')

        title_book_entry.insert(0, values[1])
        author_book_entry.insert(0, values[2])
        publishing_company_entry.insert(0, values[3])
        n_pages_entry.insert(0, values[4])
        owner_book_entry.insert(0, values[5])

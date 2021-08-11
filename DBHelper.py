import sqlite3
from tkinter.constants import END


class DBHelper:
    def __init__(self):

        self.__connection = sqlite3.connect('Livros.db')
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id_livro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            titulo_livro TEXT NOT NULL,
            autor_livro TEXT NOT NULL,
            editora_livro TEXT NOT NULL,
            paginas_livro INTEGER NOT NULL,
            proprietario_livro TEXT NOT NULL
        );
        ''')

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id_autor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_autor TEXT NOT NULL
        );
        ''')

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS editoras (
            id_editora INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_editora TEXT NOT NULL
        );
        ''')

        self.__connection.commit()

    def get_livros(self):
        return self.__cursor.execute('SELECT * FROM livros ORDER BY id_livro').fetchall()

    def get_autores(self):
        return self.__cursor.execute('SELECT * FROM autores ORDER BY id_autor').fetchall()

    def get_editoras(self):
        return self.__cursor.execute('SELECT * FROM editoras ORDER BY id_editora').fetchall()

    def add_livro(self, titulo_livro, autor_livro, editora, paginas_livro, proprietario_livro):

        self.__cursor.execute('''
        INSERT INTO livros (titulo_livro, autor_livro, editora_livro, paginas_livro, proprietario_livro)
        VALUES (?, ?, ?, ?, ?)
        ''',  (titulo_livro, autor_livro, editora, paginas_livro, proprietario_livro))

        autores = self.__cursor.execute('''
        SELECT nome_autor FROM autores;
        ''').fetchall()

        editoras = self.__cursor.execute('''
        SELECT nome_editora FROM editoras;
        ''').fetchall()

        if (autor_livro,) not in autores:
            self.__cursor.execute('''
            INSERT INTO autores (nome_autor) VALUES (?)
            ''', (autor_livro,))

        if (editora,) not in editoras:
            self.__cursor.execute('''
            INSERT INTO editoras (nome_editora) VALUES (?)
            ''', (editora,))

        self.__connection.commit()

    def add_autor(self, nome_autor):
        self.__cursor.execute(
            'INSERT INTO autores (nome_autor) VALUES (?)', (nome_autor,))

        self.__connection.commit()

    def add_editora(self, nome_editora):
        self.__cursor.execute(
            'INSERT INTO editoras (nome_editora) VALUES (?)', (nome_editora,))

        self.__connection.commit()

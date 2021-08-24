import mysql.connector


class DBHelper:
    def __init__(self):
        self.data_base = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='livraria_db'
        )

        self.cursor = self.data_base.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INT (255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR (255) NOT NULL,
            autor VARCHAR (255) NOT NULL,
            editora VARCHAR (255) NOT NULL,
            paginas INT (255) NOT NULL,
            proprietario VARCHAR (255) NOT NULL 
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INT (255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            autor VARCHAR (255) NOT NULL
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS editoras (
            id INT (255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            editora VARCHAR (255) NOT NULL
        );
        ''')

    def get_livros(self):
        self.cursor.execute('SELECT * FROM livros ORDER BY id')
        return self.cursor.fetchall()

    def get_autores(self):
        self.cursor.execute('SELECT * FROM autores ORDER BY id')
        return self.cursor.fetchall()

    def get_editoras(self):
        self.cursor.execute('SELECT * FROM editoras ORDER BY id')
        return self.cursor.fetchall()

    def add_livro(self, titulo, autor, editora, n_paginas, proprietario):
        sql = 'INSERT INTO livros (titulo, autor, editora, paginas, proprietario) VALUES (%s, %s, %s, %s, %s)'
        values = (titulo, autor, editora, n_paginas, proprietario)

        self.cursor.execute(sql, values)

        self.cursor.execute('SELECT autor FROM autores')
        autores = self.cursor.fetchall()

        self.cursor.execute('SELECT editora FROM editoras')
        editoras = self.cursor.fetchall()

        if (autor,) not in autores:
            self.add_autor(autor)

        if (editora,) not in editoras:
            self.add_editora(editora)

        self.data_base.commit()

    def add_autor(self, autor):
        sql = 'INSERT INTO autores (autor) VALUES (%s)'
        values = (autor,)

        self.cursor.execute(sql, values)

        self.data_base.commit()

    def add_editora(self, editora):
        sql = 'INSERT INTO editoras (editora) VALUES (%s)'
        values = (editora,)

        self.cursor.execute(sql, values)

        self.data_base.commit()

    def editar_livro(self, titulo, autor, editora, paginas, proprietario, id, autor_livro_selecionado, editora_livro_selecionado):
        sql = 'UPDATE livros SET titulo = %s, autor = %s, editora = %s, paginas = %s, proprietario = %s WHERE id = %s'
        values = (titulo, autor, editora, paginas, proprietario, id)

        self.cursor.execute(sql, values)

        self.cursor.execute('SELECT autor FROM livros')
        autores = self.cursor.fetchall()

        self.cursor.execute('SELECT editora FROM livros')
        editoras = self.cursor.fetchall()

        if (autor_livro_selecionado,) not in autores:
            sql = 'DELETE FROM autores WHERE autor = %s'
            values = (autor_livro_selecionado,)

            self.cursor.execute(sql, values)

        if (editora_livro_selecionado,) not in editoras:
            sql = 'DELETE FROM editoras WHERE editora = %s'
            values = (editora_livro_selecionado,)

            self.cursor.execute(sql, values)

        self.cursor.execute('SELECT autor FROM autores')
        autores = self.cursor.fetchall()

        self.cursor.execute('SELECT editora FROM editoras')
        editoras = self.cursor.fetchall()

        if (autor,) not in autores:
            self.add_autor(autor)

        if (editora,) not in editoras:
            self.add_editora(editora)

        self.data_base.commit()

    def excluir_livro(self, id_livro, autor_livro, editora_livro):
        sql = 'DELETE FROM livros WHERE id = %s'
        values = (id_livro,)

        self.cursor.execute(sql, values)

        self.cursor.execute('SELECT autor FROM livros')
        autores = self.cursor.fetchall()

        self.cursor.execute('SELECT editora FROM livros')
        editoras = self.cursor.fetchall()

        if (autor_livro,) not in autores:
            sql = 'DELETE FROM autores WHERE autor = %s'
            values = (autor_livro,)

            self.cursor.execute(sql, values)

        if (editora_livro,) not in editoras:
            sql = 'DELETE FROM editoras WHERE editora = %s'
            values = (editora_livro,)

            self.cursor.execute(sql, values)

        self.data_base.commit()

    def editar_autor(self, id_autor_selecionado, nome_autor_selecionado, novo_autor):
        sql = 'UPDATE autores SET autor = %s WHERE id = %s'
        values = (novo_autor, id_autor_selecionado)

        self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET autor = %s WHERE autor = %s'
        values = (novo_autor, nome_autor_selecionado)

        self.cursor.execute(sql, values)

        self.data_base.commit()

    def excluir_autor(self, id_autor, nome_autor):
        sql = 'DELETE FROM autores WHERE id = %s'
        values = (id_autor,)

        self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET autor = %s WHERE autor = %s'
        values = ('Desconhecido(a)', nome_autor)

        self.cursor.execute(sql, values)

        self.data_base.commit()

    def editar_editora(self, id_editora_selecionada, nome_editora_selecionada, nova_editora):
        sql = 'UPDATE editoras SET editora = %s WHERE id = %s'
        values = (nova_editora, id_editora_selecionada)

        self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET editora = %s WHERE editora = %s'
        values = (nova_editora, nome_editora_selecionada)

        self.cursor.execute(sql, values)

        self.data_base.commit()

    def excluir_editora(self, id_editora, nome_editora):
        sql = 'DELETE FROM editoras WHERE id = %s'
        values = (id_editora,)

        self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET editora = %s WHERE editora = %s'
        values = ('Desconhecida', nome_editora)

        self.cursor.execute(sql, values)

        self.data_base.commit()

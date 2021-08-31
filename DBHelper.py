import mysql.connector
import numpy as np


class DBHelper:
    def __init__(self):
        '''
        O construtor é responsável por fazer a conexão com o banco de dados e criar as tabelas
        livros, autores e editoras.
        '''
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='livraria_menan'
        )

        self.cursor = self.connection.cursor()

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
        '''
        Retorna todos os registros presentes na tabela livros.
        '''
        self.cursor.execute('SELECT * FROM livros ORDER BY id')
        return self.cursor.fetchall()

    def get_autores(self):
        '''
        Retorna todos os registros presentes na tabela autores.
        '''
        self.cursor.execute('SELECT * FROM autores ORDER BY id')
        return self.cursor.fetchall()

    def get_editoras(self):
        '''
        Retorna todos os registros presentes na tabela editoras.
        '''
        self.cursor.execute('SELECT * FROM editoras ORDER BY id')
        return self.cursor.fetchall()

    def add_livro(self, titulo, autor, editora, n_paginas, proprietario):
        '''
        Adiciona um novo registro na tabela livro, e seu respectivo autor e editora nas respectivas
        tabelas. Caso o autor do livro em questão já esteja registrado na tabela autores, ele não
        adicionado. O mesmo vale para a editora.
        '''
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

        self.connection.commit()

    def add_autor(self, autor):
        '''
        Adiciona um novo registro autor na tabela autores.
        '''
        sql = 'INSERT INTO autores (autor) VALUES (%s)'
        values = (autor,)

        self.cursor.execute(sql, values)

        self.connection.commit()

    def add_editora(self, editora):
        '''
        Adiciona um novo registro editora na tabela editoras.
        '''
        sql = 'INSERT INTO editoras (editora) VALUES (%s)'
        values = (editora,)

        self.cursor.execute(sql, values)

        self.connection.commit()

    def editar_livro(self, titulo, autor, editora, paginas, proprietario, id, autor_livro_selecionado, editora_livro_selecionado):
        '''
        Atualiza todos os campos de um registro livro. Caso o novo autor não esteja na tabela autores, ele será adicionado.
        Caso o antigo autor não esteja mais presente em nenhum livro o mesmo será excluído da tabela autores. O mesmo vale para
        as editoras.
        '''
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

        self.connection.commit()

    def excluir_livro(self, id_livro, autor_livro, editora_livro):
        '''
        Deleta um registro do tipo livro da tabela livros. Se o autor do livro em questão for o último ele
        também será excluído da tabela de autores. O mesmo vale para as editoras.
        '''
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

        self.connection.commit()

    def editar_autor(self, id_autor_selecionado, nome_autor_selecionado, novo_autor):
        '''
        Edita o nome do autor selecionado. Qualquer livro que tenha como autor o mesmo nome do
        autor selecionado também sofrerá alteração. Caso o nome do autor já exista ele será 
        excluído para evitar valores duplicados.
        '''

        self.cursor.execute('SELECT autor FROM autores')
        autores = self.cursor.fetchall()

        print(autores)
        print((novo_autor,) not in autores)

        if (novo_autor,) not in autores:
            sql = 'UPDATE autores SET autor = %s WHERE id = %s'
            values = (novo_autor, id_autor_selecionado)

            self.cursor.execute(sql, values)

        else:
            sql = 'DELETE FROM autores WHERE autor = %s'
            values = (nome_autor_selecionado,)

            self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET autor = %s WHERE autor = %s'
        values = (novo_autor, nome_autor_selecionado)

        self.cursor.execute(sql, values)

        self.connection.commit()

    def excluir_autor(self, id_autor, nome_autor):
        '''
        Exclui o autor selecionado. Caso o autor em questão exista em qualquer registro da tabela
        livros, o campo autor desses registros será trocado por "Desconhecido(a)".
        '''
        sql = 'DELETE FROM autores WHERE id = %s'
        values = (id_autor,)

        self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET autor = %s WHERE autor = %s'
        values = ('Desconhecido(a)', nome_autor)

        self.cursor.execute(sql, values)

        self.connection.commit()

    def editar_editora(self, id_editora_selecionada, nome_editora_selecionada, nova_editora):
        '''
        Edita o nome da editora selecionada. Qualquer livro que tenha como editora o mesmo nome da
        editora selecionada também sofrerá alteração. Caso o nome da editora já exista ele será 
        excluído para evitar valores duplicados.
        '''
        self.cursor.execute('SELECT editora FROM editoras')
        editoras = self.cursor.fetchall()

        if (nova_editora,) not in editoras:
            sql = 'UPDATE editoras SET editora = %s WHERE id = %s'
            values = (nova_editora, id_editora_selecionada)

            self.cursor.execute(sql, values)

        else:
            sql = 'DELETE FROM editoras WHERE editora = %s'
            values = (nome_editora_selecionada,)

            self.cursor.execute(sql, values)

        sql = 'UPDATE editoras SET editora = %s WHERE id = %s'
        values = (nova_editora, id_editora_selecionada)

        self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET editora = %s WHERE editora = %s'
        values = (nova_editora, nome_editora_selecionada)

        self.cursor.execute(sql, values)

        self.connection.commit()

    def excluir_editora(self, id_editora, nome_editora):
        '''
        Exclui a editora selecionada. Caso a editora em questão exista em qualquer registro da tabela
        livros, o campo editora desses registros será trocado por "Desconhecida".
        '''
        sql = 'DELETE FROM editoras WHERE id = %s'
        values = (id_editora,)

        self.cursor.execute(sql, values)

        sql = 'UPDATE livros SET editora = %s WHERE editora = %s'
        values = ('Desconhecida', nome_editora)

        self.cursor.execute(sql, values)

        self.connection.commit()

    def nome_autores(self):
        '''
        Esta função retorna uma lista dos nomes de todos os autores presentes na base de dados.
        '''
        self.cursor.execute('SELECT autor FROM autores')
        return list(np.array(self.cursor.fetchall()).flatten())

    def nome_editoras(self):
        '''
        Esta função retorna uma lista dos nomes de todas as editoras presentes na base de dados.
        '''
        self.cursor.execute('SELECT editora FROM editoras')
        return list(np.array(self.cursor.fetchall()).flatten())

    def titulo_livros(self):
        '''
        Esta função retorna uma lista de valores únicos de todos os títulos de livros presentes
        na base de dados.
        '''
        self.cursor.execute('SELECT titulo FROM livros')
        return list(set(np.array(self.cursor.fetchall()).flatten()))

    def pesquisar_livro(self, opcao, entrada):
        '''
        Esta função retorna o resultado da pesquisa feita de acordo com a coluna desejada (titulo, 
        autor, editora).
        '''
        if opcao == 'Livro':
            sql = 'SELECT * FROM livros WHERE titulo = %s'
            values = (entrada,)

            self.cursor.execute(sql, values)

            return self.cursor.fetchall()

        elif opcao == 'Autor':
            sql = 'SELECT * FROM livros WHERE autor = %s'
            values = (entrada,)

            self.cursor.execute(sql, values)

            return self.cursor.fetchall()

        elif opcao == 'Editora':
            sql = 'SELECT * FROM livros WHERE editora = %s'
            values = (entrada,)

            self.cursor.execute(sql, values)

            return self.cursor.fetchall()

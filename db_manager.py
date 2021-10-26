import sqlite3
import pandas as pd
from datetime import date


class db_manager:
    def __init__(self):
        self.db_name = 'livraria_hjm.db'

        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                editora TEXT NOT NULL,
                n_paginas INTEGER NOT NULL,
                situacao TEXT NOT NULL,
                beneficiado TEXT,
                telefone TEXT,
                dt_emprestimo TEXT,
                dt_devolucao TEXT
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                autor TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS editoras (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                editora TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cds (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                titulo TEXT NOT NULL,
                artista TEXT NOT NULL,
                distribuidora TEXT NOT NULL,
                duracao TEXT NOT NULL,
                situacao TEXT NOT NULL,
                beneficiado TEXT,
                telefone TEXT,
                dt_emprestimo TEXT,
                dt_devolucao TEXT
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS artistas_cds (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                artista TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS distribuidoras_cds (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                distribuidora TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dvds (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                titulo TEXT NOT NULL,
                diretor TEXT NOT NULL,
                distribuidora TEXT NOT NULL,
                duracao TEXT NOT NULL,
                situacao TEXT NOT NULL,
                beneficiado TEXT,
                telefone TEXT,
                dt_emprestimo TEXT,
                dt_devolucao TEXT
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS diretores (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                diretor TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS distribuidoras_dvds (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                distribuidora TEXT NOT NULL
            );
        ''')

        cursor.close()

        connection.commit()
        connection.close()

    def get_livros(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM livros'

        livros = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return livros

    def get_cds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM cds'

        cds = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return cds

    def get_dvds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM dvds'

        dvds = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return dvds

    def get_artistas(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM artistas_cds'

        artistas = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return artistas

    def get_autores(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM autores'

        autores = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return autores

    def get_editoras(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM editoras'

        editoras = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return editoras

    def get_diretores(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM diretores'

        diretores = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return diretores

    def get_distribuidoras_cds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM distribuidoras_cds'

        distribuidoras = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return distribuidoras

    def get_distribuidoras_dvds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT * FROM distribuidoras_dvds'

        distribuidoras = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        return distribuidoras

    def add_livro(self, titulo, autor, editora, n_pag, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        sql = '''
        INSERT INTO livros (titulo, autor, editora, n_paginas, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        values = (titulo, autor, editora, n_pag, situacao,
                  beneficiado, telefone, dt_emprestimo, dt_devolucao)

        cursor.execute(sql, values)

        cursor.close()

        connection.commit()

        connection.close()

        self.add_autor(autor)
        self.add_editora(editora)

    def add_autor(self, autor):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT autor FROM autores'

        autores = cursor.execute(query).fetchall()

        if (autor,) not in autores:
            sql = '''
            INSERT INTO autores (autor)
            VALUES (?)
            '''

            values = (autor,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def add_editora(self, editora):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT editora FROM editoras'

        editoras = cursor.execute(query).fetchall()

        if (editora,) not in editoras:
            sql = '''
            INSERT INTO editoras (editora)
            VALUES (?)
            '''

            values = (editora,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def add_dvd(self, titulo, diretor, distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        sql = '''
            INSERT INTO dvds (titulo, diretor, distribuidora, duracao, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        values = (titulo, diretor, distribuidora, tempo, situacao,
                  beneficiado, telefone, dt_emprestimo, dt_devolucao)

        cursor.execute(sql, values)

        cursor.close()

        connection.commit()

        connection.close()

        self.add_diretor_dvd(diretor)
        self.add_distribuidora_dvd(distribuidora)

    def add_diretor_dvd(self, diretor):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT diretor FROM diretores'

        diretores = cursor.execute(query).fetchall()

        if (diretor,) not in diretores:
            sql = '''
                INSERT INTO diretores (diretor)
                VALUES (?)
            '''

            values = (diretor,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def add_distribuidora_dvd(self, distribuidora):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT distribuidora FROM distribuidoras_dvds'

        distribuidoras = cursor.execute(query).fetchall()

        if (distribuidora,) not in distribuidoras:
            sql = '''
                INSERT INTO distribuidoras_dvds (distribuidora)
                VALUES (?)
            '''

            values = (distribuidora,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def add_cd(self, titulo, artista_autor, distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        sql = '''
            INSERT INTO cds (titulo, artista, distribuidora, duracao, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        values = (titulo, artista_autor, distribuidora, tempo, situacao,
                  beneficiado, telefone, dt_emprestimo, dt_devolucao)

        cursor.execute(sql, values)

        cursor.close()

        connection.commit()

        connection.close()

        self.add_autor_artista_cd(artista_autor)
        self.add_distribuidora_cd(distribuidora)

    def add_autor_artista_cd(self, autor_artista):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT artista FROM  artistas_cds'

        artistas = cursor.execute(query).fetchall()

        if (autor_artista,) not in artistas:
            sql = '''
                INSERT INTO artistas_cds (artista)
                VALUES (?)
            '''

            values = (autor_artista,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def add_distribuidora_cd(self, distribuidora):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT distribuidora FROM distribuidoras_cds'

        distribuidoras = cursor.execute(query).fetchall()

        if (distribuidora,) not in distribuidoras:
            sql = '''
                INSERT INTO distribuidoras_cds (distribuidora)
                VALUES (?)
            '''

            values = (distribuidora,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def nome_autores(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT autor FROM autores'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        autores = [autor[0] for autor in query_result]

        return autores

    def nome_editoras(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT editora FROM editoras'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        editoras = [editora[0] for editora in query_result]

        return editoras

    def titulo_livros(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT DISTINCT titulo FROM livros'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def nome_diretores_dvds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT diretor FROM diretores'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        diretores = [diretor[0] for diretor in query_result]

        return diretores

    def nome_autores_artistas_cds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT artista FROM artistas_cds'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        artistas = [artista[0] for artista in query_result]

        return artistas

    def nome_distribuidoras_dvds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT distribuidora FROM distribuidoras_dvds'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        distribuidoras = [distribuidora[0] for distribuidora in query_result]

        return distribuidoras

    def nome_distribuidoras_cds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT distribuidora FROM distribuidoras_cds'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        distribuidoras = [distribuidora[0] for distribuidora in query_result]

        return distribuidoras

    def titulos_dvds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT DISTINCT titulo FROM dvds'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def titulos_cds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT DISTINCT titulo FROM cds'

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def titulos_livros_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT titulo
            FROM livros
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def autores_livros_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT autor
            FROM livros
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        autores = [autor[0] for autor in query_result]

        return autores

    def editoras_livros_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT editora
            FROM livros
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        editoras = [editora[0] for editora in query_result]

        return editoras

    def titulos_livros_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT titulo
            FROM livros
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def autores_livros_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT autor
            FROM livros
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        autores = [autor[0] for autor in query_result]

        return autores

    def editoras_livros_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT editora
            FROM livros
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        editoras = [editora[0] for editora in query_result]

        return editoras

    def titulos_cds_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT titulo
            FROM cds
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def autores_artistas_cds_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT artista
            FROM cds
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        artistas = [artista[0] for artista in query_result]

        return artistas

    def distribuidoras_cds_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT distribuidora
            FROM cds
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        distribuidoras = [distribuidora[0] for distribuidora in query_result]

        return distribuidoras

    def titulos_cds_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT titulo
            FROM cds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def autores_artistas_cds_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT artista
            FROM cds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        artistas = [artista[0] for artista in query_result]

        return artistas

    def distribuidoras_cds_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT distribuidora
            FROM cds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        distribuidoras = [distribuidora[0] for distribuidora in query_result]

        return distribuidoras

    def titulos_dvds_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT titulo
            FROM dvds
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def diretores_dvds_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT diretor
            FROM dvds
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        diretores = [diretor[0] for diretor in query_result]

        return diretores

    def distribuidoras_dvds_disponiveis(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT distribuidora
            FROM dvds
            WHERE situacao = 'Disponível'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        distribuidoras = [distribuidora[0] for distribuidora in query_result]

        return distribuidoras

    def titulos_dvds_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT titulo
            FROM dvds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        titulos = [titulo[0] for titulo in query_result]

        return titulos

    def diretores_dvds_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT diretor
            FROM dvds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        diretores = [diretor[0] for diretor in query_result]

        return diretores

    def distribuidoras_dvds_emprestados(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT distribuidora
            FROM dvds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        distribuidoras = [distribuidora[0] for distribuidora in query_result]

        return distribuidoras

    def beneficiados_livros(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT beneficiado
            FROM livros
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        beneficiados = [beneficiado[0] for beneficiado in query_result]

        return beneficiados

    def beneficiados_cds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT beneficiado
            FROM cds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        beneficiados = [beneficiado[0] for beneficiado in query_result]

        return beneficiados

    def beneficiados_dvds(self):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = '''
            SELECT DISTINCT beneficiado
            FROM dvds
            WHERE situacao = 'Emprestado'
        '''

        query_result = cursor.execute(query).fetchall()

        cursor.close()

        connection.close()

        beneficiados = [beneficiado[0] for beneficiado in query_result]

        return beneficiados

    def titulos_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv', index_col=False)

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def autores_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv', index_col=False)

        autores = df['autor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return autores

    def editoras_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv', index_col=False)

        editoras = df['editora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return editoras

    def titulos_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv', index_col=False)

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def autores_artistas_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv', index_col=False)

        autores_artistas = df['artista_autor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return autores_artistas

    def distribuidoras_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return distribuidoras

    def titulos_dvds_emprestimo_expirado(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def diretores_dvds_emprestimo_expirado(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        diretores = df['diretor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return diretores

    def distribuidoras_dvds_emprestimo_expirado(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna().unique().tolist()

        return distribuidoras

    def editar_livro(self, id, titulo, autor_selecionado, novo_autor, editora_selecionada, nova_editora, n_pag, situacao, beneficiado, tel, dt_emprestimo, dt_devolucao):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        sql = '''
            UPDATE livros
            SET titulo = ?,
                autor = ?,
                editora = ?,
                n_paginas = ?,
                situacao = ?,
                beneficiado = ?,
                telefone = ?,
                dt_emprestimo = ?,
                dt_devolucao = ?
            WHERE id = ?
        '''

        values = (titulo, novo_autor, nova_editora, n_pag, situacao,
                  beneficiado, tel, dt_emprestimo, dt_devolucao, id)

        cursor.execute(sql, values)

        connection.commit()

        self.add_autor(novo_autor)
        self.add_editora(nova_editora)

        query_1 = 'SELECT autor FROM livros'
        query_2 = 'SELECT editora FROM livros'

        autores = cursor.execute(query_1).fetchall()

        editoras = cursor.execute(query_2).fetchall()

        if (autor_selecionado,) not in autores:
            sql = 'DELETE FROM autores WHERE autor = ?'
            values = (autor_selecionado,)

            cursor.execute(sql, values)

            connection.commit()

        if (editora_selecionada,) not in editoras:
            sql = 'DELETE FROM editoras WHERE editora = ?'
            values = (editora_selecionada,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def excluir_livro(self, id, autor_selecionado, editora_selecionada):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        sql = '''
            DELETE FROM livros
            WHERE id = ?
        '''

        values = (id,)

        cursor.execute(sql, values)

        connection.commit()

        query_1 = 'SELECT autor FROM livros'
        query_2 = 'SELECT editora FROM livros'

        autores = cursor.execute(query_1).fetchall()

        editoras = cursor.execute(query_2).fetchall()

        if (autor_selecionado,) not in autores:
            sql = 'DELETE FROM autores WHERE autor = ?'
            values = (autor_selecionado,)

            cursor.execute(sql, values)

            connection.commit()

        if (editora_selecionada,) not in editoras:
            sql = 'DELETE FROM editoras WHERE editora = ?'
            values = (editora_selecionada,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def editar_autor_livro(self, id, autor_selecionado, novo_autor):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT autor FROM autores'

        autores = cursor.execute(query).fetchall()

        if (novo_autor,) in autores:
            sql = '''
                DELETE FROM autores
                WHERE id = ?
            '''

            values = (id,)

            cursor.execute(sql, values)

            connection.commit()

        else:
            sql = '''
                UPDATE autores
                SET autor = ?
                WHERE id = ?
            '''

            values = (novo_autor, id)

            cursor.execute(sql, values)

            connection.commit()

        sql = '''
            UPDATE livros
            SET autor = ?
            WHERE autor = ?
        '''

        values = (novo_autor, autor_selecionado)

        cursor.execute(sql, values)

        connection.commit()

        cursor.close()

        connection.close()

    def editar_editora_livro(self, id, editora_selecionada, nova_editora):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT editora FROM editoras'

        editoras = cursor.execute(query).fetchall()

        if (nova_editora,) in editoras:
            sql = '''
                DELETE FROM editoras
                WHERE id = ?
            '''

            values = (id,)

            cursor.execute(sql, values)

            connection.commit()

        else:
            sql = '''
                UPDATE editoras
                SET editora = ?
                WHERE id = ?
            '''

            values = (nova_editora, id)

            cursor.execute(sql, values)

            connection.commit()

        sql = '''
            UPDATE livros
            SET editora = ?
            WHERE editora = ?
        '''

        values = (nova_editora, editora_selecionada)

        cursor.execute(sql, values)

        connection.commit()

        cursor.close()

        connection.close()

    def editar_dvd(self, id, titulo, diretor_selecionado, novo_diretor, distribuidora_selecionada, nova_distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        sql = '''
            UPDATE dvds
            SET titulo = ?,
                diretor = ?,
                distribuidora = ?,
                duracao = ?,
                situacao = ?,
                beneficiado = ?,
                telefone = ?,
                dt_emprestimo = ?,
                dt_devolucao = ?
            WHERE id = ?
        '''

        values = (titulo, novo_diretor, nova_distribuidora, tempo, situacao,
                  beneficiado, telefone, dt_emprestimo, dt_devolucao, id)

        cursor.execute(sql, values)

        connection.commit()

        self.add_diretor_dvd(novo_diretor)
        self.add_distribuidora_dvd(nova_distribuidora)

        query_1 = 'SELECT diretor FROM dvds'
        query_2 = 'SELECT distribuidora FROM dvds'

        diretores = cursor.execute(query_1).fetchall()
        distribuidoras = cursor.execute(query_2).fetchall()

        if (diretor_selecionado,) not in diretores:
            sql = '''
                DELETE FROM diretores
                WHERE diretor = ?
            '''

            values = (diretor_selecionado,)

            cursor.execute(sql, values)

            connection.commit()

        if (distribuidora_selecionada,) not in distribuidoras:
            sql = '''
                DELETE FROM distribuidoras_dvds
                WHERE distribuidora = ?
            '''

            values = (distribuidora_selecionada,)

            cursor.execute(sql, values)

            connection.commit()

        cursor.close()

        connection.close()

    def editar_diretor_dvd(self, diretor_selecionado, novo_diretor):
        connection = sqlite3.connect(self.db_name)

        cursor = connection.cursor()

        query = 'SELECT diretor FROM diretores'

        diretores = cursor.execute(query).fetchall()

        if (novo_diretor,) in diretores:
            sql = '''
                DELETE FROM diretores
                WHERE diretor = ?
            '''

            values = (diretor_selecionado,)

            cursor.execute(sql, values)

            connection.commit()

        else:
            sql = '''
                UPDATE diretores
                SET diretor = ?
                WHERE diretor = ?
            '''

            values = (novo_diretor, diretor_selecionado)

            cursor.execute(sql, values)

            connection.commit()

        sql = '''
            UPDATE dvds
            SET diretor = ?
            WHERE diretor = ?
        '''

        values = (novo_diretor, diretor_selecionado)

        cursor.execute(sql, values)

        connection.commit()

        cursor.close()

        connection.close()

    def editar_distribuidora_dvd(self, distribuidora_selecionada, nova_distribuidora):
        df_dvds = pd.read_csv('dvds.csv')
        df_distribuidoras = pd.read_csv('distribuidoras_dvds.csv')

        distribuidoras = df_distribuidoras['distribuidora'].to_list()

        if nova_distribuidora in distribuidoras:
            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora']
                                                      != distribuidora_selecionada]

        else:
            df_distribuidoras.loc[df_distribuidoras['distribuidora'] ==
                                  distribuidora_selecionada, 'distribuidora'] = nova_distribuidora

        df_dvds.loc[df_dvds['distribuidora'] ==
                    distribuidora_selecionada, 'distribuidora'] = nova_distribuidora

        df_dvds.loc[:, 'id':'dt_devolucao'].to_csv('dvds.csv', index=False)
        df_distribuidoras.loc[:, 'id':'distribuidora'].to_csv(
            'distribuidoras_dvds.csv', index=False)

    def excluir_dvd(self, id, diretor, distribuidora):
        df_dvds = pd.read_csv('dvds.csv', index_col=False)
        df_diretores = pd.read_csv('diretores_dvds.csv', index_col=False)
        df_distribuidoras = pd.read_csv(
            'distribuidoras_dvds.csv', index_col=False)

        df_dvds = df_dvds.loc[df_dvds['id'] != id]

        diretores = df_dvds['diretor'].to_list()
        distribuidoras = df_dvds['distribuidora'].to_list()

        if diretor not in diretores:
            df_diretores = df_diretores.loc[df_diretores['diretor'] != diretor]

            df_diretores.loc[:, 'id':'diretor'].to_csv('diretores_dvds.csv')

        if distribuidora not in distribuidoras:
            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora'] != distribuidora]

            df_distribuidoras.loc[:, 'id':'distribuidora'].to_csv(
                'distribuidoras_dvds.csv')

        df_dvds.loc[:, 'id':'dt_devolucao'].to_csv('dvds.csv', index=False)

    def editar_cd(self, id, titulo, autor_artista_selecionado, novo_autor_artista, distribuidora_selecionada, nova_distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df_cds = pd.read_csv('cds.csv', index_col=False)

        df_cds.loc[df_cds['id'] == id, 'titulo'] = titulo
        df_cds.loc[df_cds['id'] == id, 'artista_autor'] = novo_autor_artista
        df_cds.loc[df_cds['id'] == id, 'distribuidora'] = nova_distribuidora
        df_cds.loc[df_cds['id'] == id, 'tempo'] = tempo
        df_cds.loc[df_cds['id'] == id, 'situacao'] = situacao
        df_cds.loc[df_cds['id'] == id, 'beneficiado'] = beneficiado
        df_cds.loc[df_cds['id'] == id, 'telefone'] = telefone
        df_cds.loc[df_cds['id'] == id, 'dt_emprestimo'] = dt_emprestimo
        df_cds.loc[df_cds['id'] == id, 'dt_devolucao'] = dt_devolucao

        self.add_autor_artista_cd(novo_autor_artista)
        self.add_distribuidora_cd(nova_distribuidora)

        autores_artistas = df_cds['artista_autor'].to_list()
        distribuidoras = df_cds['distribuidora'].to_list()

        if autor_artista_selecionado not in autores_artistas:
            df_autor_artista = pd.read_csv(
                'autores_artistas_cds.csv', index_col=False)

            df_autor_artista = df_autor_artista.loc[df_autor_artista['autor_artista']
                                                    != autor_artista_selecionado]

            df_autor_artista.loc[:, 'id':'autor_artista'].to_csv(
                'autores_artistas_cds.csv', index=False)

        if distribuidora_selecionada not in distribuidoras:
            df_distribuidoras = pd.read_csv(
                'distribuidoras_cds.csv', index_col=False)

            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora']
                                                      != distribuidora_selecionada]

            df_distribuidoras.loc[:, 'id':'distribuidora'].to_csv(
                'distribuidoras_cds.csv', index=False)

        df_cds.loc[:, 'id':'dt_devolucao'].to_csv('cds.csv', index=False)

    def editar_autor_artista_cd(self, autor_artista_selecionado, novo_autor_artista):
        df_cds = pd.read_csv('cds.csv')
        df_autor_artista = pd.read_csv('autores_artistas_cds.csv')

        autores_artistas = df_autor_artista['autor_artista'].to_list()

        if novo_autor_artista in autores_artistas:
            df_autor_artista = df_autor_artista.loc[df_autor_artista['autor_artista']
                                                    != autor_artista_selecionado]

        else:
            df_autor_artista.loc[df_autor_artista['autor_artista'] ==
                                 autor_artista_selecionado, 'autor_artista'] = novo_autor_artista

        df_cds.loc[df_cds['artista_autor'] == autor_artista_selecionado,
                   'artista_autor'] = novo_autor_artista

        df_cds.loc[:, 'id':'dt_devolucao'].to_csv('cds.csv', index=False)
        df_autor_artista.loc[:, 'id':'autor_artista'].to_csv(
            'autores_artistas_cds.csv', index=False)

    def editar_distribuidora_cd(self, distribuidora_selecionada, nova_distribuidora):
        df_cds = pd.read_csv('cds.csv')
        df_distribuidoras = pd.read_csv('distribuidoras_cds.csv')

        distribuidoras = df_distribuidoras['distribuidora'].to_list()

        if nova_distribuidora in distribuidoras:
            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora']
                                                      != distribuidora_selecionada]

        else:
            df_distribuidoras.loc[df_distribuidoras['distribuidora'] ==
                                  distribuidora_selecionada, 'distribuidora'] = nova_distribuidora

        df_cds.loc[df_cds['distribuidora'] == distribuidora_selecionada,
                   'distribuidora'] = nova_distribuidora

        df_cds.loc[:, 'id':'dt_devolucao'].to_csv('cds.csv', index=False)
        df_distribuidoras.loc[:, 'id':'distribuidora'].to_csv(
            'distribuidoras_cds.csv', index=False)

    def excluir_cd(self, id, autor_artista, distribuidora):
        df_cds = pd.read_csv('cds.csv', index_col=False)
        df_autores_artistas = pd.read_csv(
            'autores_artistas_cds.csv', index_col=False)
        df_distribuidoras = pd.read_csv(
            'distribuidoras_cds.csv', index_col=False)

        df_cds = df_cds.loc[df_cds['id'] != id]

        autores_artistas = df_cds['artista_autor'].to_list()
        distribuidoras = df_cds['distribuidora'].to_list()

        if autor_artista not in autores_artistas:
            df_autores_artistas = df_autores_artistas.loc[
                df_autores_artistas['autor_artista'] != autor_artista]

            df_autores_artistas.loc[:, 'id':'autor_artista'].to_csv(
                'autores_artistas_cds.csv', index=False)

        if distribuidora not in distribuidoras:
            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora'] != distribuidora]

            df_distribuidoras.loc[:, 'id':'distribuidora'].to_csv(
                'distribuidoras_cds.csv', index=False)

        df_cds.loc[:, 'id':'dt_devolucao'].to_csv('cds.csv', index=False)

    def pesquisar_livro(self, entrada, campo_pesquisa):
        df = pd.read_csv('livros.csv', index_col=False)

        if campo_pesquisa == 'Título (Todos)':
            resultado = df.loc[df['titulo'] == entrada]

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Autor (Todos)':
            resultado = df.loc[df['autor'] == entrada]

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Editora (Todos)':
            resultado = df.loc[df['editora'] == entrada]

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Título (Disponíveis)':
            resultado = df.loc[df['titulo'] == entrada].where(
                df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Autor (Disponíveis)':
            resultado = df.loc[df['autor'] == entrada].where(
                df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Editora (Disponíveis)':
            resultado = df.loc[df['editora'] == entrada].where(
                df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Título (Emprestados)':
            resultado = df.loc[df['titulo'] == entrada].where(
                df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Autor (Emprestados)':
            resultado = df.loc[df['autor'] == entrada].where(
                df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Editora (Emprestados)':
            resultado = df.loc[df['editora'] == entrada].where(
                df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Título (Empréstimo Expirado)':
            resultado = df.loc[df['titulo'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Autor (Empréstimo Expirado)':
            resultado = df.loc[df['autor'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Editora (Empréstimo Expirado)':
            resultado = df.loc[df['editora'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Beneficiado':
            resultado = df.loc[df['beneficiado'] == entrada]

            resultado['id'] = resultado['id'].astype('int64')
            resultado['n_pag'] = resultado['n_pag'].astype('int64')

            return resultado.values.tolist()

    def pesquisar_autor(self, entrada):
        df = pd.read_csv('autores_livros.csv', index_col=False)

        resultado = df.loc[df['autor'] == entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_editora(self, entrada):
        df = pd.read_csv('editoras_livros.csv', index_col=False)

        resultado = df.loc[df['editora'] == entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_cd(self, entrada, campo_pesquisa):
        df = pd.read_csv('cds.csv', index_col=False)

        if campo_pesquisa == 'Título (Todos)':
            resultado = df.loc[df['titulo'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Artista/Autor (Todos)':
            resultado = df.loc[df['artista_autor'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Todos)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Disponíveis)':
            resultado = df.loc[df['titulo'] ==
                               entrada].where(df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Artista/Autor (Disponíveis)':
            resultado = df.loc[df['artista_autor'] ==
                               entrada].where(df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Distribuidora (Disponíveis)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Título (Emprestados)':
            resultado = df.loc[df['titulo'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Artista/Autor (Emprestados)':
            resultado = df.loc[df['artista_autor'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Distribuidora (Emprestados)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Título (Empréstimo Expirado)':
            resultado = df.loc[df['titulo'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Artista/Autor (Empréstimo Expirado)':
            resultado = df.loc[df['artista_autor'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Distribuidora (Empréstimo Expirado)':
            resultado = df.loc[df['distribuidora'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Beneficiado':
            resultado = df.loc[df['beneficiado'] == entrada]

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

    def pesquisar_dvd(self, entrada, campo_pesquisa):
        df = pd.read_csv('dvds.csv', index_col=False)

        if campo_pesquisa == 'Título (Todos)':
            resultado = df.loc[df['titulo'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Diretor (Todos)':
            resultado = df.loc[df['diretor'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Todos)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Disponíveis)':
            resultado = df.loc[df['titulo'] ==
                               entrada].where(df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Diretor (Disponíveis)':
            resultado = df.loc[df['diretor'] ==
                               entrada].where(df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Distribuidora (Disponíveis)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Disponível').dropna(axis=0, how='all')

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.fillna('').values.tolist()

        elif campo_pesquisa == 'Título (Emprestados)':
            resultado = df.loc[df['titulo'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Diretor (Emprestados)':
            resultado = df.loc[df['diretor'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Distribuidora (Emprestados)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Título (Empréstimo Expirado)':
            resultado = df.loc[df['titulo'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Diretor (Empréstimo Expirado)':
            resultado = df.loc[df['diretor'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Distribuidora (Empréstimo Expirado)':
            resultado = df.loc[df['distribuidora'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna(), format='%d/%m/%Y').dt.date < date.today()).dropna()

            resultado['id'] = resultado['id'].astype('int64')

            return resultado.values.tolist()

        elif campo_pesquisa == 'Beneficiado':
            resultado = df.loc[df['beneficiado'] == entrada].values.tolist()

            return resultado

    def pesquisar_autor_artista_cd(self, entrada):
        df = pd.read_csv('autores_artistas_cds.csv', index_col=False)

        resultado = df.loc[df['autor_artista'] ==
                           entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_diretor_dvd(self, entrada):
        df = pd.read_csv('diretores_dvds.csv', index_col=False)

        resultado = df.loc[df['diretor'] == entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_distribuidora_cd(self, entrada):
        df = pd.read_csv('distribuidoras_cds.csv', index_col=False)

        resultado = df.loc[df['distribuidora'] ==
                           entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_distribuidora_dvd(self, entrada):
        df = pd.read_csv('distribuidoras_dvds.csv', index_col=False)

        resultado = df.loc[df['distribuidora'] ==
                           entrada].fillna('').values.tolist()

        return resultado

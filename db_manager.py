import pandas as pd
from datetime import date


class db_manager:
    def __init__(self):
        pass

    def get_livros(self):
        df = pd.read_csv('livros.csv')

        livros = df.loc[:, 'id':'dt_devolucao'].fillna('').values.tolist()

        return livros

    def get_cds(self):
        df = pd.read_csv('cds.csv')

        cds = df.loc[:, 'id':'dt_devolucao'].fillna('').values.tolist()

        return cds

    def get_dvds(self):
        df = pd.read_csv('dvds.csv')

        dvds = df.loc[:, 'id':'dt_devolucao'].fillna('').values.tolist()

        return dvds

    def get_artistas(self):
        df = pd.read_csv('autores_artistas_cds.csv')

        artistas = df.loc[:, 'id':'autor_artista'].fillna('').values.tolist()

        return artistas

    def get_autores(self):
        df = pd.read_csv('autores_livros.csv')

        autores = df.loc[:, 'id':'autor'].fillna('').values.tolist()

        return autores

    def get_editoras(self):
        df = pd.read_csv('editoras_livros.csv')

        editoras = df.loc[:, 'id':'editora'].fillna('').values.tolist()

        return editoras

    def get_diretores(self):
        df = pd.read_csv('diretores_dvds.csv')

        diretores = df.loc[:, 'id':'diretor'].fillna('').values.tolist()

        return diretores

    def get_distribuidoras_cds(self):
        df = pd.read_csv('distribuidoras_cds.csv')

        distribuidoras = df.loc[:, 'id':'distribuidora'].fillna(
            '').values.tolist()

        return distribuidoras

    def get_distribuidoras_dvds(self):
        df = pd.read_csv('distribuidoras_dvds.csv')

        distribuidoras = df.loc[:, 'id':'distribuidora'].fillna(
            '').values.tolist()

        return distribuidoras

    def add_livro(self, titulo, autor, editora, n_pag, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df = pd.read_csv('livros.csv')

        id = len(df) + \
            1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

        new_row = {
            'id': id,
            'titulo': titulo,
            'autor': autor,
            'editora': editora,
            'n_pag': n_pag,
            'situacao': situacao,
            'beneficiado': beneficiado,
            'telefone': telefone,
            'dt_emprestimo': dt_emprestimo,
            'dt_devolucao': dt_devolucao
        }

        df = df.append(new_row, ignore_index=True)

        df.to_csv('livros.csv', index=False)

        self.add_autor(autor)
        self.add_editora(editora)

    def add_autor(self, autor):
        df = pd.read_csv('autores_livros.csv')

        if autor not in self.nome_autores():
            id = len(df) + \
                1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

            new_row = {
                'id': id,
                'autor': autor
            }

            df = df.append(new_row, ignore_index=True)

            df.to_csv('autores_livros.csv', index=False)

    def add_editora(self, editora):
        df = pd.read_csv('editoras_livros.csv')

        editoras = df['editora'].to_list()

        if editora not in editoras:
            id = len(df) + \
                1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

            new_row = {
                'id': id,
                'editora': editora
            }

            df = df.append(new_row, ignore_index=True)

            df.to_csv('editoras_livros.csv', index=False)

    def add_dvd(self, titulo, diretor, distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df = pd.read_csv('dvds.csv', index_col=False)

        id = len(df) + \
            1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

        new_row = {
            'id': id,
            'titulo': titulo,
            'diretor': diretor,
            'distribuidora': distribuidora,
            'tempo': tempo,
            'situacao': situacao,
            'beneficiado': beneficiado,
            'telefone': telefone,
            'dt_emprestimo': dt_emprestimo,
            'dt_devolucao': dt_devolucao
        }

        df = df.append(new_row, ignore_index=True)

        df.to_csv('dvds.csv', index=False)

        self.add_diretor_dvd(diretor)
        self.add_distribuidora_dvd(distribuidora)

    def add_cd(self, titulo, artista_autor, distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df = pd.read_csv('cds.csv', index_col=False)

        id = len(df) + \
            1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

        new_row = {
            'id': id,
            'titulo': titulo,
            'artista_autor': artista_autor,
            'distribuidora': distribuidora,
            'tempo': tempo,
            'situacao': situacao,
            'beneficiado': beneficiado,
            'telefone': telefone,
            'dt_emprestimo': dt_emprestimo,
            'dt_devolucao': dt_devolucao
        }

        df = df.append(new_row, ignore_index=True)

        df.to_csv('cds.csv', index=False)

        self.add_autor_artista_cd(artista_autor)
        self.add_distribuidora_cd(distribuidora)

    def add_diretor_dvd(self, diretor):
        df = pd.read_csv('diretores_dvds.csv', index_col=False)

        diretores = df['diretor'].to_list()

        if diretor not in diretores:
            id = len(df) + \
                1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

            new_row = {
                'id': id,
                'diretor': diretor
            }

            df = df.append(new_row, ignore_index=True)

            df.to_csv('diretores_dvds.csv', index=False)

    def add_autor_artista_cd(self, autor_artista):
        df = pd.read_csv('autores_artistas_cds.csv', index_col=False)

        autores_artistas = df['autor_artista'].to_list()

        if autor_artista not in autores_artistas:
            id = len(df) + \
                1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

            new_row = {
                'id': id,
                'autor_artista': autor_artista
            }

            df = df.append(new_row, ignore_index=True)

            df.to_csv('autores_artistas_cds.csv', index=False)

    def add_distribuidora_dvd(self, distribuidora):
        df = pd.read_csv('distribuidoras_dvds.csv', index_col=False)

        distribuidoras = df['distribuidora'].to_list()

        if distribuidora not in distribuidoras:
            id = len(df) + \
                1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

            new_row = {
                'id': id,
                'distribuidora': distribuidora
            }

            df = df.append(new_row, ignore_index=True)

            df.to_csv('distribuidoras_dvds.csv', index=False)

    def add_distribuidora_cd(self, distribuidora):
        df = pd.read_csv('distribuidoras_cds.csv', index_col=False)

        distribuidoras = df['distribuidora'].to_list()

        if distribuidora not in distribuidoras:
            id = len(df) + \
                1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

            new_row = {
                'id': id,
                'distribuidora': distribuidora
            }

            df = df.append(new_row, ignore_index=True)

            df.to_csv('distribuidoras_cds.csv', index=False)

    def nome_autores(self):
        df = pd.read_csv('autores_livros.csv')

        autores = df['autor'].to_list()

        return autores

    def nome_editoras(self):
        df = pd.read_csv('editoras_livros.csv')

        editoras = df['editora'].to_list()

        return editoras

    def titulo_livros(self):
        df = pd.read_csv('livros.csv')

        titulos = df['titulo'].unique().astype(str).tolist()

        return titulos

    def nome_diretores_dvds(self):
        df = pd.read_csv('diretores_dvds.csv')

        diretores = df['diretor'].to_list()

        return diretores

    def nome_autores_artistas_cds(self):
        df = pd.read_csv('autores_artistas_cds.csv', index_col=False)

        autores_artistas = df['autor_artista'].to_list()

        return autores_artistas

    def nome_distribuidoras_dvds(self):
        df = pd.read_csv('distribuidoras_dvds.csv', index_col=False)

        distribuidoras = df['distribuidora'].to_list()

        return distribuidoras

    def nome_distribuidoras_cds(self):
        df = pd.read_csv('distribuidoras_cds.csv', index_col=False)

        distribuidoras = df['distribuidora'].to_list()

        return distribuidoras

    def titulos_dvds(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        titulos = df['titulo'].unique().tolist()

        return titulos

    def titulos_cds(self):
        df = pd.read_csv('cds.csv', index_col=False)

        titulos = df['titulo'].unique().tolist()

        return titulos

    def titulos_livros_disponiveis(self):
        df = pd.read_csv('livros.csv', index_col=False)

        titulos = df['titulo'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return titulos

    def autores_livros_disponiveis(self):
        df = pd.read_csv('livros.csv', index_col=False)

        autores = df['autor'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return autores

    def editoras_livros_disponiveis(self):
        df = pd.read_csv('livros.csv', index_col=False)

        editoras = df['editora'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return editoras

    def titulos_livros_emprestados(self):
        df = pd.read_csv('livros.csv', index_col=False)

        titulos = df['titulo'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return titulos

    def autores_livros_emprestados(self):
        df = pd.read_csv('livros.csv', index_col=False)

        autores = df['autor'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return autores

    def editoras_livros_emprestados(self):
        df = pd.read_csv('livros.csv', index_col=False)

        editoras = df['editora'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return editoras

    def titulos_cds_disponiveis(self):
        df = pd.read_csv('cds.csv', index_col=False)

        titulos = df['titulo'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return titulos

    def autores_artistas_cds_disponiveis(self):
        df = pd.read_csv('cds.csv', index_col=False)

        autores_artistas = df['artista_autor'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return autores_artistas

    def distribuidoras_cds_disponiveis(self):
        df = pd.read_csv('cds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return distribuidoras

    def titulos_cds_emprestados(self):
        df = pd.read_csv('cds.csv', index_col=False)

        titulos = df['titulo'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return titulos

    def autores_artistas_cds_emprestados(self):
        df = pd.read_csv('cds.csv', index_col=False)

        autores_artistas = df['artista_autor'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return autores_artistas

    def distribuidoras_cds_emprestados(self):
        df = pd.read_csv('cds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return distribuidoras

    def titulos_dvds_disponiveis(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        titulos = df['titulo'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return titulos

    def diretores_dvds_disponiveis(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        diretores = df['diretor'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return diretores

    def distribuidoras_dvds_disponiveis(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return distribuidoras

    def titulos_dvds_emprestados(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        titulos = df['titulo'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return titulos

    def diretores_dvds_emprestados(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        diretores = df['diretor'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return diretores

    def distribuidoras_dvds_emprestados(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return distribuidoras

    def beneficiados_livros(self):
        df = pd.read_csv('livros.csv', index_col=False)

        beneficiados = df['beneficiado'].dropna().unique().tolist()

        return beneficiados

    def beneficiados_cds(self):
        df = pd.read_csv('cds.csv', index_col=False)

        beneficiados = df['beneficiado'].dropna().unique().tolist()

        return beneficiados

    def beneficiados_dvds(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        beneficiados = df['beneficiado'].dropna().unique().tolist()

        return beneficiados

    def titulos_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv', index_col=False)

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def autores_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv', index_col=False)

        autores = df['autor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return autores

    def editoras_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv', index_col=False)

        editoras = df['editora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return editoras

    def titulos_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv', index_col=False)

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def autores_artistas_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv', index_col=False)

        autores_artistas = df['artista_autor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return autores_artistas

    def distribuidoras_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return distribuidoras

    def titulos_dvds_emprestimo_expirado(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def diretores_dvds_emprestimo_expirado(self):
        df = pd.read_csv('dvds.csv', index_col=False)

        diretores = df['diretor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

        return diretores

    def distribuidoras_dvds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv', index_col=False)

        distribuidoras = df['distribuidora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

        return distribuidoras

    def editar_livro(self, id, titulo, autor_selecionado, novo_autor, editora_selecionada, nova_editora, n_pag, situacao, beneficiado, tel, dt_emprestimo, dt_devolucao):
        df_livros = pd.read_csv('livros.csv', index_col=False)

        df_livros.loc[id-1, 'titulo'] = titulo
        df_livros.loc[id-1, 'autor'] = novo_autor
        df_livros.loc[id-1, 'editora'] = nova_editora
        df_livros.loc[id-1, 'n_pag'] = n_pag
        df_livros.loc[id-1, 'situacao'] = situacao
        df_livros.loc[id-1, 'beneficiado'] = beneficiado
        df_livros.loc[id-1, 'telefone'] = tel
        df_livros.loc[id-1, 'dt_emprestimo'] = dt_emprestimo
        df_livros.loc[id-1, 'dt_devolucao'] = dt_devolucao

        self.add_autor(novo_autor)
        self.add_editora(nova_editora)

        autores = df_livros['autor'].to_list()
        editoras = df_livros['editora'].to_list()

        if autor_selecionado not in autores:
            df_autores_livros = pd.read_csv(
                'autores_livros.csv', index_col=False)

            df_autores_livros = df_autores_livros.loc[df_autores_livros['autor']
                                                      != autor_selecionado]

            df_autores_livros.to_csv('autores_livros.csv', index=False)

        if editora_selecionada not in editoras:
            df_editoras_livros = pd.read_csv(
                'editoras_livros.csv', index_col=False)

            df_editoras_livros = df_editoras_livros.loc[df_editoras_livros['editora']
                                                        != editora_selecionada]

            df_editoras_livros.to_csv('editoras_livros.csv', index=False)

        df_livros.to_csv('livros.csv', index=False)

    def excluir_livro(self, id, autor_selecionado, editora_selecionada):
        df_livros = pd.read_csv('livros.csv', index_col=False)
        df_autores_livros = pd.read_csv('autores_livros.csv', index_col=False)
        df_editoras_livros = pd.read_csv(
            'editoras_livros.csv', index_col=False)

        df_livros = df_livros.loc[df_livros['id'] != id]

        autores = df_livros['autor'].to_list()
        editoras = df_livros['editora'].to_list()

        if autor_selecionado not in autores:
            df_autores_livros = df_autores_livros.loc[df_autores_livros['autor']
                                                      != autor_selecionado]

            df_autores_livros.to_csv('autores_livros.csv', index=False)

        if editora_selecionada not in editoras:
            df_editoras_livros = df_editoras_livros.loc[df_editoras_livros['editora']
                                                        != editora_selecionada]

            df_editoras_livros.to_csv('editoras_livros.csv', index=False)

        df_livros.to_csv('livros.csv', index=False)

    def editar_autor_livro(self, id, autor_selecionado, novo_autor):
        df_livros = pd.read_csv('livros.csv', index_col=False)
        df_autores_livros = pd.read_csv('autores_livros.csv', index_col=False)

        df_autores_livros.loc[id - 1, 'autor'] = novo_autor

        df_livros.loc[df_livros['autor'] ==
                      autor_selecionado, 'autor'] = novo_autor

        df_livros.to_csv('livros.csv', index=False)
        df_autores_livros.to_csv('autores_livros.csv', index=False)

    def editar_editora_livro(self, id, editora_selecionada, nova_editora):
        df_livros = pd.read_csv('livros.csv', index_col=False)
        df_editoras_livros = pd.read_csv(
            'editoras_livros.csv', index_col=False)

        df_editoras_livros.loc[id - 1, 'editora'] = nova_editora

        df_livros.loc[df_livros['editora'] ==
                      editora_selecionada, 'editora'] = nova_editora

        df_livros.to_csv('livros.csv', index=False)
        df_editoras_livros.to_csv('editoras_livros.csv', index=False)

    def editar_dvd(self, id, titulo, diretor_selecionado, novo_diretor, distribuidora_selecionada, nova_distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df_dvds = pd.read_csv('dvds.csv', index_col=False)

        df_dvds.loc[id-1, 'titulo'] = titulo
        df_dvds.loc[id-1, 'diretor'] = novo_diretor
        df_dvds.loc[id-1, 'distribuidora'] = nova_distribuidora
        df_dvds.loc[id-1, 'tempo'] = tempo
        df_dvds.loc[id-1, 'situacao'] = situacao
        df_dvds.loc[id-1, 'beneficiado'] = beneficiado
        df_dvds.loc[id-1, 'telefone'] = telefone
        df_dvds.loc[id-1, 'dt_emprestimo'] = dt_emprestimo
        df_dvds.loc[id-1, 'dt_devolucao'] = dt_devolucao

        self.add_diretor_dvd(novo_diretor)
        self.add_distribuidora_dvd(nova_distribuidora)

        diretores = df_dvds['diretor'].to_list()
        distribuidoras = df_dvds['distribuidora'].to_list()

        if diretor_selecionado not in diretores:
            df_diretores_dvds = pd.read_csv(
                'diretores_dvds.csv', index_col=False)

            df_diretores_dvds = df_diretores_dvds.loc[df_diretores_dvds['diretor']
                                                      != diretor_selecionado]

            df_diretores_dvds.to_csv('diretores_dvds.csv', index=False)

        if distribuidora_selecionada not in distribuidoras:
            df_distribuidoras_dvds = pd.read_csv(
                'distribuidoras_dvds.csv', index_col=False)

            df_distribuidoras_dvds = df_distribuidoras_dvds.loc[
                df_distribuidoras_dvds['distribuidora'] != distribuidora_selecionada]

            df_distribuidoras_dvds.to_csv(
                'distribuidoras_dvds.csv', index=False)

        df_dvds.to_csv('dvds.csv', index=False)

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

            df_diretores.to_csv('diretores_dvds.csv')

        if distribuidora not in distribuidoras:
            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora'] != distribuidora]

            df_distribuidoras.to_csv('distribuidoras_dvds.csv')

        df_dvds.to_csv('dvds.csv', index=False)

    def editar_cd(self, id, titulo, autor_artista_selecionado, novo_autor_artista, distribuidora_selecionada, nova_distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df_cds = pd.read_csv('cds.csv', index_col=False)

        df_cds.loc[id-1, 'titulo'] = titulo
        df_cds.loc[id-1, 'artista_autor'] = novo_autor_artista
        df_cds.loc[id-1, 'distribuidora'] = nova_distribuidora
        df_cds.loc[id-1, 'tempo'] = tempo
        df_cds.loc[id-1, 'situacao'] = situacao
        df_cds.loc[id-1, 'beneficiado'] = beneficiado
        df_cds.loc[id-1, 'telefone'] = telefone
        df_cds.loc[id-1, 'dt_emprestimo'] = dt_emprestimo
        df_cds.loc[id-1, 'dt_devolucao'] = dt_devolucao

        self.add_autor_artista_cd(novo_autor_artista)
        self.add_distribuidora_cd(nova_distribuidora)

        autores_artistas = df_cds['artista_autor'].to_list()
        distribuidoras = df_cds['distribuidora'].to_list()

        if autor_artista_selecionado not in autores_artistas:
            df_autor_artista = pd.read_csv(
                'autores_artistas_cds.csv', index_col=False)

            df_autor_artista = df_autor_artista.loc[df_autor_artista['autor_artista']
                                                    != autor_artista_selecionado]

            df_autor_artista.to_csv('autores_artistas_cds.csv', index=False)

        if distribuidora_selecionada not in distribuidoras:
            df_distribuidoras = pd.read_csv(
                'distribuidoras_cds.csv', index_col=False)

            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora']
                                                      != distribuidora_selecionada]

            df_distribuidoras.to_csv('distribuidoras_cds.csv', index=False)

        df_cds.to_csv('cds.csv', index=False)

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

            df_autores_artistas.to_csv('autores_artistas_cds.csv', index=False)

        if distribuidora not in distribuidoras:
            df_distribuidoras = df_distribuidoras.loc[df_distribuidoras['distribuidora'] != distribuidora]

            df_distribuidoras.to_csv('distribuidoras_cds.csv', index=False)

        df_cds.to_csv('cds.csv', index=False)

    def pesquisar_livro(self, entrada, campo_pesquisa):
        df = pd.read_csv('livros.csv', index_col=False)

        if campo_pesquisa == 'Título (Todos)':
            resultado = df.loc[df['titulo'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Autor (Todos)':
            resultado = df.loc[df['autor'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Editora (Todos)':
            resultado = df.loc[df['editora'] ==
                               entrada].fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Disponíveis)':
            resultado = df.loc[df['titulo'] == entrada].where(
                df['situacao'] == 'Disponível').dropna(axis=0, how='all').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Autor (Disponíveis)':
            resultado = df.loc[df['autor'] == entrada].where(
                df['situacao'] == 'Disponível').dropna(axis=0, how='all').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Editora (Disponíveis)':
            resultado = df.loc[df['editora'] == entrada].where(
                df['situacao'] == 'Disponível').dropna(axis=0, how='all').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Emprestados)':
            resultado = df.loc[df['titulo'] == entrada].where(
                df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Autor (Emprestados)':
            resultado = df.loc[df['autor'] == entrada].where(
                df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Editora (Emprestados)':
            resultado = df.loc[df['editora'] == entrada].where(
                df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Empréstimo Expirado)':
            resultado = df.loc[df['titulo'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Autor (Empréstimo Expirado)':
            resultado = df.loc[df['autor'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Editora (Empréstimo Expirado)':
            resultado = df.loc[df['editora'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Beneficiado':
            resultado = df.loc[df['beneficiado'] == entrada].values.tolist()

            return resultado

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
                               entrada].where(df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Artista/Autor (Disponíveis)':
            resultado = df.loc[df['artista_autor'] ==
                               entrada].where(df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Disponíveis)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Emprestados)':
            resultado = df.loc[df['titulo'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Artista/Autor (Emprestados)':
            resultado = df.loc[df['artista_autor'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Emprestados)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Empréstimo Expirado)':
            resultado = df.loc[df['titulo'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Artista/Autor (Empréstimo Expirado)':
            resultado = df.loc[df['artista_autor'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Empréstimo Expirado)':
            resultado = df.loc[df['distribuidora'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Beneficiado':
            resultado = df.loc[df['beneficiado'] == entrada].values.tolist()

            return resultado

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
                               entrada].where(df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Diretor (Disponíveis)':
            resultado = df.loc[df['diretor'] ==
                               entrada].where(df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Disponíveis)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Emprestados)':
            resultado = df.loc[df['titulo'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Diretor (Emprestados)':
            resultado = df.loc[df['diretor'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Emprestados)':
            resultado = df.loc[df['distribuidora'] ==
                               entrada].where(df['situacao'] == 'Emprestado').dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Título (Empréstimo Expirado)':
            resultado = df.loc[df['titulo'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Diretor (Empréstimo Expirado)':
            resultado = df.loc[df['diretor'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

        elif campo_pesquisa == 'Distribuidora (Empréstimo Expirado)':
            resultado = df.loc[df['distribuidora'] == entrada].where(pd.to_datetime(
                df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

            return resultado

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

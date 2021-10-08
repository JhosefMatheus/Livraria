import pandas as pd
from datetime import date


class db_manager:
    def __init__(self):
        pass

    def get_data(self, file_name):
        df = pd.read_csv(file_name)

        df = df.fillna('')

        return df.values.tolist()

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
        df = pd.read_csv('dvds.csv')

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
        df = pd.read_csv('cds.csv')

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
        df = pd.read_csv('diretores_dvds.csv')

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
        df = pd.read_csv('autores_artistas_cds.csv')

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
        df = pd.read_csv('distribuidoras_dvds.csv')

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
        df = pd.read_csv('distribuidoras_cds.csv')

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

        titulos = df['titulo'].unique().tolist()

        return titulos

    def nome_diretores_dvds(self):
        df = pd.read_csv('diretores_dvds.csv')

        diretores = df['diretor'].to_list()

        return diretores

    def nome_autores_artistas_cds(self):
        df = pd.read_csv('autores_artistas_cds.csv')

        autores_artistas = df['autor_artista'].to_list()

        return autores_artistas

    def nome_distribuidoras_dvds(self):
        df = pd.read_csv('distribuidoras_dvds.csv')

        distribuidoras = df['distribuidora'].to_list()

        return distribuidoras

    def nome_distribuidoras_cds(self):
        df = pd.read_csv('distribuidoras_cds.csv')

        distribuidoras = df['distribuidora'].to_list()

        return distribuidoras

    def titulos_dvds(self):
        df = pd.read_csv('dvds.csv')

        titulos = df['titulo'].unique().tolist()

        return titulos

    def titulos_cds(self):
        df = pd.read_csv('cds.csv')

        titulos = df['titulo'].unique().tolist()

        return titulos

    def titulos_livros_disponiveis(self):
        df = pd.read_csv('livros.csv')

        titulos = df['titulo'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return titulos

    def autores_livros_disponiveis(self):
        df = pd.read_csv('livros.csv')

        autores = df['autor'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return autores

    def editoras_livros_disponiveis(self):
        df = pd.read_csv('livros.csv')

        editoras = df['editora'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return editoras

    def titulos_livros_emprestados(self):
        df = pd.read_csv('livros.csv')

        titulos = df['titulo'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return titulos

    def autores_livros_emprestados(self):
        df = pd.read_csv('livros.csv')

        autores = df['autor'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return autores

    def editoras_livros_emprestados(self):
        df = pd.read_csv('livros.csv')

        editoras = df['editora'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return editoras

    def titulos_cds_disponiveis(self):
        df = pd.read_csv('cds.csv')

        titulos = df['titulo'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return titulos

    def autores_artistas_cds_disponiveis(self):
        df = pd.read_csv('cds.csv')

        autores_artistas = df['artista_autor'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return autores_artistas

    def distribuidoras_cds_disponiveis(self):
        df = pd.read_csv('cds.csv')

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return distribuidoras

    def titulos_cds_emprestados(self):
        df = pd.read_csv('cds.csv')

        titulos = df['titulo'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return titulos

    def autores_artistas_cds_emprestados(self):
        df = pd.read_csv('cds.csv')

        autores_artistas = df['artista_autor'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return autores_artistas

    def distribuidoras_cds_emprestados(self):
        df = pd.read_csv('cds.csv')

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return distribuidoras

    def titulos_dvds_disponiveis(self):
        df = pd.read_csv('dvds.csv')

        titulos = df['titulo'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return titulos

    def diretores_dvds_disponiveis(self):
        df = pd.read_csv('dvds.csv')

        diretores = df['diretor'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return diretores

    def distribuidoras_dvds_disponiveis(self):
        df = pd.read_csv('dvds.csv')

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Disponível').dropna().unique().tolist()

        return distribuidoras

    def titulos_dvds_emprestados(self):
        df = pd.read_csv('dvds.csv')

        titulos = df['titulo'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return titulos

    def diretores_dvds_emprestados(self):
        df = pd.read_csv('dvds.csv')

        diretores = df['diretor'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return diretores

    def distribuidoras_dvds_emprestados(self):
        df = pd.read_csv('dvds.csv')

        distribuidoras = df['distribuidora'].where(
            df['situacao'] == 'Emprestado').dropna().unique().tolist()

        return distribuidoras

    def beneficiados_livros(self):
        df = pd.read_csv('livros.csv')

        beneficiados = df['beneficiado'].dropna().unique().tolist()

        return beneficiados

    def beneficiados_cds(self):
        df = pd.read_csv('cds.csv')

        beneficiados = df['beneficiado'].dropna().unique().tolist()

        return beneficiados

    def beneficiados_dvds(self):
        df = pd.read_csv('dvds.csv')

        beneficiados = df['beneficiado'].dropna().unique().tolist()

        return beneficiados

    def titulos_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv')

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def autores_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv')

        autores = df['autor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return autores

    def editoras_livros_emprestimo_expirado(self):
        df = pd.read_csv('livros.csv')

        editoras = df['editora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return editoras

    def titulos_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv')

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def autores_artistas_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv')

        autores_artistas = df['artista_autor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return autores_artistas

    def distribuidoras_cds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv')

        distribuidoras = df['distribuidora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return distribuidoras

    def titulos_dvds_emprestimo_expirado(self):
        df = pd.read_csv('dvds.csv')

        titulos = df['titulo'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().unique().tolist()

        return titulos

    def diretores_dvds_emprestimo_expirado(self):
        df = pd.read_csv('dvds.csv')

        diretores = df['diretor'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

        return diretores

    def distribuidoras_dvds_emprestimo_expirado(self):
        df = pd.read_csv('cds.csv')

        distribuidoras = df['distribuidora'].where(pd.to_datetime(
            df['dt_devolucao'].dropna()).dt.date < date.today()).dropna().values.tolist()

        return distribuidoras

    def editar_livro(self, id, titulo, autor_selecionado, novo_autor, editora_selecionada, nova_editora, n_pag, situacao, beneficiado, tel, dt_emprestimo, dt_devolucao):
        df_livros = pd.read_csv('livros.csv')

        df_livros.loc[id-1, 'titulo'] = titulo
        df_livros.loc[id-1, 'autor'] = novo_autor
        df_livros.loc[id-1, 'editora'] = nova_editora
        df_livros.loc[id-1, 'n_pag'] = n_pag
        df_livros.loc[id-1, 'situacao'] = situacao
        df_livros.loc[id-1, 'beneficiado'] = beneficiado
        df_livros.loc[id-1, 'telefone'] = tel
        df_livros.loc[id-1, 'dt_emprestimo'] = dt_emprestimo
        df_livros.loc[id-1, 'dt_devolucao'] = dt_devolucao

        df_livros.to_csv('livros.csv', index=False)

        self.add_autor(novo_autor)
        self.add_editora(nova_editora)

        df_livros = pd.read_csv('livros.csv')

        autores = df_livros['autor'].to_list()
        editoras = df_livros['editora'].to_list()

        if autor_selecionado not in autores:
            df_autores_livros = pd.read_csv('autores_livros.csv')

            id_autor = df_autores_livros.index[df_autores_livros['autor'] == autor_selecionado].tolist(
            )

            df_autores_livros.drop(id_autor, axis=0, inplace=True)

            df_autores_livros.to_csv('autores_livros.csv', index=False)

        if editora_selecionada not in editoras:
            df_editoras_livros = pd.read_csv('editoras_livros.csv')

            id_editora = df_editoras_livros.index[df_editoras_livros['editora'] == editora_selecionada].tolist(
            )

            df_editoras_livros.drop(id_editora, axis=0, inplace=True)

            df_editoras_livros.to_csv('editoras_livros.csv', index=False)

    def excluir_livro(self, id, autor_selecionado, editora_selecionada):
        df_livros = pd.read_csv('livros.csv')
        df_autores_livros = pd.read_csv('autores_livros.csv')
        df_editoras_livros = pd.read_csv('editoras_livros.csv')

        id_livro = df_livros.index[df_livros['id'] == id].tolist()

        df_livros.drop(id_livro, axis=0, inplace=True)

        autores = df_livros['autor'].to_list()
        editoras = df_livros['editora'].to_list()

        if autor_selecionado not in autores:
            id_autor = df_autores_livros.index[df_autores_livros['autor'] == autor_selecionado].tolist(
            )

            df_autores_livros.drop(id_autor, axis=0, inplace=True)

            df_autores_livros.to_csv('autores_livros.csv', index=False)

        if editora_selecionada not in editoras:
            id_editora = df_editoras_livros.index[df_editoras_livros['editora'] == editora_selecionada].tolist(
            )

            df_editoras_livros.drop(id_editora, axis=0, inplace=True)

            df_editoras_livros.to_csv('editoras_livros.csv', index=False)

        df_livros.to_csv('livros.csv', index=False)

    def editar_autor_livro(self, id, autor_selecionado, novo_autor):
        df_livros = pd.read_csv('livros.csv')
        df_autores_livros = pd.read_csv('autores_livros.csv')

        df_autores_livros.loc[id - 1, 'autor'] = novo_autor

        df_livros.loc[df_livros['autor'] ==
                      autor_selecionado, 'autor'] = novo_autor

        df_livros.to_csv('livros.csv', index=False)
        df_autores_livros.to_csv('autores_livros.csv', index=False)

    def editar_editora_livro(self, id, editora_selecionada, nova_editora):
        df_livros = pd.read_csv('livros.csv')
        df_editoras_livros = pd.read_csv('editoras_livros.csv')

        df_editoras_livros.loc[id - 1, 'editora'] = nova_editora

        df_livros.loc[df_livros['editora'] ==
                      editora_selecionada, 'editora'] = nova_editora

        df_livros.to_csv('livros.csv', index=False)
        df_editoras_livros.to_csv('editoras_livros.csv', index=False)

    def editar_dvd(self, id, titulo, diretor_selecionado, novo_diretor, distribuidora_selecionada, nova_distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df_dvds = pd.read_csv('dvds.csv')

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
            df_diretores_dvds = pd.read_csv('diretores_dvds.csv')

            id_diretor = df_diretores_dvds.index[df_diretores_dvds['diretor'] == diretor_selecionado].tolist(
            )

            df_diretores_dvds.drop(id_diretor, axis=0, inplace=True)

            df_diretores_dvds.to_csv('diretores_dvds.csv', index=False)

        if distribuidora_selecionada not in distribuidoras:
            df_distribuidoras_dvds = pd.read_csv('distribuidoras_dvds.csv')

            id_distribuidora = df_distribuidoras_dvds.index[df_distribuidoras_dvds['distribuidora'] == distribuidora_selecionada].tolist(
            )

            df_distribuidoras_dvds.drop(id_distribuidora, axis=0, inplace=True)

            df_distribuidoras_dvds.to_csv(
                'distribuidoras_dvds.csv', index=False)

        df_dvds.to_csv('dvds.csv', index=False)

    def excluir_dvd(self, id, diretor, distribuidora):
        df_dvds = pd.read_csv('dvds.csv')
        df_diretores = pd.read_csv('diretores_dvds.csv')
        df_distribuidoras = pd.read_csv('distribuidoras_dvds.csv')

        id_dvd = df_dvds.index[df_dvds['id'] == id].tolist()

        df_dvds.drop(id_dvd, axis=0, inplace=True)

        diretores = df_dvds['diretor'].to_list()
        distribuidoras = df_dvds['distribuidora'].to_list()

        if diretor not in diretores:
            id_diretor = df_diretores.index[df_diretores['diretor'] == diretor].tolist(
            )

            df_diretores.drop(id_diretor, axis=0, inplace=True)

            df_diretores.to_csv('diretores_dvds.csv')

        if distribuidora not in distribuidoras:
            id_distribuidora = df_distribuidoras.index[df_distribuidoras['distribuidora'] == distribuidora].tolist(
            )

            df_distribuidoras.drop(id_distribuidora, axis=0, inplace=True)

            df_distribuidoras.to_csv('distribuidoras_dvds.csv')

        df_dvds.to_csv('dvds.csv', index=False)

    def editar_cd(self, id, titulo, autor_artista_selecionado, novo_autor_artista, distribuidora_selecionada, nova_distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        df_cds = pd.read_csv('cds.csv')

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
            df_autor_artista = pd.read_csv('autores_artistas_cds.csv')

            id_autor_artista = df_autor_artista.index[df_autor_artista['autor_artista']
                                                      == autor_artista_selecionado].tolist()

            df_autor_artista.drop(id_autor_artista, axis=0, inplace=True)

            df_autor_artista.to_csv('autores_artistas_cds.csv', index=False)

        if distribuidora_selecionada not in distribuidoras:
            df_distribuidoras = pd.read_csv('distribuidoras_cds.csv')

            id_distribuidora = df_distribuidoras.index[df_distribuidoras['distribuidora']
                                                       == distribuidora_selecionada].tolist()

            df_distribuidoras.drop(id_distribuidora, axis=0, inplace=True)

            df_distribuidoras.to_csv('distribuidoras_cds.csv', index=False)

        df_cds.to_csv('cds.csv', index=False)

    def excluir_cd(self, id, autor_artista, distribuidora):
        df_cds = pd.read_csv('cds.csv')
        df_autores_artistas = pd.read_csv('autores_artistas_cds.csv')
        df_distribuidoras = pd.read_csv('distribuidoras_cds.csv')

        id_cd = df_cds.index[df_cds['id'] == id].tolist()

        df_cds.drop(id_cd, axis=0, inplace=True)

        autores_artistas = df_cds['artista_autor'].to_list()
        distribuidoras = df_cds['distribuidora'].to_list()

        if autor_artista not in autores_artistas:
            id_autor_artista = df_autores_artistas.index[df_autores_artistas['autor_artista'] == autor_artista].tolist(
            )

            df_autores_artistas.drop(id_autor_artista, axis=0, inplace=True)

            df_autores_artistas.to_csv('autores_artistas_cds.csv', index=False)

        if distribuidora not in distribuidoras:
            id_distribuidora = df_distribuidoras.index[df_distribuidoras['distribuidora'] == distribuidora].tolist(
            )

            df_distribuidoras.drop(id_distribuidora, axis=0, inplace=True)

            df_distribuidoras.to_csv('distribuidoras_cds.csv', index=False)

        df_cds.to_csv('cds.csv', index=False)

    def pesquisar_livro(self, entrada, campo_pesquisa):
        df = pd.read_csv('livros.csv')

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
                df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Autor (Disponíveis)':
            resultado = df.loc[df['autor'] == entrada].where(
                df['situacao'] == 'Disponível').fillna('').values.tolist()

            return resultado

        elif campo_pesquisa == 'Editora (Disponíveis)':
            resultado = df.loc[df['editora'] == entrada].where(
                df['situacao'] == 'Disponível').fillna('').values.tolist()

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
        df = pd.read_csv('autores_livros.csv')

        resultado = df.loc[df['autor'] == entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_editora(self, entrada):
        df = pd.read_csv('editoras_livros.csv')

        resultado = df.loc[df['editora'] == entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_cd(self, entrada, campo_pesquisa):
        df = pd.read_csv('cds.csv')

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
        df = pd.read_csv('dvds.csv')

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
        df = pd.read_csv('autores_artistas_cds.csv')

        resultado = df.loc[df['autor_artista'] ==
                           entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_diretor_dvd(self, entrada):
        df = pd.read_csv('diretores_dvds.csv')

        resultado = df.loc[df['diretor'] == entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_distribuidora_cd(self, entrada):
        df = pd.read_csv('distribuidoras_cds.csv')

        resultado = df.loc[df['distribuidora'] ==
                           entrada].fillna('').values.tolist()

        return resultado

    def pesquisar_distribuidora_dvd(self, entrada):
        df = pd.read_csv('distribuidoras_dvds.csv')

        resultado = df.loc[df['distribuidora'] ==
                           entrada].fillna('').values.tolist()

        return resultado

    def get_livros_emprestimos_expirados(self):
        df = pd.read_csv('livros.csv')

        livros = df.where(pd.to_datetime(df['dt_devolucao'].dropna(
        )).dt.date < date.today()).dropna(axis=0, how='all').values.tolist()

        return livros

    def get_cds_emprestimos_expirados(self):
        df = pd.read_csv('cds.csv')

        cds = df.where(pd.to_datetime(df['dt_devolucao'].dropna(
        )).dt.date < date.today()).dropna(axis=0, how='all').values.tolist()

        return cds

    def get_dvds_emprestimos_expirados(self):
        df = pd.read_csv('dvds.csv')

        dvds = df.where(pd.to_datetime(df['dt_devolucao'].dropna(
        )).dt.date < date.today()).dropna(axis=0, how='all').values.tolist()

        return dvds
